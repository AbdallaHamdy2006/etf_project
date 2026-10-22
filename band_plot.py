import numpy as np
import matplotlib.pyplot as plt
from arb_calculator import arbitrage, breakeven_pct

#assume the ETF has a NAV of $30 per share
nav = 30.0

#test premiums and discounts ranging from -1% to +1%
premiums = np.linspace(-1, 1, 200)
prices = nav * (1 + premiums / 100)

#set up the graph
fig, ax = plt.subplots(figsize=(9, 5))

#compare a cheaper basket with a more expensive basket
basket_costs = [
    ("Liquid basket (5 bps)", 5),
    ("Illiquid basket (40 bps)", 40)
]

for name, basket_cost in basket_costs:
    profits = []

    # Calculate the estimated profit at each ETF price
    for price in prices:
        result = arbitrage(
            price,
            nav,
            basket_cost_bps=basket_cost
        )
        profits.append(result[3])

    # Find the break-even premium or discount
    break_even = breakeven_pct(
        nav,
        basket_cost_bps=basket_cost
    )

    label = name + ", break-even +/-" + str(round(break_even, 2)) + "%"
    ax.plot(premiums, profits, label=label)

#add labels and a zero-profit line
ax.axhline(0, color="black", linewidth=0.8)
ax.set_xlabel("Premium (+) / Discount (-), %")
ax.set_ylabel("Estimated arbitrage profit per creation unit ($)")
ax.set_title("Where does arbitrage become profitable?")
ax.legend()

#save and display the graph
plt.savefig("band_chart.png", dpi=150)
plt.show()