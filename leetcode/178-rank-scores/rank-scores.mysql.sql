# Write your MySQL query statement below

select s.Score as Score, sr.rank as Rank 
from scores as s
left join
(select score, (@row_number:=@row_number+1) as rank from (select distinct(score) as score
     from scores order by score desc) as ss, (SELECT @row_number:=0) as t) as sr 
on s.score = sr.score 
order by Rank
