# Write your MySQL query statement below
delete p1 from person as p1, 
    person as p2 
where p2.Email = p1.Email and p2.Id < p1.Id
