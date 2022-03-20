import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets

def app():
    st.title('Data')

    st.write("This is the `Data` page of the multi-page app.")
    
    form = st.form(key="annotation")
    with form:
        cols = st.columns((1, 1))
        author = cols[0].text_input("Report author:")
        bug_type = cols[1].selectbox(
            "Bug type:", ["Front-end", "Back-end", "Data related", "404"], index=2
        )
        comment = st.text_area("Comment:")
        cols = st.columns(2)
        date = cols[0].date_input("Bug date occurrence:")
        bug_severity = cols[1].slider("Bug severity:", 1, 5, 2)
        submitted = st.form_submit_button(label="Submit")