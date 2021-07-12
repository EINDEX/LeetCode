
Select
Request_at as Day,
ROUND(1-(SUM(case 
when Status = 'completed' then 1
else 0
end) / Count(ID)),2) as 'Cancellation Rate'
from Trips as trips
left join Users as client on client.users_id = trips.client_id
left join Users as driver on driver.users_id = trips.driver_id
where client.Banned = 'No'
and driver.Banned = 'No'
and Request_at >= "2013-10-01"
and Request_at <= "2013-10-03"
group by Request_at

# select 
# SUM(case 
# when Status = 'completed' then 1
# else 0
# end) , Count(ID),Request_at
# from trips
# left join Users as client on client.users_id = trips.client_id
# left join Users as driver on driver.users_id = trips.driver_id
# where client.Banned = 'No'
# and driver.Banned = 'No'
# group by Request_at