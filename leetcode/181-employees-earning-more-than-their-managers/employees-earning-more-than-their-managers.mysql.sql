# Write your MySQL query statement below
select e.name as Employee
from employee as e
left join employee as m on e.ManagerId = m.Id
where e.Salary > m.Salary