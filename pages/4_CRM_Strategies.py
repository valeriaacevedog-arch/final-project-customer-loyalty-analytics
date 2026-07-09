import streamlit as st
import pandas as pd

st.set_page_config(page_title="CRM Strategies", layout="wide")

df = pd.read_csv("data/customer_loyalty_segments.csv")

st.title("🎁 CRM Strategies")

st.success("""
Each customer segment receives an automatically generated CRM recommendation.
""")

st.divider()

recommendations = (
    df[
        ["Loyalty_Segment","Recommendation"]
    ]
    .drop_duplicates()
)

st.dataframe(
    recommendations,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.markdown("""
## Recommended CRM Actions

🏆 Champions

• Exclusive VIP Rewards

• Early Access

• Referral Campaigns

---

❤️ Loyal Customers

• Personalized Promotions

• Cross-selling

• Frequency Campaigns

---

⚠️ At Risk

• Win-back Campaigns

• High-value Incentives

• Discount Coupons

---

🌱 Potential Loyalists

• Second Purchase Discounts

• Loyalty Education

• Product Recommendations
""")
