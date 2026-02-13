import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("retail.db")

# Load data into pandas
df = pd.read_sql("SELECT * FROM sales", conn)

# Create revenue column
df["revenue"] = df["quantity"] * df["price"]

print("----- FULL DATA -----")
print(df)

print("\nTotal Revenue:", df["revenue"].sum())

# Monthly Revenue
df["month"] = df["order_date"].str[:7]
monthly = df.groupby("month")["revenue"].sum()

print("\nMonthly Revenue:")
print(monthly)

# Plot Monthly Revenue
monthly.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# Top Products
top_products = df.groupby("product")["quantity"].sum().sort_values(ascending=False)

print("\nTop Selling Products:")
print(top_products)

conn.close()