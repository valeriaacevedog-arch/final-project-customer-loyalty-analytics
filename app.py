import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Beyond Points",
    page_icon="🎯",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/customer_loyalty_segments.csv")

df = load_data()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("📂 Navigation")

st.sidebar.info("""
**Beyond Points**

Customer Loyalty Decision Support Tool

Ironhack Final Project
""")

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🎯 Beyond Points")

st.subheader("Customer Loyalty Decision Support Tool")

st.info("""
👋 **Welcome to Beyond Points**

This interactive decision-support application helps CRM and Loyalty Managers transform customer analytics into strategic business decisions.

### 🚀 This application combines:

- 📊 Customer Segmentation
- ⚠️ Churn Prediction
- 🎁 CRM Strategy Recommendation

Use the navigation menu on the left to explore each module.
""")

st.divider()

# ---------------------------------------------------
# EXECUTIVE OVERVIEW
# ---------------------------------------------------

st.subheader("📈 Executive Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="👥 Total Customers",
        value=f"{len(df):,}"
    )

with col2:
    st.metric(
        label="🎯 Customer Segments",
        value=df["Loyalty_Segment"].nunique()
    )

with col3:
    st.metric(
        label="⚠️ Customers at Risk",
        value=int(df["Churn"].sum())
    )

with col4:
    st.metric(
        label="💰 Average Customer Value",
        value=f"€ {df['Monetary'].mean():.2f}"
    )

st.divider()

# ---------------------------------------------------
# CUSTOMER SEGMENTS
# ---------------------------------------------------

st.subheader("📊 Customer Segment Distribution")

st.caption(
    "Distribution of customers across the identified loyalty segments."
)

segment_count = (
    df["Loyalty_Segment"]
    .value_counts()
)

st.bar_chart(segment_count)

st.divider()

# ---------------------------------------------------
# CRM STRATEGIES
# ---------------------------------------------------

st.subheader("🎁 Recommended CRM Strategies")

st.caption(
    "Each customer segment receives a personalized CRM strategy based on customer behaviour."
)

recommendations = (
    df[
        ["Loyalty_Segment", "Recommendation"]
    ]
    .drop_duplicates()
    .sort_values("Loyalty_Segment")
)

st.dataframe(
    recommendations,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ---------------------------------------------------
# DATASET PREVIEW
# ---------------------------------------------------

st.subheader("📋 Dataset Preview")

st.caption(
    "Sample of the analytical dataset used for customer segmentation, churn prediction and CRM recommendations."
)

st.dataframe(
    df.head(20),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.caption(
    "Developed by **Valeria Acevedo** | Ironhack Final Project | Beyond Points 🎯"
)