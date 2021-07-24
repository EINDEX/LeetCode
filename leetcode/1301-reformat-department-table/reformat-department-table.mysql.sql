# Write your MySQL query statement below
select 
id,
sum(If(month='Jan', revenue, null)) as Jan_Revenue,
sum(If(month='Feb', revenue, null)) as Feb_Revenue,
sum(If(month='Mar', revenue, null)) as Mar_Revenue,
sum(If(month='Apr', revenue, null)) as Apr_Revenue,
sum(If(month='May', revenue, null)) as May_Revenue,
sum(If(month='Jun', revenue, null)) as Jun_Revenue,
sum(If(month='Jul', revenue, null)) as Jul_Revenue,
sum(If(month='Aug', revenue, null)) as Aug_Revenue,
sum(If(month='Sep', revenue, null)) as Sep_Revenue,
sum(If(month='Oct', revenue, null)) as Oct_Revenue,
sum(If(month='Nov', revenue, null)) as Nov_Revenue,
sum(If(month='Dec', revenue, null)) as Dec_Revenue
from Department 
group by id


