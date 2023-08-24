"""
https://leetcode.com/problems/nth-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')

ains information about the salary of an employee.


Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

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
n = 2
Output:
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output:
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
"""

import pandas as pd


# Runtime
# Details
# 484ms
# Beats 5.13%of users with Pandas
# Memory
# Details
# 60.33MB
# Beats 78.74%of users with Pandas
# https://leetcode.com/problems/nth-highest-salary/solutions/3858402/very-simple-and-clean-pandas-with-comments/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(sorted_salaries) < N:
        return pd.DataFrame({'getNthHighestSalary': [None]})
    nth_highest = sorted_salaries.iloc[N - 1]
    return pd.DataFrame({'getNthHighestSalary': [nth_highest]})


data = [
    [1, 100],
    [2, 200],
    [3, 300],
]
Salaries = pd.DataFrame(data, columns=['id', 'salary']).astype(
    {
        'id':'int64',
        'salary':'int64',
    }
)

print(nth_highest_salary(Salaries, 2)) # 200


data = [
    [1, 100],
]
Salaries = pd.DataFrame(data, columns=['id', 'salary']).astype(
    {
        'id':'int64',
        'salary':'int64',
    }
)

print(nth_highest_salary(Salaries, 2)) # null
