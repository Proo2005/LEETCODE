# Write your MySQL query statement below
SELECT Person.firstname , Person.lastname ,Address.city , Address.state 
from Person
left JOIN Address
ON Person.personId = Address.personId  

