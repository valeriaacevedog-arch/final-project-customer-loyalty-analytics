import streamlit as st
import pandas as pd

st.set_page_config(page_title="Churn Prediction", layout="wide")

df = pd.read_csv("data/customer_loyalty_segments.csv")

st.title("⚠️ Churn Prediction")

st.warning("""
Customers predicted as churn should be prioritized in CRM campaigns.
""")

st.divider()

st.metric(
    "Customers Predicted as Churn",
    int(df["Predicted_Churn"].sum())
)

st.divider()

st.subheader("Predicted Churn Distribution")

st.bar_chart(df["Predicted_Churn"].value_counts())

st.divider()

st.subheader("Predicted Churn by Loyalty Segment")

table = (
    df.groupby("Loyalty_Segment")["Predicted_Churn"]
    .sum()
)

st.bar_chart(table)

st.divider()

st.markdown("""
## Recommended Actions

- 🎁 Personalized Discounts

- 💌 Win-back Email Journeys

- ⭐ Bonus Loyalty Points

- 📲 Push Notifications
""")
