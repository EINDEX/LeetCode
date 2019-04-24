# Write your MySQL query statement below
SELECT w.Id 
FROM Weather AS w
JOIN Weather AS wj ON DATEDIFF(w.RecordDate, wj.RecordDate) = 1
AND w.Temperature > wj.Temperature