sql_queries = {

    "Retrieve all successful bookings":
    """
    SELECT *
    FROM ola_t
    WHERE Booking_Status = 'Success';
    """,

    "Find the average ride distance for each vehicle type":
    """
    SELECT Vehicle_Type,
           ROUND(AVG(Ride_Distance),2) AS Average_Ride_Distance
    FROM ola_t
    GROUP BY Vehicle_Type;
    """,

    "Get the total number of cancelled rides by customers":
    """
    SELECT COUNT(*) AS Customer_Canceled_Rides_Count
    FROM ola_t
    WHERE Booking_Status = 'Canceled by Customer';
    """,

    "List the top 5 customers who booked the highest number of rides":
    """
    SELECT Customer_ID,
           COUNT(*) AS Total_Rides
    FROM ola_t
    GROUP BY Customer_ID
    ORDER BY Total_Rides DESC
    LIMIT 5;
    """,

    "Get the number of rides cancelled by drivers due to personal and car-related issues":
    """
    SELECT COUNT(*) AS Driver_Cancellation_Count
    FROM ola_t
    WHERE Canceled_Rides_by_Driver = 'Personal & Car related issue';
    """,

    "Find the maximum and minimum driver ratings for Prime Sedan bookings":
    """
    SELECT Vehicle_Type,
           MAX(Driver_Ratings) AS Max_Driver_Rating,
           MIN(Driver_Ratings) AS Min_Driver_Rating
    FROM ola_t
    WHERE Vehicle_Type = 'Prime Sedan'
    GROUP BY Vehicle_Type;
    """,

    "Retrieve all rides where payment was made using UPI":
    """
    SELECT *
    FROM ola_t
    WHERE Payment_Method = 'UPI';
    """,

    "Find the average customer rating per vehicle type":
    """
    SELECT Vehicle_Type,
           ROUND(AVG(Customer_Rating),2) AS Avg_Customer_Rating
    FROM ola_t
    GROUP BY Vehicle_Type
    ORDER BY Avg_Customer_Rating DESC;
    """,

    "Calculate the total booking value of rides completed successfully":
    """
    SELECT SUM(Booking_Value) AS Total_Booking_Value
    FROM ola_t
    WHERE Incomplete_Rides = 'No';
    """,

    "List all incomplete rides along with the reason":
    """
    SELECT Booking_ID,
           Customer_ID,
           Vehicle_Type,
           Pickup_Location,
           Drop_Location,
           Incomplete_Rides,
           Incomplete_Rides_Reason
    FROM ola_t
    WHERE Incomplete_Rides = 'Yes';
    """
}

insights = {

    "Retrieve all successful bookings":
    "Shows all successfully completed rides along with revenue, ratings, and ride-performance analysis.",

    "Find the average ride distance for each vehicle type":
    "Bikes have highest average ride distance probably because its costs less and mobility.",

    "Get the total number of cancelled rides by customers":
    "Measures customer cancellation frequency.",

    "List the top 5 customers who booked the highest number of rides":
    "Identifies customers who frequently use rides, helps to understand customer category and improvise the ride positions.",

    "Get the number of rides cancelled by drivers due to personal and car-related issues":
    "Helps to identify the inefeciency of Drivers and can adjust thier pay.",

    "Find the maximum and minimum driver ratings for Prime Sedan bookings":
    "Evaluates service quality consistency among Prime Sedan drivers.",

    "Retrieve all rides where payment was made using UPI":
    "Analyzes UPI adoption and provides insights into customer payment preferences.",

    "Find the average customer rating per vehicle type":
    "Compares customer satisfaction across vehicle categories and helps identify the most preferred ride type   .",

    "Calculate the total booking value of rides completed successfully":
    "Measures revenue generated from successful bookings.",

    "List all incomplete rides along with the reason":
    "Helps identify ride failures and work on the set-backs."
}