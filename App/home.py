import streamlit as st

def home_page():
 
    st.title("Welcome to the Agricultural Crop Prediction App")
    st.header("Predicting Crop Yield and More")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("C:\\Users\\user\\OneDrive\\Desktop\\photos\\images.jpeg", use_column_width=True)
    
    with col2:
        st.image("C:\\Users\\user\\OneDrive\\Desktop\\photos\\images (3).jpeg", use_column_width=True)
    
    with col3:
        st.image("C:\\Users\\user\\OneDrive\\Desktop\\photos\\hqdefault.jpg", use_column_width=True)
    
    
    st.write("""
    This app is designed to help farmers, agricultural experts, and researchers predict crop yield 
    based on a variety of factors such as soil fertility, weather conditions, and pollution levels.
    
    **Features**:
    - Predict annual crop yield.
    - Analyze environmental factors that impact crops.
    - View detailed insights and reports.
    
    Start exploring by navigating through the app's features using the sidebar!
    """)

    st.subheader("About the Project")
    st.write("""
    The **Agricultural Crop Prediction App** is a data-driven tool designed to assist farmers, agricultural experts, 
    and researchers in making informed decisions about crop yield. 
    By analyzing factors such as soil fertility, weather patterns, pollution levels, and crop types, 
    this app provides accurate predictions and insights into potential crop outcomes.

    The app uses machine learning models and statistical methods to process historical data and generate predictions.
    It supports various agricultural datasets and allows users to customize their inputs to better reflect real-world conditions.
    """)

    st.subheader("How It Works")
    st.write("""
    - **Data Input**:  Users provide key agricultural data, such as soil quality, 
    rainfall, temperature, and crop type.
             
    - **Data Analysis**: The app analyzes this input data to identify patterns and factors that influence crop yield.
    - **Prediction**: Using trained machine learning models, the app predicts the annual crop yield or other important metrics.
    - **Insights**: After the prediction, the app generates a report summarizing the key influencing factors and the expected outcomes.
    - **Visualization**: Users can visualize trends and patterns in the data through graphs and charts.
    
    To get started, navigate through the features on the sidebar. Input your data, and let the app do the rest!
    """)

    st.write("---")
    st.write("""Thank you for using the **Agricultural Crop Prediction App**!
              We hope this tool helps you achieve better insights and optimize your crop production.""")


