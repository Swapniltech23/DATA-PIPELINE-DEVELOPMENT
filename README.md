# DATA-PIPELINE-DEVELOPMENT

*COMAPNY : CODETECHIT SOLUTIONS

*NAME : SWAPNIL SAHU

*INTERN ID : CT08JDB

*DOMAIN : DATA SCIENCE

*DURATION : 4 WEEKS

*MENTOR : NEELA SANTOSH


#DESCRIPTION OF TASK :
Introduction
The Diwali Sales Dataset contains customer transaction data, including details such as Age, Gender, Product Category, Orders, and Amount Spent. The goal of this project was to clean, process, and enhance the dataset by handling missing values, correcting inconsistencies, and deriving meaningful features. This transformed dataset enables better insights into customer spending behavior, product category sales, and high-value customers.

By implementing an ETL (Extract, Transform, Load) pipeline in Python, I ensured that the data was structured, accurate, and ready for further analysis.

Tasks Performed
1. Data Loading and Cleaning
The dataset was first loaded into a Pandas DataFrame, followed by initial cleaning steps:

*Dropped unnecessary columns like User_ID, Cust_name, and unnamed1, which were not useful for analysis.
*Checked for missing values and filled missing amounts using Mean Imputation to maintain consistency.

2. Handling Data Inconsistencies
The dataset had negative values in the Age and Orders columns, leading to misleading results. To fix this:

*Removed rows where Age was ≤ 0 or > 100, ensuring only realistic values.
*Ensured Orders had only positive values to maintain logical correctness.

3. Encoding Categorical Data
Categorical variables were converted into numerical format to facilitate analysis:

*Gender Encoding: Converted "Male" and "Female" into binary values (0 for Female, 1 for Male) using LabelEncoder().

4. Feature Engineering
To derive better insights from the dataset, several new features were created:
*Total_Spend: Orders × Amount – Represents the total expenditure of each customer.
*Avg_Spend_per_Order: Total_Spend / Orders – Measures how much a customer spends per order.
*Total Sales per Product Category: Grouped data by Product_Category and calculated the total revenue for each category.
*High Spender Flag: Identified Top 25% customers based on total spending using quantile-based segmentation.

These features help in understanding customer purchase behavior and product performance.

5. Data Aggregation & Export
*Merged category-wise total sales into the dataset, providing an overview of how each product category contributes to overall revenue.
*Saved the final cleaned and transformed dataset as final_diwali_sales_data.csv for further business insights and analysis.

Tools & Technologies Used
1)Python – For data processing and automation
2)Pandas & NumPy – Data cleaning, transformation, and calculations
3)Scikit-learn – Used for missing value imputation
4)CSV Files – For storing and exporting processed data

Real-World Applications & Use Cases
1)Customer Segmentation: Identifies high-value customers for better marketing strategies.
2)Sales Trend Analysis: Helps businesses understand which product categories generate maximum revenue.
3)Inventory Management: Assists in stocking more of the best-selling products.
4)Personalized Recommendations: Can be used for targeted product suggestions based on spending behavior.
5)Market Research: Provides insights into how Age, Gender, and Region affect purchasing trends.

Conclusion
This project successfully transformed a raw, unstructured dataset into a clean, structured, and feature-rich dataset. By handling missing values, fixing inconsistencies, and deriving meaningful insights, the final dataset is now accurate, well-organized, and ready for analysis or machine learning applications.

The ETL pipeline ensures that the data is reliable and reusable, making it highly valuable for business analytics, decision-making, and e-commerce strategy planning. 

#OUTPUT
![Image](https://github.com/user-attachments/assets/b327c337-7bf2-429d-84d3-c045e1a8134e)

