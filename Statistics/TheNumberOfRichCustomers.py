"""
https://leetcode.com/problems/the-number-of-rich-customers/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Create table If Not Exists Store (bill_id int, customer_id int, amount int)
Truncate table Store
insert into Store (bill_id, customer_id, amount) values ('6', '1', '549')
insert into Store (bill_id, customer_id, amount) values ('8', '1', '834')
insert into Store (bill_id, customer_id, amount) values ('4', '2', '394')
insert into Store (bill_id, customer_id, amount) values ('11', '3', '657')
insert into Store (bill_id, customer_id, amount) values ('13', '3', '257')

data = [[6, 1, 549], [8, 1, 834], [4, 2, 394], [11, 3, 657], [13, 3, 257]]
Store = pd.DataFrame(data, columns=['bill_id', 'customer_id', 'amount']).astype({'bill_id':'int64', 'customer_id':'int64', 'amount':'int64'})


Table: Store

+-------------+------+
| Column Name | Type |
+-------------+------+
| bill_id     | int  |
| customer_id | int  |
| amount      | int  |
+-------------+------+
bill_id is the primary key (column with unique values) for this table.
Each row contains information about the amount of one bill and the customer associated with it.


Write a solution to report the number of customers who had at least one bill with an amount strictly greater than 500.

The result format is in the following example.



Example 1:

Input:
Store table:
+---------+-------------+--------+
| bill_id | customer_id | amount |
+---------+-------------+--------+
| 6       | 1           | 549    |
| 8       | 1           | 834    |
| 4       | 2           | 394    |
| 11      | 3           | 657    |
| 13      | 3           | 257    |
+---------+-------------+--------+
Output:
+------------+
| rich_count |
+------------+
| 2          |
+------------+
Explanation:
Customer 1 has two bills with amounts strictly greater than 500.
Customer 2 does not have any bills with an amount strictly greater than 500.
Customer 3 has one bill with an amount strictly greater than 500.
"""

import pandas as pd


# def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
#     return store[store['amount'] > 500][['customer_id']].drop_duplicates().count().rename({'customer_id': 'rich_count'})

# Runtime
# Details
# 476ms
# Beats 5.01%of users with Pandas
# Memory
# Details
# 61.13MB
# Beats 17.20%of users with Pandas
# https://leetcode.com/problems/the-number-of-rich-customers/solutions/3883540/pandas-very-simple-approach/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    num_rich = store[store['amount'] > 500]['customer_id'].nunique()
    return pd.DataFrame({'rich_count': [num_rich]})


data = [[6, 1, 549], [8, 1, 834], [4, 2, 394], [11, 3, 657], [13, 3, 257]]
Store = pd.DataFrame(data, columns=['bill_id', 'customer_id', 'amount']).astype({'bill_id':'int64', 'customer_id':'int64', 'amount':'int64'})

print(count_rich_customers(Store))
