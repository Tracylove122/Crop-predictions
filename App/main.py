import streamlit as st          
from streamlit_option_menu import option_menu  
from home import home_page 
from prediction import pred_page
from Dashboard import dashboard_page


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="PredictPrice"
)

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Prediction", "Dashboard"],
        icons=["house", "pair of dice", "line graph"], 
        menu_icon="cast",
    )
    

if selected == "Home":
   home_page()

elif selected == "Prediction":
    pred_page()

else:
    dashboard_page()