"""
https://leetcode.com/problems/count-salary-categories/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Create table If Not Exists Accounts (account_id int, income int)
Truncate table Accounts
insert into Accounts (account_id, income) values ('3', '108939')
insert into Accounts (account_id, income) values ('2', '12747')
insert into Accounts (account_id, income) values ('8', '87709')
insert into Accounts (account_id, income) values ('6', '91796')

data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
Accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})

Table: Accounts

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.


Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
Output:
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
Explanation:
Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.
"""


import pandas as pd


# Runtime
# Details
# 525ms
# Beats 7.17%of users with Pandas
# Memory
# Details
# 83.92MB
# Beats 75.14%of users with Pandas
def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    total_count = accounts.shape[0]
    low_count = accounts[accounts['income'] < 20000].shape[0]
    high_count = accounts[accounts['income'] > 50000].shape[0]
    average_count = total_count - low_count - high_count
    return pd.DataFrame({'category': ['High Salary', 'Average Salary', 'Low Salary'],
                         'accounts_count': [high_count, average_count, low_count]})


data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
Accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})

print(count_salary_categories(Accounts))
