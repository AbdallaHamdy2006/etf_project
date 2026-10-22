
from premium_discount import load

#compare XIU and XBB during calm and stressful periods
etfs = ["XIU_TO", "XBB_TO"]

for etf in etfs:
    data = load(etf)

    #Data from the calmer period
    calm_period = data.loc["2019-06-01":"2020-01-31", "prem_pct"]

    #Data from the market stress period
    stress_period = data.loc["2020-03-01":"2020-04-15", "prem_pct"]

    print(etf)

    #Check how much the premium or discount changed or varied during the calm and stress periods
    print(
        "  Calm period - standard deviation:",
        round(calm_period.std(), 3),
        "Largest gap:",
        round(calm_period.abs().max(), 3)
    )

    print(
        "  Stress period - standard deviation:",
        round(stress_period.std(), 3),
        "Largest gap:",
        round(stress_period.abs().max(), 3)
    )
