import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Executive Dashboard", layout="wide")

# --------------------------
# LOAD DATA
# --------------------------

df = pd.read_csv("data/customer_loyalty_segments.csv")

# --------------------------
# TITLE
# --------------------------

st.title("📊 Executive Dashboard")

st.markdown(
"""
Overview of customer behaviour and loyalty performance.
"""
)

# --------------------------
# KPIs
# --------------------------

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "👥 Customers",
    f"{len(df):,}"
)

col2.metric(
    "⭐ Segments",
    df["Loyalty_Segment"].nunique()
)

col3.metric(
    "⚠️ Churn Risk",
    int(df["Predicted_Churn"].sum())
)

col4.metric(
    "💰 Avg Monetary",
    f"€{df['Monetary'].mean():.2f}"
)

st.divider()

# --------------------------
# SEGMENTS
# --------------------------

segment_counts = (
    df["Loyalty_Segment"]
    .value_counts()
    .reset_index()
)

segment_counts.columns = [
    "Segment",
    "Customers"
]

fig = px.bar(
    segment_counts,
    x="Segment",
    y="Customers",
    color="Segment",
    text="Customers"
)

fig.update_layout(
    showlegend=False,
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------
# CHURN
# --------------------------

st.subheader("⚠️ Churn Prediction")

churn = (
    df["Predicted_Churn"]
    .value_counts()
    .reset_index()
)

churn.columns = [
    "Status",
    "Customers"
]

churn["Status"] = churn["Status"].map({
    0:"Safe",
    1:"At Risk"
})

fig2 = px.pie(
    churn,
    values="Customers",
    names="Status",
    hole=.5
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
