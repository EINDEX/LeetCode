# Write your MySQL query statement below

select class from (select count(distinct(student)) as t, class from courses group by class order by t desc) as a where a.t >=5;
