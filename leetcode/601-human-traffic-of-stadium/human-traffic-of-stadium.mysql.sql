# Write your MySQL query statement below

select distinct s.* from
(select s1.id as s1_id, s2.id as s2_id, s3.id as s3_id from stadium as s1
join stadium as s2 on s1.id+1 = s2.id
join stadium as s3 on s2.id+1 = s3.id
where s1.people >= 100 and s2.people >= 100 and s3.people >= 100
) as t
join stadium as s on t.s1_id = s.id or t.s2_id = s.id or t.s3_id = s.id
