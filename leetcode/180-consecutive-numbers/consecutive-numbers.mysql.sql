# Write your MySQL query statement below
# with a as()

# select distinct a1.num as ConsecutiveNums from a as a1 left join a as a2 on a1.Id = a2.Id + 1 where a1.num = a2.num

select distinct l1.num as ConsecutiveNums from Logs as l1 
join Logs as l2 on l1.Id = l2.Id - 1 and l1.num = l2.num
join Logs as l3 on l2.Id = l3.Id - 1 and l2.num = l3.num