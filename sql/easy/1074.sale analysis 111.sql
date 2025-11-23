# Write your MySQL query statement below
select p.product_id as product_id, p.product_name as product_name
from Product p
join sales s on s.product_id = p.product_id 
where s.sale_date BETWEEN '2019-01-01' AND '2019-03-31' ;
