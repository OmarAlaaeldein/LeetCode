# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE p FROM Person p,Person x WHERE p.email=x.email AND p.id>x.id
