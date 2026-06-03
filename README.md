# OLA Ride Insights

This project analyzes OLA ride booking data using **MySQL**, **Power BI**, and **Streamlit**. The goal is to study booking trends, revenue patterns, cancellations, customer behavior, and ride ratings through SQL queries and interactive dashboards.

## Live Demo

https://ola-insights.up.railway.app/

---

## What this project does

- Loads cleaned OLA ride data into MySQL
- Runs SQL queries for business analysis
- Displays query results in a Streamlit dashboard
- Shows insights for each analysis
- Visualizes ride data using Power BI dashboards
- Connects Streamlit to a Railway-hosted MySQL database

---

## Tools Used

- Python
- Pandas
- MySQL
- SQL
- Streamlit
- Power BI
- Railway
- pymysql
- python-dotenv

---

## Dataset

The dataset contains **103,024 ride booking records** with information such as:

- Booking Status
- Customer ID
- Vehicle Type
- Pickup and Drop Locations
- Ride Distance
- Booking Value
- Payment Method
- Driver Ratings
- Customer Ratings
- Cancellation Reasons
- TAT (Turn Around Time)

---

## Project Structure

```bash
OLA_Ride_Insights/
│
├── app.py
├── .env
├── README.md
├── requirements.txt
│
├── data/
│   └── ola_cleaned.csv
│
├── scripts/
│   ├── db_config.py
│   ├── db_table_creation.py
│   ├── db_data_insertion.py
│   └── queries_and_insights.py
│
├── sql/
│   └── ola_queries.sql
│
└── powerbi/
    └── ola_dashboard.pbix
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
MYSQLHOST=your_host
MYSQLPORT=your_port
MYSQLUSER=your_user
MYSQLPASSWORD=your_password
MYSQLDATABASE=your_database
```

Do not commit the `.env` file to GitHub.

---

## How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

If required:

```bash
pip install pandas streamlit pymysql python-dotenv sqlalchemy
```

### 2. Configure Database

Add your Railway MySQL credentials to the `.env` file.

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

---

## SQL Analysis Included

The dashboard includes analysis for:

1. Retrieve all successful bookings
2. Average ride distance by vehicle type
3. Total customer cancellations
4. Top 5 customers by number of rides
5. Driver cancellations due to personal/car issues
6. Maximum and minimum driver ratings for Prime Sedan
7. UPI payment bookings
8. Average customer rating by vehicle type
9. Total booking value of completed rides
10. Incomplete rides and their reasons

---

## Power BI Dashboard

### Overall

- Ride Volume Over Time
- Booking Status Breakdown

### Vehicle Type

- Top 5 Vehicle Types by Ride Distance
- Average Customer Ratings by Vehicle Type

### Revenue

- Revenue by Payment Method
- Top 5 Customers by Total Booking Value
- Ride Distance Distribution Per Day

### Cancellation

- Customer Cancellation Reasons
- Driver Cancellation Reasons

### Ratings

- Customer Rating Distribution
- Driver Rating Distribution
- Customer Rating vs Driver Rating

---

## Key Insights

- Around 62% of rides were completed successfully.
- Driver cancellations were higher than customer cancellations.
- Prime Sedan covered the highest ride distance among vehicle categories.
- Customer ratings remained close to 4.0 across vehicle types.
- Cash and UPI were the most commonly used payment methods.
- Driver-related issues were the leading cause of driver cancellations.

---

## Notes

- Query results are fetched directly from the MySQL database.
- Streamlit is connected to Railway-hosted MySQL.
- Power BI dashboards are built from the cleaned dataset.
- Environment variables are used to keep database credentials secure.

---

## Deployment

**Database:** Railway MySQL

**Application:** Streamlit

**Hosting:** Railway

### Live Application

https://ola-insights.up.railway.app/

---

## License

Bleeh.