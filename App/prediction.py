import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sqlalchemy import create_engine, text


with open('App/encoded_soil_type_crop_type_location.pkl', "rb") as f:
    encoder = pickle.load(f)


with open('App/scaler.pkl', "rb") as f:
    scaler = pickle.load(f)

with open('App/best_model_random_forest.pkl', "rb") as f:
    model = pickle.load(f) 


def pred_page():
    df = pd.read_csv('App/Actual_df.csv')

    with st.expander("My DataFrame"):
      st.dataframe(df.head())


    columns = df.columns.tolist()
    st.write(columns)

    with st.sidebar:
        
        Pollution_level = st.slider('Pollution Level', min_value=0.0, max_value=100.0, value=50.0)
        Plot_size = st.slider('Plot Size', min_value=0.0, max_value=100.0, value=10.0)
        Annual_yield = st.slider('Annual Yield (in tons)', min_value=0, max_value=100, value=5)
        Crop_type = st.selectbox("Crop Type", options=df['Crop_type'].unique())
        Standard_yield = st.slider('Standard Yield', min_value=df['Standard_yield'].min(), max_value=df['Standard_yield'].max(), value=df['Standard_yield'].min())
        Elevation = st.slider('Elevation', min_value=df['Elevation'].min(), max_value=df['Elevation'].max(), value=df['Elevation'].min())
        Latitude = st.slider('Latitude', min_value=df['Latitude'].min(), max_value=df['Latitude'].max(), value=df['Latitude'].min())
        Longitude = st.slider('Longitude', min_value=df['Longitude'].min(), max_value=df['Longitude'].max(), value=df['Longitude'].min())
        Location = st.selectbox('Location', options=df['Location'].unique())
        Slope = st.slider('Slope', min_value=df['Slope'].min(), max_value=df['Slope'].max(), value=df['Slope'].min())
        Soil_fertility = st.selectbox("Soil Fertility", options=df['Soil_fertility'].unique())
        Soil_type = st.selectbox("Soil Type", options=df['Soil_type'].unique())
        pH = st.slider('pH', min_value=df['pH'].min(), max_value=df['pH'].max(), value=df['pH'].min())
        Rainfall = st.slider('Rainfall (in mm)', min_value=0, max_value=2000, value=500)
        Min_temperature_C = st.slider('Minimum Temperature (°C)', min_value=-10, max_value=50, value=15)
        Max_temperature_C = st.slider('Maximum Temperature (°C)', min_value=-10, max_value=50, value=30)
        Ave_temps = st.slider('Ave_temps', min_value=df['Ave_temps'].min(), max_value=df['Ave_temps'].max(), value=df['Ave_temps'].min())
        



    input_data = pd.DataFrame({
        columns[0] : [Pollution_level],
        columns[1]: [Plot_size],
        columns[2]: [Annual_yield],
        columns[3]: [Crop_type],
        columns[4]: [Standard_yield],
        columns[5]: [Elevation],
        columns[6]: [Latitude],
        columns[7]: [Longitude],
        columns[8]: [Location],
        columns[9]: [Slope],
        columns[10]: [Soil_fertility],
        columns[11]:[Soil_type],
        columns[12]: [pH],
        columns[13]: [Rainfall],
        columns[14]: [Min_temperature_C],
        columns[15]: [Max_temperature_C],
        columns[16]: [Ave_temps],

    })

    input_data['growing_conditions'] = (input_data['Rainfall'] +  input_data['Soil_fertility'])

    input_data["yield_efficiency"] = (input_data["Annual_yield"] / input_data["Standard_yield"])
    input_data["Soil_nature"]=(input_data["Soil_fertility"] * input_data["pH"])


    input_data.drop(columns=['Annual_yield'], inplace=True)
    st.dataframe(input_data)


    encoded_value = encoder.transform(input_data[['Soil_type', 'Crop_type', 'Location']]).toarray()
    df_cat = pd.DataFrame(encoded_value, columns=encoder.get_feature_names_out(['Soil_type', 'Crop_type', 'Location']))
    
    input_df = pd.concat([input_data.reset_index(drop=True), df_cat.reset_index(drop=True)], axis=1)
    input_df.drop(columns=['Soil_type', 'Crop_type', 'Location'], inplace=True)

    with st.expander("User Input After Encoding"):
       st.dataframe(input_df)

    with st.expander('Scaled DataFrame'):
        scaled_input = scaler.transform(input_df)
        scaled_df = pd.DataFrame(scaled_input, columns=input_df.columns)

        st.dataframe(scaled_df)
        st.title("Now Let's Help You Predict")

    prediction = model.predict(scaled_df)

    def load_prediction(predictions):
        return f"<h3 style='color:green;'>The prediction based on your input is: {predictions[0]}</h3>"

    st.markdown(load_prediction(prediction), unsafe_allow_html=True)


