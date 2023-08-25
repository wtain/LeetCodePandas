"""
https://leetcode.com/problems/rearrange-products-table/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Create table If Not Exists Products (product_id int, store1 int, store2 int, store3 int)
Truncate table Products
insert into Products (product_id, store1, store2, store3) values ('0', '95', '100', '105')
insert into Products (product_id, store1, store2, store3) values ('1', '70', 'None', '80')

data = [[0, 95, 100, 105], [1, 70, None, 80]]
Products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'int64', 'store1':'int64', 'store2':'int64', 'store3':'int64'})

Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.


Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
Output:
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
Explanation:
Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.
"""

import pandas as pd

# Runtime
# Details
# 512ms
# Beats 7.29%of users with Pandas
# Memory
# Details
# 60.99MB
# Beats 56.68%of users with Pandas
# https://leetcode.com/problems/rearrange-products-table/solutions/3849226/pandas-vs-sql-elegant-short-all-30-days-of-pandas-solutions/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(products, id_vars='product_id', var_name='store', value_name='price').dropna()


data = [[0, 95, 100, 105], [1, 70, None, 80]]
Products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'Int64', 'store1':'Int64', 'store2':'Int64', 'store3':'Int64'})

print(rearrange_products_table(Products))
