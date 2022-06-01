# Write your MySQL query statement below
UPDATE Salary SET
sex = CASE sex
    WHEN 'f' THEN 'm'
    ElSE 'f'
END;