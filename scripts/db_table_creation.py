from db_config import get_connection

try:
    conn = get_connection()
    cursor = conn.cursor()

    # to prevent error if table exists. drops table before creating again.
    cursor.execute(""" drop table if exists ola_t """) 

    # table creation query.
    table_create_query = """ 
    create table ola_t (
    Date DATETIME,
    Time TIME,

    Booking_ID VARCHAR(20) PRIMARY KEY,
    Booking_Status VARCHAR(30),

    Customer_ID VARCHAR(15),

    Vehicle_Type VARCHAR(20),

    Pickup_Location VARCHAR(20),
    Drop_Location VARCHAR(20),

    V_TAT FLOAT,
    C_TAT FLOAT,

    Canceled_Rides_by_Customer VARCHAR(100),
    Canceled_Rides_by_Driver VARCHAR(100),

    Incomplete_Rides VARCHAR(20),
    Incomplete_Rides_Reason VARCHAR(100),

    Booking_Value INT,

    Payment_Method VARCHAR(30),

    Ride_Distance INT,

    Driver_Ratings FLOAT,
    Customer_Rating FLOAT,

    TAT_Applicable INT,
    Rated_Ride_Applicable INT
    );
    """
    cursor.execute(query=table_create_query)
    conn.commit() # commit changes to database.

    print("Table Created in database=ola, table=ola_t")

except Exception as e:
    # in-case if an error occures while connecting to database.
    print("Error :",e)

finally:
    # close cursor and connection.
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()