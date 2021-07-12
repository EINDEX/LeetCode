# Write your MySQL query statement below
with a as(select l1.Id, l1.num from Logs as l1 left join Logs as l2 on l1.Id = l2.Id + 1 where l1.num = l2.num)

select distinct a1.num as ConsecutiveNums from a as a1 left join a as a2 on a1.Id = a2.Id + 1 where a1.num = a2.num
