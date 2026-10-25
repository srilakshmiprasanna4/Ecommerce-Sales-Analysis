import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("data/superstore.csv", encoding = "latin1")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

# Check Missing Values

print("\nMissing Values in each column:")
print(df.isnull().sum())

# Check Duplicate Rows

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Convert Date columns to datetime

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nUpdated date data types:")
print(df[["Order Date","Ship Date"]].dtypes)

print("\nFirst 5 Order dates:")
print(df["Order Date"].head())

# Understand the data Statistically

print("\nStatistical summery of Dataset:")
pd.set_option("display.max_columns",None)
pd.set_option("display.width",100)
print(df.describe())

# Basic sales and profit analysis

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
average_sales = df["Sales"].mean()
average_profit = df["Profit"].mean()

print("\n--- Sales and Profit Analysis ---")
print("Total Sales:",round(total_sales,2))
print("Total Profit:",round(total_profit,2))
print("Average sales per Row:",round(average_sales,2))
print("Average Profit per Row:",round(average_profit,2))

# Sales by category

sales_by_category = df.groupby("Category")["Sales"].sum()
print("\n--- Total Sales by Category ---")
print(sales_by_category)

# Profit by Category

profit_by_category = df.groupby("Category")["Profit"].sum()
print("\n--- Total Profit by Category")
print(profit_by_category)

# Compare Sales and Profit by Category

category_summary = df.groupby("Category")[["Sales","Profit"]].sum()
print("\n--- Sales and Profit by Category ---")
print(category_summary)

# Sales by Region

sales_by_region = df.groupby("Region")["Sales"].sum()
print("\n--- Total Sales by Region ---")
print(sales_by_region)

# Profit by Region

profit_by_region = df.groupby("Region")["Profit"].sum()
print("\n--- Total Profit by Region ---")
print(profit_by_region)

# Compare Sales and Profit by Region

region_summary = df.groupby("Region")[["Sales","Profit"]].sum()
print("\n--- Sales and Profit by Region ---")
print(region_summary)

# Sales by Year

df["Year"] = df["Order Date"].dt.year
sales_by_year = df.groupby("Year")["Sales"].sum()
print("\n--- Total Sales by Year ---")
print(sales_by_year)

# Sales by Month

df["Month"] = df["Order Date"].dt.month
sales_by_month = df.groupby("Month")["Sales"].sum()
print("\n--- Total Sales by Month ---")
print(sales_by_month)

# Visualize monthly Sales

plt.figure(figsize=(10,5))

plt.bar(sales_by_month.index,sales_by_month.values)

plt.title("Total Sales by Month")
plt.xlabel("Month Number")
plt.ylabel("Total Sales ($)")

plt.xticks(range(1,13))
plt.tight_layout()
plt.savefig("outputs/monthly_sales.png",dpi = 300, bbox_inches = "tight")
plt.show()

# Profit by Year

profit_by_year = df.groupby("Year")["Profit"].sum()
print("\n--- Total Profit by Year ---")
print(profit_by_year)

# Visualize yearly Sales and Profit

plt.figure(figsize=(10, 5))

plt.plot(sales_by_year.index, sales_by_year.values, marker="o", label="Sales")
plt.plot(profit_by_year.index, profit_by_year.values, marker="o", label="Profit")

plt.title("Yearly Sales and Profit")
plt.xlabel("Year")
plt.ylabel("Amount ($)")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("outputs/yearly_sales_profit.png", dpi=300, bbox_inches="tight")
plt.show()

# Top 10 Products by Sales

sales_by_product = df.groupby("Product Name")["Sales"].sum()
top_10_products = sales_by_product.sort_values(ascending = False).head(10)
print("\n--- Top 10 Products by Sales ---")
print(top_10_products.round(2))

# Visualize top 10 products by Sales

plt.figure(figsize=(12, 7))

top_10_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Product Name")

plt.tight_layout()
plt.savefig("outputs/top_10_products_by_sales.png", dpi=300, bbox_inches="tight")
plt.show()

# Top 10 Products by Profit

profit_by_product = df.groupby("Product Name")["Profit"].sum()
top_10_profit_products = profit_by_product.sort_values(ascending=False).head(10)
print("\n--- Top 10 Products by Profit ---")
print(top_10_profit_products.round(2))

# Visualize top 10 products by Profit

plt.figure(figsize=(12,7))
top_10_profit_products.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Profit")
plt.xlabel("Total Profit ($)")
plt.ylabel("Product Name")

plt.tight_layout()
plt.savefig("outputs/top_10_products_by_profit.png",dpi=300,bbox_inches = "tight")
plt.show()

# Visualize profit by Category

profit_by_category = df.groupby("Category")["Profit"].sum()
plt.figure(figsize=(8,5))
profit_by_category.plot(kind = "bar")

