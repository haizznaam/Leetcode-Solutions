-- Write your MySQL query statement below

WITH merged_table AS (
    SELECT 
        d.name as Department, 
        e.name as Employee, 
        e.salary as Salary
    FROM 
        Employee e LEFT JOIN Department d 
        ON e.departmentId = d.id)


SELECT * 
FROM 
    merged_table
WHERE 
    (Department, Salary) IN (
        SELECT Department, MAX(Salary)
        FROM merged_table
        GROUP BY Department
    );