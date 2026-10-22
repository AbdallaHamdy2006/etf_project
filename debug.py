import pandas as pd

#check the price and NAV data for both ETFs 
etfs = ["XIU_TO", "XBB_TO"]

for etf in etfs:
    #load the historical ETF prices
    prices = pd.read_csv(
        f"data/{etf}_price.csv",
        index_col=0,
        parse_dates=True
    )

    #load the NAV data
    nav = pd.read_csv(f"data/{etf}_nav.csv")

    #make sure the dates and NAV values have the correct format
    nav["Date"] = pd.to_datetime(nav["Date"], errors="coerce")
    nav["NAV"] = pd.to_numeric(nav["NAV"], errors="coerce")

    #remove rows with missing dates or NAV values
    nav = nav.dropna(subset=["Date", "NAV"])

    #use the dates as the index and sort them
    nav = nav.set_index("Date").sort_index()

    #find the dates available in both datasets
    combined = prices.join(nav, how="inner")

    print(etf)

    print(
        "  Price data:",
        prices.index.min().date(), "to",
        prices.index.max().date(),
        "|", len(prices), "rows"
    )

    print(
        "  NAV data:  ",
        nav.index.min().date(), "to",
        nav.index.max().date(),
        "|", len(nav), "rows"
    )

    print("  Overlapping rows:", len(combined))

    #realized after checking the data that for some reason the XIU data was uploaded twice which is why my chart looked off then fixed it