plt.title("Total Profit by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Profit ($)")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("outputs/profit_by_category.png",dpi = 300,bbox_inches = "tight")
plt.show()

# Visualize Sales by Category

sales_by_category = df.groupby("Category")["Sales"].sum()
plt.figure(figsize=(8,5))
sales_by_category.plot(kind = "bar")

plt.title("Total Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales ($)")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("outputs/sales_by_category.png",dpi = 300,bbox_inches = "tight")
plt.show()

# Visualize Profit by Region

profit_by_region = df.groupby("Region")["Profit"].sum()
plt.figure(figsize=(8,5))

profit_by_region.plot(kind="bar")
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit ($)")

plt.xticks(rotation = 0)
plt.tight_layout()

plt.savefig("outputs/profit_by_region.png",dpi=300,bbox_inches="tight")
plt.show()

# Visualize Sales by Region

sales_by_region = df.groupby("Region")["Sales"].sum()
plt.figure(figsize=(8,5))

profit_by_region.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales ($)")

plt.xticks(rotation = 0)
plt.tight_layout()

plt.savefig("outputs/sales_by_region.png",dpi=300,bbox_inches="tight")
plt.show()

# Visualize Yearly Profit

profit_by_year = df.groupby("Year")["Profit"].sum()
plt.figure(figsize=(9,5))
profit_by_year.plot(kind="bar")

plt.title("Total Profit by Year")
plt.xlabel("Year")
plt.ylabel("Total Profit ($)")

plt.xticks(rotation = 0)
plt.tight_layout()

plt.savefig("outputs/yearly_profit.png",dpi = 300,bbox_inches = "tight")
plt.show()

# Analyze Profit by Sub-Category

profit_by_subcategory = df.groupby("Sub-Category")["Profit"].sum()
profit_by_subcategory = profit_by_subcategory.sort_values(ascending = False)
print("\n--- Profit by Sub-Category ---")
print(profit_by_subcategory.round(2))

# Visualize Profit by Sub-Category

plt.figure(figsize=(12,7))
profit_by_subcategory.sort_values().plot(kind="barh")

plt.title("Profit by Product Sub_Category")
plt.xlabel("Total Profit ($)")
plt.ylabel("Sub_Category")

plt.axvline(x=0, linewidth=1)
plt.tight_layout()

plt.savefig("outputs/profit_by_subcategory.png",dpi=300,bbox_inches="tight")
plt.show()

# Analyze Sales by Sub-Category

sales_by_subcategory = df.groupby("Sub-Category")["Sales"].sum()
sales_by_subcategory = sales_by_subcategory.sort_values(ascending = False)
print("\n--- Sales by Sub-Category ---")
print(sales_by_subcategory.round(2))

# Visualize Sales by Sub-Category

plt.figure(figsize=(12,7))
sales_by_subcategory.sort_values().plot(kind="barh")

plt.title("Sales by Product Sub_Category")
plt.xlabel("Total Sales ($)")
plt.ylabel("Sub_Category")

plt.tight_layout()

plt.savefig("outputs/sales_by_subcategory.png",dpi=300,bbox_inches="tight")
plt.show()


# Find the highest and lowest profit sub-categories

most_profitable = profit_by_subcategory.idxmax()
highest_profit = profit_by_subcategory.max()

least_profitable = profit_by_subcategory.idxmin()
lowest_profit = profit_by_subcategory.min()

print("\n--- Profitability Insights ---")

print(f"Most profitable sub-category: {most_profitable}")
print(f"Highest profit: ${highest_profit:,.2f}")

print(f"Lowest profit sub-category: {least_profitable}")
print(f"Lowest profit: ${lowest_profit:,.2f}")


# Calculate profit margin by category

category_summary = df.groupby("Category")[["Sales", "Profit"]].sum()

category_summary["Profit Margin (%)"] = (
    category_summary["Profit"] / category_summary["Sales"]
) * 100

print("\n--- Profit Margin by Category ---")
print(category_summary.round(2))


# Find the category with the highest profit margin

best_margin_category = category_summary["Profit Margin (%)"].idxmax()
best_margin = category_summary["Profit Margin (%)"].max()

print("\n--- Best Profit Margin ---")
print(f"Category: {best_margin_category}")
print(f"Profit Margin: {best_margin:.2f}%")


# Visualize profit margin by category

profit_margin_by_category = category_summary["Profit Margin (%)"]

plt.figure(figsize=(8, 5))

profit_margin_by_category.plot(kind="bar")

plt.title("Profit Margin by Category")
plt.xlabel("Product Category")
plt.ylabel("Profit Margin (%)")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("outputs/profit_margin_by_category.png",dpi=300,bbox_inches="tight")
plt.show()
















