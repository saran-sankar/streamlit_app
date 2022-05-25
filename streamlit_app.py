import streamlit as st
import pandas as pd

st.title('Streamlit App')
st.text('Text')

fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_list = fruit_list.set_index('Fruit')

streamlist.multiselect('Pick fruits: ', list(fruit_list.names))
st.dataframe(fruit_list)
