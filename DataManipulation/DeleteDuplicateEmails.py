"""
https://leetcode.com/problems/delete-duplicate-emails/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Create table If Not Exists Person (Id int, Email varchar(255))
Truncate table Person
insert into Person (id, email) values ('1', 'john@example.com')
insert into Person (id, email) values ('2', 'bob@example.com')
insert into Person (id, email) values ('3', 'john@example.com')

data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
Person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'int64', 'email':'object'})


Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.


Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

For Pandas users, please note that you are supposed to modify Person in place.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

The result format is in the following example.



Example 1:

Input:
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.
"""

import pandas as pd

# Modify Person in place
# def delete_duplicate_emails(person: pd.DataFrame) -> None:
#     min_ids = person.groupby('email').min()
#     person.drop(person.groupby('email')['id'] == min_ids['id'], inplace=True)


# Runtime
# Details
# 435ms
# Beats 5.05%of users with Pandas
# Memory
# Details
# 60.79MB
# Beats 77.64%of users with Pandas
# https://leetcode.com/problems/delete-duplicate-emails/solutions/3863077/pandas-2-liner-very-simple-approach/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id', ascending=True, inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)


data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
Person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'int64', 'email':'object'})


delete_duplicate_emails(Person)
print(Person)