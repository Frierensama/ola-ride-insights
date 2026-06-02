import streamlit as st
from scripts.queries_and_insights import sql_queries,insights
from scripts.db_config import get_connection
import pandas as pd

st.set_page_config(page_title="Dashboard",layout='wide')
st.title("Dashbaord")
st.write("interactive anlaysis")

selected_query = st.sidebar.selectbox('select analysis',list(sql_queries.keys()))

try:
    conn = get_connection()

    df = pd.read_sql(sql_queries[selected_query], conn)

    st.subheader(selected_query)

    with st.expander('view code'):
        st.code(sql_queries[selected_query],language='sql')

    search_text = st.text_input("search in it")

    if search_text:
        df = df[df.astype(str).apply(lambda x : x.str.contains(search_text,case=False,na=False).any(axis=1))]

    col1, col2, col3= st.columns(3)

    with col1:
        st.metric('records', len(df))
    with col2:
        st.metric("cols",len(df.columns))
    with col3:
        st.metric('null count', int(df.isnull().sum().sum()))
    
    st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False)

    

    st.info(insights[selected_query])

except Exception as e:
    st.error(f"Error:{e}")
finally:
    if 'conn' in locals():
        conn.close()