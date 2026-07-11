# final-project-customer-loyalty-analytics
Final Project

## 🎯 Business Problem

Companies collect large amounts of customer data every day, but many struggle to transform that information into effective loyalty actions.

Traditional loyalty programs often use generic campaigns that fail to address the different needs and behaviors of customers.

This project aims to answer three key business questions:

- What customer segments exist?
- What differentiates each segment?
- Which loyalty strategy should be applied to each segment?

---

## Project Objectives

The main objectives of this project are:

- Analyze customer purchasing behavior.
- Identify different customer loyalty segments.
- Predict customers at risk of churn.
- Recommend personalized loyalty strategies.
- Support CRM decision-making through an interactive dashboard.

---

## Dataset

This project uses the **Brazilian E-commerce Public Dataset by Olist**, available on Kaggle.

The dataset contains information about:

- Customers
- Orders
- Products
- Payments
- Customer reviews
- Delivery performance

After data cleaning and feature engineering, a Customer Analytical Dataset (CAD) was created to perform customer segmentation and churn prediction.

## Features

- Customer segmentation
- Churn prediction
- Business insights dashboard
- Loyalty strategy recommendations

## Tech Stack

- Python
- Pandas
- Streamlit


## Project Structure

```text
BeyondPoints/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── customer_loyalty_segments.csv
│
├── pages/
│   ├── 1_Data_Understanding.py
│   ├── 2_Business_Insights.py
│   ├── 3_Customer_Segmentation.py
│   ├── 4_Churn_Prediction.py
│   └── 5_Loyalty_Strategy.py
│
└── notebooks/
    └── FinalProject.ipynb

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py