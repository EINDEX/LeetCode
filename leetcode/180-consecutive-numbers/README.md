# Consecutive Numbers

## Difficulty
Medium

## Question
<p>Table: <code>Logs</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
id is the primary key for this table.
</pre>

<p>&nbsp;</p>

<p>Write an SQL query to find all numbers that appear at least three times consecutively.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The query result format is in the following example:</p>

<p>&nbsp;</p>

<pre>
Logs table:
+----+-----+
| Id | Num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+

Result table:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
1 is the only number that appears consecutively for at least three times.
</pre>



## Solution
### mysql
```mysql
# Write your MySQL query statement below
with a as(select l1.Id, l1.num from Logs as l1 left join Logs as l2 on l1.Id = l2.Id + 1 where l1.num = l2.num)

select distinct a1.num as ConsecutiveNums from a as a1 left join a as a2 on a1.Id = a2.Id + 1 where a1.num = a2.num

```