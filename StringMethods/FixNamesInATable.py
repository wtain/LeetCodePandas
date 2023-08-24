"""
https://leetcode.com/problems/fix-names-in-a-table/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Create table If Not Exists Users (user_id int, name varchar(40))
Truncate table Users
insert into Users (user_id, name) values ('1', 'aLice')
insert into Users (user_id, name) values ('2', 'bOB')

data = [[1, 'aLice'], [2, 'bOB']]
Users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})

Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.


Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

The result format is in the following example.



Example 1:

Input:
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
Output:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
"""

import pandas as pd

# def fix_names(users: pd.DataFrame) -> pd.DataFrame:
#
#     def canonize(name: str) -> str:
#         return name[0].upper() + name[1:].lower()
#
#     users['name'] = canonize(users['name'].str)
#     return users.sort_values(by='user_id', ascending=True)


# Runtime
# Details
# 596ms
# Beats 5.09%of users with Pandas
# Memory
# Details
# 62.04MB
# Beats 6.89%of users with Pandas
# https://leetcode.com/problems/fix-names-in-a-table/solutions/3853461/2-steps-pandas-approach-mysql-with-comments-and-explanation/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values(by='user_id', ascending=True)


data = [[1, 'aLice'], [2, 'bOB']]
Users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})


print(fix_names(Users))
