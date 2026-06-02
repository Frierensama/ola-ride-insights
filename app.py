import streamlit as st
import pandas as pd
from scripts.db_config import get_connection
from scripts.queries_and_insights import sql_queries, insights

st.set_page_config(page_title="OLA Ride Analysis dashboard",layout="wide")

st.title("OLA Rides Analysis Report")
st.write("Interactive analysis of OLA Rides data using sql.")

selected_query = st.selectbox("Select Analysis",list(sql_queries.keys()))

try:
    conn = get_connection()
    cursor = conn.cursor()

    df = pd.read_sql(sql_queries[selected_query],conn)

    st.subheader(selected_query)
    st.dataframe(df, use_container_width=True)
    st.metric("Records Returned", len(df))

    st.info(insights[selected_query])

except Exception as e:
    st.error(f"Error:{e}")

finally:
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()