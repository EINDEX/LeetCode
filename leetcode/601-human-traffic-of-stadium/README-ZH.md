# Human Traffic of Stadium

## Difficulty
Hard

## Question
<p>Table: <code>Stadium</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
visit_date is the primary key for this table.
Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
No two rows will have the same visit_date, and as the id increases, the dates increase as well.
</pre>

<p>&nbsp;</p>

<p>Write an SQL query to display the records with three or more rows with <strong>consecutive</strong> <code>id</code>&#39;s, and the number of people is greater than or equal to 100 for each.</p>

<p>Return the result table ordered by <code>visit_date</code> in <strong>ascending order</strong>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>

<pre>
<code>Stadium</code> table:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+

Result table:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
The four rows with ids 5, 6, 7, and 8 have consecutive ids and each of them has &gt;= 100 people attended. Note that row 8 was included even though the visit_date was not the next day after row 7.
The rows with ids 2 and 3 are not included because we need at least three consecutive ids.</pre>


## Solution
### mysql
```mysql
# Write your MySQL query statement below

select distinct s.* from
(select s1.id as s1_id, s2.id as s2_id, s3.id as s3_id from stadium as s1
join stadium as s2 on s1.id+1 = s2.id
join stadium as s3 on s2.id+1 = s3.id
where s1.people >= 100 and s2.people >= 100 and s3.people >= 100
) as t
join stadium as s on t.s1_id = s.id or t.s2_id = s.id or t.s3_id = s.id

```

## Author
EINDEX