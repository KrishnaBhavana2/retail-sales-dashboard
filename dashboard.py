import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Smart Retail Dashboard", layout="wide")

st.title("📊 Smart Retail Sales Analytics Dashboard")

# Connect to database
conn = sqlite3.connect("retail.db")
df = pd.read_sql("SELECT * FROM sales", conn)

df["revenue"] = df["quantity"] * df["price"]
df["month"] = df["order_date"].str[:7]

# Metrics Section
total_revenue = df["revenue"].sum()
total_orders = df["order_id"].count()
unique_customers = df["customer_id"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"₹{total_revenue:,}")
col2.metric("📦 Total Orders", total_orders)
col3.metric("👥 Unique Customers", unique_customers)

st.divider()

# Monthly Revenue Chart
st.subheader("📈 Monthly Revenue Trend")
monthly = df.groupby("month")["revenue"].sum()
st.line_chart(monthly)

# Top Products
st.subheader("🏆 Top Selling Products")
top_products = df.groupby("product")["quantity"].sum()
st.bar_chart(top_products)

conn.close()