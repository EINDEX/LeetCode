# Classes More Than 5 Students

## Difficulty
Easy

## Question
<p>There is a table <code>courses</code> with columns: <b>student</b> and <b>class</b></p>

<p>Please list out all classes which have more than or equal to 5 students.</p>

<p>For example, the table:</p>

<pre>
+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
</pre>

<p>Should output:</p>

<pre>
+---------+
| class   |
+---------+
| Math    |
+---------+
</pre>

<p>&nbsp;</p>

<p><b>Note:</b><br />
The students should not be counted duplicate in each course.</p>



## Solution
### mysql
```mysql
# Write your MySQL query statement below

select class from (select count(distinct(student)) as t, class from courses group by class order by t desc) as a where a.t >=5;

```