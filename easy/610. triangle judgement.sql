# Write your MySQL query statement below
SELECT * ,
CASE 
WHEN x+y>z AND z+y>x AND x+z>y THEN 'Yes'
ELSE 'No'
END AS triangle
FROM Triangle