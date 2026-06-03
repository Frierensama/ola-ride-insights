use ola;
show tables;
select count(customer_id) from ola_t group by booking_id;
desc ola_t;

-- query 01
select * from ola_t
where Booking_Status = 'Success';

-- query 02
select Vehicle_Type, round(avg(Ride_Distance),2) as Average_Ride_Distance
from ola_t
group by Vehicle_Type;

-- query 03
select count(*) as 'Customer_Canceled_Rides_Count'
from ola_t
where Booking_Status='Canceled by Customer';

-- query 04
select Customer_ID, count(*) as 'Total_Rides'
from ola_t
group by Customer_ID
order by count(*) desc
limit 5;

-- query 05
select count(*) as 'Canceled_Rides_by_Driver'
from ola_t
where Canceled_Rides_by_Driver = 'Personal & Car related issue';

-- query 06
select Vehicle_Type, max(Driver_Ratings) as Max_Driver_Rating, min(Driver_Ratings) as Min_Driver_Rating
from ola_t
group by Vehicle_Type
having Vehicle_Type = 'Prime Sedan';

-- query 07
select * from ola_t
where Payment_Method = 'UPI';

-- query 08
select Vehicle_Type, round(avg(Customer_Rating),2) as Avg_Customer_Rating
from ola_t
group by Vehicle_Type
order by Avg_Customer_Rating desc;

-- query 09
select sum(Booking_Value) as Total_Booking_Value
from ola_t
where Incomplete_Rides = 'No';

-- query 10
select Booking_ID, Customer_ID, Vehicle_Type, Pickup_Location, Drop_Location, Incomplete_Rides, Incomplete_Rides_Reason
FROM ola_t
WHERE Incomplete_Rides = 'Yes';