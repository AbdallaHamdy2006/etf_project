
import streamlit as st
from arb_calculator import arbitrage, breakeven_pct

# Page title
st.title("ETF Create/Redeem Arbitrage Calculator")

#enter the ETF details
nav = st.number_input("NAV per share ($)", value=29.91)
price = st.number_input("ETF market price ($)", value=30.00)

#enter the unit size and trading costs
unit_size = st.number_input(
    "Creation unit size (shares)", value=50000, step=1000
)

basket_cost = st.slider("Basket trading cost (bps)", 0, 100, 5)
etf_cost = st.slider("ETF trading cost (bps)", 0, 50, 2)
fixed_fee = st.number_input("Fixed creation/redemption fee ($)", value=500)

#calculate the estimated arbitrage result
action, gross, costs, profit = arbitrage(
    price, nav, unit_size, basket_cost, etf_cost, fixed_fee
)

#display the results
st.subheader(action)

st.metric("Gross price gap", f"${gross:,.2f}")
st.metric("Total costs", f"${costs:,.2f}")
st.metric("Estimated net profit", f"${profit:,.2f}")

break_even = breakeven_pct(
    nav, unit_size, basket_cost, etf_cost, fixed_fee
)

st.write(f"Break-even gap: +/-{break_even:.3f}%")

# Show whether the estimated trade covers its costs
if profit > 0:
    st.success("The estimated profit is positive after costs.")
else:
    st.warning("The estimated profit does not cover the costs.")
