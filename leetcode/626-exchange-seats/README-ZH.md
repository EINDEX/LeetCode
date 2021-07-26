# Exchange Seats

## Difficulty
Medium

## Question
<p>Mary is a teacher in a middle school and she has a table <code>seat</code> storing students&#39; names and their corresponding seat ids.</p>

<p>The column <b>id</b> is continuous increment.</p>

<p>Mary wants to change seats for the adjacent students.</p>

<p>Can you write a SQL query to output the result for Mary?</p>

<p>&nbsp;</p>

<pre>
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
</pre>

<p>For the sample input, the output is:</p>

<pre>
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
</pre>

<p><b>Note:</b></p>

<p>If the number of students is odd, there is no need to change the last one&#39;s seat.</p>


## Solution
### mysql
```mysql
# Write your MySQL query statement below
SELECT (
    CASE 
        WHEN MOD(id, 2) = 1 AND id = (SELECT COUNT(1) FROM seat) THEN id
        WHEN MOD(id, 2) = 1 THEN id+1
        ELSE id -1
    END 
) AS id, student
FROM seat
ORDER BY id;
```

## Author
EINDEX