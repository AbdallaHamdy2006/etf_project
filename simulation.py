import numpy as np
import matplotlib.pyplot as plt

def run_simulation(threshold, arb_power, steps=2000, vol=0.05, seed_val=42):
    #setting up a random number generator
    rng = np.random.default_rng(seed_val)       
    
    premium_series = np.zeros(steps)                      
    
    for i in range(1, steps):
        # random shock from order flow
        shock = rng.normal(0, vol)
        p = premium_series[i - 1] + shock    
        
        #check if premium exceeds the threshold
        if abs(p) > threshold:                       
            # calculate how much it went over the band
            excess_amount = p - np.sign(p) * threshold      
            # arbitrageurs pull the price back
            p = p - (arb_power * excess_amount)
            
        premium_series[i] = p
        
    return premium_series


if __name__ == '__main__':
    # define different scenarios to test
    scenarios = [
        ('No arbitrage (no APs)', 0.10, 0.0),
        ('Liquid Stock basket: band +/-0.10%', 0.10, 0.8),
        ('Illiquid Bond basket: band +/-0.40%', 0.40, 0.8),
    ]

    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    
    for idx, scn in enumerate(scenarios):
        label = scn[0]
        thr = scn[1]
        strength = scn[2]
        
        sim_data = run_simulation(thr, strength)
        
        current_ax = axes[idx]
        current_ax.plot(sim_data)
        current_ax.axhline(0, color='black', linewidth=0.8)
        
        if strength > 0:
            current_ax.axhline(thr, color='red', linestyle='--')
            current_ax.axhline(-thr, color='red', linestyle='--')
            
        current_ax.set_title(label)
        current_ax.set_ylabel('Premium, %')
        
        # print out stats
        print("Scenario:", label)
        print("Typical gap (std):", round(sim_data.std(), 3))
        print("Worst gap (max abs):", round(abs(sim_data).max(), 3))
        print("-" * 40)

    plt.xlabel('Time step')
    plt.tight_layout()
    plt.savefig('simulation_chart.png', dpi=150)
    plt.show()