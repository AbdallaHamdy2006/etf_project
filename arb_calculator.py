def arbitrage(etf_price, nav, unit_size=50000,
              basket_cost_bps=5, etf_cost_bps=2, fixed_fee=500):

    #calculates the value of the creation unit
    total_value = nav * unit_size

    #calculates the difference between the ETF price and its NAV
    price_difference = abs(etf_price - nav) * unit_size

    #estimates the total transaction costs - couldn't find reliable data on the average etf trading costs
    print("Estimating total transaction costs...")
    cost_rate = basket_cost_bps + etf_cost_bps
    costs = total_value * cost_rate / 10000 + fixed_fee

    #decides whether creating or redeeming shares makes more sense based on whether the ETF is trading at a premium or discount to its NAV
    if etf_price > nav:
        action = "CREATE"
    else:
        action = "REDEEM"

    #calculate the profit after costs
    profit = price_difference - costs

    return action, price_difference, costs, profit


def breakeven_pct(nav, unit_size=50000,
                  basket_cost_bps=5, etf_cost_bps=2, fixed_fee=500):

    #calculates the costs as a percentage of the total value
    total_value = nav * unit_size
    cost_rate = basket_cost_bps + etf_cost_bps
    costs = total_value * cost_rate / 10000 + fixed_fee

    return costs / total_value * 100


if __name__ == "__main__":
    etf_price = 30.00
    nav = 29.91

    action, gap, costs, profit = arbitrage(etf_price, nav)

    print("Action:", action)
    print("Gross price gap: $", round(gap, 2))
    print("Estimated costs: $", round(costs, 2))
    print("Estimated profit: $", round(profit, 2))
    print("Break-even gap: +/-", round(breakeven_pct(nav), 4), "%")