import streamlit as st
import pandas as pd
from scripts.db_config import get_connection
from scripts.queries_and_insights import sql_queries, insights

st.set_page_config( page_title="OLA Ride Analysis Dashboard",page_icon="🚕",layout="wide")

st.title("🚕 OLA Ride Analysis Dashboard")
st.write("Interactive analysis of OLA rides data using MySQL, and Streamlit.")

selected_query = st.sidebar.selectbox("Select Analysis",list(sql_queries.keys()))

try:
    conn = get_connection()

    df = pd.read_sql(sql_queries[selected_query],conn)
    st.subheader(selected_query)

    with st.expander("View SQL Query"):
        st.code(sql_queries[selected_query],language="sql")

    search_term = st.text_input("Search in results")

    if search_term:
        df = df[
            df.astype(str).apply(
                lambda x: x.str.contains(
                    search_term,
                    case=False,
                    na=False
                )
            )
            .any(axis=1)
        ]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Records Returned",len(df))
    with col2:
        st.metric("Columns",len(df.columns))
    with col3:
        st.metric("Null Values",int(df.isnull().sum().sum()))

    st.divider()

    st.dataframe(df,use_container_width=True,height=500)

    csv = df.to_csv(index=False)

    # st.download_button(
    #     label="Download Results",
    #     data=csv,
    #     file_name="ola_query_results.csv",
    #     mime="text/csv"
    # )

    st.divider()

    st.subheader("Business Insight")
    st.info(insights[selected_query])

except Exception as e:
    st.error(f"Error: {e}")

finally:
    if "conn" in locals():
        conn.close()