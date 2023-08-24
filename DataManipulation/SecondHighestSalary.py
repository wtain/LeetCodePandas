"""
https://leetcode.com/problems/second-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Create table If Not Exists Employee (id int, salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')

data = [[1, 100], [2, 200], [3, 300]]
Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.


Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.



Example 1:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
"""

import pandas as pd

# def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
#     salaries = employee['salary']
#     maxv = salaries.max()
#     return salaries[salaries['salary'] < maxv].max()


# Runtime
# Details
# 527ms
# Beats 5.44%of users with Pandas
# Memory
# Details
# 60.83MB
# Beats 44.18%of users with Pandas
# def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
#     sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
#     if len(sorted_salaries) < 2:
#         return pd.DataFrame({'SecondHighestSalary': [None]})
#     second_highest = sorted_salaries.iloc[1]
#     return pd.DataFrame({'SecondHighestSalary': [second_highest]})


# Runtime
# Details
# 407ms
# Beats 5.44%of users with Pandas
# Memory
# Details
# 61.85MB
# Beats 5.21%of users with Pandas
# https://leetcode.com/problems/second-highest-salary/solutions/3859199/pandas-an-effortless-and-simple-approach-with-comments/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique = employee['salary'].drop_duplicates()
    second_highest = unique.nlargest(2).iloc[-1] if len(unique) >= 2 else None
    if second_highest is None:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})

data = [[1, 100], [2, 200], [3, 300]]
Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})


print(second_highest_salary(Employee))


