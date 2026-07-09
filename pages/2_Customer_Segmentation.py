import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Segmentation", layout="wide")

df = pd.read_csv("data/customer_loyalty_segments.csv")

st.title("📊 Customer Segmentation")

st.info("""
Customers were segmented using the RFM model and K-Means clustering.
""")

st.divider()

st.subheader("Segment Distribution")

st.bar_chart(df["Loyalty_Segment"].value_counts())

st.divider()

st.subheader("Average Recency")

st.bar_chart(df.groupby("Loyalty_Segment")["Recency"].mean())

st.subheader("Average Frequency")

st.bar_chart(df.groupby("Loyalty_Segment")["Frequency"].mean())

st.subheader("Average Monetary")

st.bar_chart(df.groupby("Loyalty_Segment")["Monetary"].mean())

st.divider()

st.markdown("""
## Key Business Insights

🏆 Champions generate the highest value.

❤️ Loyal Customers purchase frequently.

⚠️ At Risk customers require retention campaigns.

🌱 Potential Loyalists should receive second-purchase incentives.
""")
