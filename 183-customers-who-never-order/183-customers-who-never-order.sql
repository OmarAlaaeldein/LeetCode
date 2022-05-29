# Write your MySQL query statement below
SELECT p.name as Customers FROM Customers p Where p.id NOT IN (SELECT o.customerId FROM Orders o )