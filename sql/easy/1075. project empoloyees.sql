# Write your MySQL query statement below
select p.project_id as project_id , ROUND(AVG(e.experience_years), 2) AS average_years
from Project p
join employee e ON e.employee_id = p.employee_id
GROUP BY 
    p.project_id;