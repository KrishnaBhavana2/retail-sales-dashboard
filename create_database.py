import sqlite3

# Create connection
conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER,
    order_date TEXT,
    customer_id INTEGER,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    city TEXT
)
""")

# Insert sample data
data = [
    (1, "2024-01-10", 101, "Laptop", "Electronics", 1, 50000, "Hyderabad"),
    (2, "2024-01-15", 102, "Mobile", "Electronics", 2, 20000, "Chennai"),
    (3, "2024-02-05", 103, "Shoes", "Fashion", 3, 3000, "Mumbai"),
    (4, "2024-02-20", 101, "Headphones", "Electronics", 2, 1500, "Delhi"),
    (5, "2024-03-01", 104, "Watch", "Fashion", 1, 5000, "Bangalore"),
]

cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?, ?)", data)

conn.commit()
conn.close()

print("✅ Database Created Successfully!")