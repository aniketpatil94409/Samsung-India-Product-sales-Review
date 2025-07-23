# Samsung Product Performance & Customer Sentiment Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv(r"C:\\Users\\Lenovo\\Desktop\\Project Analysis\\Samsung_Sales_Project\\Samsung_Product_Review_Sales.csv")


# 2. Basic Info
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Column Names:", df.columns.tolist())
print("Missing Values:\n", df.isnull().sum())

# 3. Add Average Selling Price (ASP)
df["ASP"] = df["Revenue_INR"] / df["Units_Sold"]

# 4. Create Warranty_Claimed Column
df["Warranty_Claimed"] = np.where(
    (df["Return_Product"] == "Yes") | (df["Star_Rating"] <= 2), "Yes", "No"
)

# 5. Summary Stats
print("\nSummary Statistics:")
print(df.describe())

# 6. Top 5 Product Categories by Revenue
top_categories = df.groupby("Product_Category")["Revenue_INR"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Categories by Revenue:\n", top_categories)

# 7. Average Star Rating by Platform
avg_rating = df.groupby("Platform")["Star_Rating"].mean()
print("\nAverage Star Rating by Platform:\n", avg_rating)

# 8. Plot 1: Top Categories by Revenue
plt.figure(figsize=(8, 5))
top_categories.plot(kind="bar", color="orange")
plt.title("Top 5 Product Categories by Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()

# 9. Plot 2: Average Star Rating by Platform
plt.figure(figsize=(8, 5))
avg_rating.plot(kind="bar", color="skyblue")
plt.title("Average Star Rating by Platform")
plt.xlabel("Platform")
plt.ylabel("Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
