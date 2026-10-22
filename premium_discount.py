import pandas as pd
import matplotlib.pyplot as plt

def load_data(ticker):
    #load price data
    price_df = pd.read_csv(f'data/{ticker}_price.csv', index_col=0, parse_dates=True)
    price_df = price_df.iloc[:, [0]] # grab first col
    price_df.columns = ['price']
    price_df['price'] = pd.to_numeric(price_df['price'], errors='coerce')

    #load NAV data
    nav_df = pd.read_csv(f'data/{ticker}_nav.csv')
    nav_df = nav_df.iloc[:, :2]                     
    nav_df.columns = ['Date', 'NAV']             
    nav_df['Date'] = pd.to_datetime(nav_df['Date'], errors='coerce')
    nav_df['NAV'] = pd.to_numeric(nav_df['NAV'], errors='coerce')
    
    #clean up the nav df a bit
    nav_df = nav_df.dropna()
    nav_df = nav_df.drop_duplicates(subset='Date')
    nav_df = nav_df.set_index('Date')
    nav_df = nav_df.sort_index()

    #merge them together on date index
    combined = price_df.join(nav_df, how='inner')
    combined = combined.dropna(subset=['price', 'NAV'])
    
    #calculate premium or discount percentage
    combined['prem_pct'] = ((combined['price'] - combined['NAV']) / combined['NAV']) * 100
    
    return combined

if __name__ == '__main__':
    #testing out a couple funds
    my_funds = ['XIU_TO', 'XBB_TO']
    
    plt.figure(figsize=(10, 5))
    
    for fund in my_funds:
        df = load_data(fund)
        
        plt.plot(df.index, df['prem_pct'], label=fund)
        
        # print some stats to check values
        print("Fund:", fund)
        print("Rows loaded:", len(df))
        print("Avg prem/disc:", df['prem_pct'].mean())
        print("Max:", df['prem_pct'].max())
        print("Min:", df['prem_pct'].min())
        print("-" * 30)

    plt.axhline(0, color='black', linewidth=0.8)
    plt.ylabel('Premium (+) / Discount (-) to NAV, %')
    plt.title('ETF price vs NAV comparison')
    plt.legend()
    
    plt.savefig('premium_chart.png', dpi=150)
    plt.show()




