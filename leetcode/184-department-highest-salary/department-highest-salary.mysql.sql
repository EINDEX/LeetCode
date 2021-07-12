# Write your MySQL query statement below

# select d.Name as Department, e.Name as Employee, e.Salary 
# from Employee e 
# join (select Max(Salary) as MaxSalary, DepartmentId from Employee group by DepartmentId) as t
# on e.DepartmentId = t.DepartmentId
# join Department as d on d.Id = e.Id
# # where t.MaxSalary = e.Salary

select d.Name as Department, e.Name as Employee, MaxSalary as Salary
from Employee e 
join (select Max(Salary) as MaxSalary, DepartmentId from Employee group by DepartmentId) as t
on e.DepartmentId = t.DepartmentId and e.Salary = t.MaxSalary
join Department as d on d.Id = e.DepartmentId