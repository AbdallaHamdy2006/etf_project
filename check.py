import pandas as pd

for name in ['XIU_TO', 'XBB_TO']:
    path = f'data/{name}_nav.csv'
    with open(path) as f:
        print(name, '- first line on disk:', repr(f.readline()))

    nav = pd.read_csv(path)
    print('  columns pandas sees:', list(nav.columns))
    nav = nav.iloc[:, :2]
    nav.columns = ['Date', 'NAV']
    nav['Date'] = pd.to_datetime(nav['Date'], errors='coerce')
    nav['NAV'] = pd.to_numeric(nav['NAV'], errors='coerce')
    bad = (nav['Date'].isna() | nav['NAV'].isna()).sum()
    print('  unreadable rows:', int(bad))

    nav = nav.dropna().drop_duplicates(subset='Date').set_index('Date').sort_index()
    print('  NAV on June 3-5, 2019:', nav.loc['2019-06-03':'2019-06-05', 'NAV'].tolist())

