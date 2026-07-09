import streamlit as st
import pandas as pd

# ==================================================
# PAGE CONFIGURATION
# ==================================================
st.set_page_config(
    page_title="Beyond Points",
    page_icon="🎯",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================
@st.cache_data
def load_data():
    customers = pd.read_csv("data/customer_analytical_dataset.csv")
    segments = pd.read_csv("data/customer_loyalty_segments.csv")
    return customers, segments

customers, segments = load_data()

# ==================================================
# HOME PAGE
# ==================================================
st.title("🎯 Beyond Points")

st.subheader("Customer Loyalty Decision Support Tool")

st.markdown("""
Welcome to **Beyond Points**, an interactive decision support tool that helps CRM and Loyalty Managers transform historical customer data into strategic business decisions.

### Business Questions

1. Who are our customers?
2. What differentiates each customer segment?
3. Which loyalty strategy should be applied to each segment?
""")

st.divider()

# ==================================================
# QUICK METRICS
# ==================================================
col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Customers",
        value=f"{customers.shape[0]:,}"
    )

with col2:
    st.metric(
        label="Customer Segments",
        value=segments["segment"].nunique()
    )

st.divider()

st.subheader("Customer Dataset Preview")

st.dataframe(customers.head())