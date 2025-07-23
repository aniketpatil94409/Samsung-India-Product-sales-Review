Create database samsung_overall_sales;
use samsung_overall_sales;

#1.Total Units Sold by Product Category
create view Total_units_sold_by_category as
select Product_Category,sum(Units_Sold) as Total_units_sold
from Samsung_Product_Review_Sales
group by Product_Category
order by Total_units_sold desc;

select * from Total_units_sold_by_category;

#2. Total Revenue by Region
create view Total_Revenue_by_region as
select Region,sum(Revenue_INR) as total_Revenue
from Samsung_Product_Review_Sales
group by Region
order by total_Revenue desc;

select * from Total_Revenue_by_region;

#3. Average Star Rating per Product
create view avg_star_rating_per_product as
select Product_Name, round(avg(Star_Rating),2) as avg_Rating
from Samsung_Product_Review_Sales
group by Product_Name
order by avg_Rating desc;

select * from avg_star_rating_per_product;

#4. Total Units Sold by State
create view total_units_sold_by_state as
select state,sum(Units_Sold) as Total_Units
from Samsung_Product_Review_Sales
group by state
order by Total_Units desc;

select * from total_units_sold_by_state;

#5.  Top 5 Most Returned Products
create view Top_5_Returned_Product as 
select Product_Name,count(*) as Total_Return
from Samsung_Product_Review_Sales
where Return_Product = 'Yes'
group by Product_Name 
order by Total_Return desc
limit 5;

select * from Top_5_Returned_Product;

#6. Sentiment Distribution (Positive, Neutral, Negative)
create view Sentiment_Distribution as
SELECT Sentiment_Label, COUNT(*) AS Review_Count
FROM Samsung_Product_Review_Sales
GROUP BY Sentiment_Label;

select * from Sentiment_Distribution;
