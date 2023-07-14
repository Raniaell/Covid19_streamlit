import streamlit as st
from joblib import load
st.set_page_config( page_title="Pandemic Era in UK",
                   page_icon="🚨")
st.title("Pandemic Covid 19 data in the United Kingdom UK")
st.sidebar.success("Select a page above")
st.header("Let's start Predicting")
lg = load('covid19.joblib')
x = st.number_input("The number of cases confirmed is:")
st.write("The chosen number is 👉:", x)
lg.coef_=load("y.joblib")
lg.intercept_=load("y2.joblib")
y = lambda x : lg.coef_[3]*x**3 + lg.coef_[2]*x**2 +lg.coef_[1]*x + lg.coef_[0] * lg.intercept_
if (st.button("💀 Deaths predictor 💀")):
    st.write("Unfortunately, the number of deaths is as follow 🙁:")
    st.write(round(y(x)))
    