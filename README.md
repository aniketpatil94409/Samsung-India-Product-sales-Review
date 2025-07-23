# Samsung India Product Performance & Customer Sentiment Dashboard

This project analyzes sales, warranty, return behavior, and customer sentiment of Samsung products in India using SQL, Power BI, and Python.


## Project Overview
A 5-page end-to-end BI dashboard built with a combination of:
-  SQL (data querying & filtering)
-  Power BI (interactive dashboard)
-  Python (EDA and reporting)
-  CSV & Excel (data prep)
## Dataset
- `Samsung_Product_Review_Sales.csv`: Contains 4300+ records
- Columns include:
  - `Product_Name`, `Product_Category`, `Revenue_INR`, `Units_Sold`
  - `Platform`, `Region`, `City`, `Star_Rating`
  - `Return_Product`, `Review_Reason`, `Keyword_Extracted`
  - `Sentiment_Label` (Positive/Neutral/Negative)

---
## Power BI Dashboard 
### 1️⃣ Sales Overview
- KPIs: Total Revenue, Total Units Sold
- Bar chart: Revenue by Product Category
- Line chart: Units Sold by State

![Sales Overview](screenshots/Screenshot_1.jpg)


### 2️⃣ Regional Performance
- Map: Revenue by State
- Stacked column: Units by Region and Category
- Pie: Revenue Share by Region

![Sales Overview](screenshots/Screenshot_2.jpg)


### 3️⃣ Product Analysis
- Bar: Top 10 Products by Revenue
- Warranty Claims by Product
- ASP by Product Category
- Gauge: Total Warranty Claims

![Sales Overview](screenshots/Screenshot_3.jpg)


### 4️⃣ Customer Sentiments
- KPI cards: Avg Rating, Review Counts
- Pie chart: Sentiment Breakdown
- Table: Customer Review Details
- Bar chart: Star Rating by Platform

![Sales Overview](screenshots/Screenshot_4.jpg)


### 5️⃣ Channel Performance
- KPIs: Online vs Offline Revenue
- Bar: Revenue by Platform / Store
- Pie: Sales Share by Channel
- Table: Channel wise Customer Feedback

![Sales Overview](screenshots/Screenshot_5.jpg)


---
## Python
(`samsung_product_analysis.py`)

- Uses only `pandas`, `numpy`, and `matplotlib`
- Calculates:
  - ASP (Average Selling Price)
  - Top Product Categories
  - Avg Rating by Platform
  - Simulated Warranty Claim field
- Generates bar plots (optional)

---
## SQL Queries
The project includes a backend SQL script:   `Samsung_Product_Review_Sales.sql`

#### 🔍 Key Queries:
| Query Title                      | Description                                                        |
|----------------------------------|---------------------------------------------------------------------|
| Units Sold by Category           | Aggregates total units by product category                         |
| Revenue by Region                | Total revenue across all states or zones                           |
| Units Sold by States              | Aggregates total units by States                             |
| Return Rate by Platform          | Filters only online platforms, counts return %                     |
| Sentiment Breakdown              | Groups Positive, Neutral, Negative reviews                         |

####  Example:
SELECT Product_Category, SUM(Unit_Sold) AS Total_Units
FROM SamsungData
GROUP BY Product_Category
ORDER BY Total_Units DESC;

##### Skills Demonstrated:

- SQL (grouping, aggregation, filters)
- Power BI (slicers, KPIs, navigation)
- Python (data cleaning, grouping, plotting)
- Business thinking: sentiment analysis, product return behavior, channel comparison

---
## How to Use
1. Clone the repo
2. Open Power BI file: `Samsung_Product_Review_Sales.pbix`
3. Run `samsung_product_analysis.py` or in Jupyter Notebook/vs studio
4. Explore the CSV in Excel or Python
5. Review insights in the README or dashboard screenshots

---
## Conclusion :
This project demonstrates how SQL, Python, and Power BI can be integrated to deliver business insights. It helps uncover patterns in Samsung india product sales and empowers better decision-making for business.
