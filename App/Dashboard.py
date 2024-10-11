# def dashboard_page():
#     # Function code here
#     pass

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sqlalchemy import create_engine,text

engine = create_engine('sqlite:///Maji_Ndogo_farm_survey_small.db')

with engine.connect() as connection:
    result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    for row in result:
        print(row)

slq_query = """
            SELECT *
            FROM farm_management_features
            JOIN geographic_features
            ON farm_management_features.field_id = geographic_features.field_id
            JOIN soil_and_crop_features
            ON geographic_features.field_id = soil_and_crop_features.field_id
            JOIN weather_features
            ON soil_and_crop_features.field_id = weather_features.field_id
            """

df=pd.read_sql(slq_query,engine)
df = df.drop(columns=["Field_ID"])
df.rename({"Crop_type":"Annual yield"},axis=1,inplace=True)
df.rename({"Annual_yield":"Crop_type"},axis=1,inplace=True)
df.rename({"Annual yield":"Annual_yield"},axis=1,inplace=True)
df["Crop_type"]=df["Crop_type"].str.replace(" ","")
df["Crop_type"]=df["Crop_type"].replace({'caassaval':"cassava", 'teaa':'tea','wheatn':'wheat','cassaval':'cassava'})
df["Elevation"]=df["Elevation"].abs()




def dashboard_page():
    st.title("Crop Yield Dashboard")


    st.header("Summary Statistics")
    st.write(df.describe())

    st.header("Crop Yield Distribution")
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Annual_yield'], bins=30, kde=True)
    plt.title('Distribution of Crop Yield')
    plt.xlabel('Annual Yield')
    plt.ylabel('Frequency')
    st.pyplot(plt)


    st.header("Correlation Heatmap")
    plt.figure(figsize=(12, 8))
    numeric_df = df.select_dtypes(include=[np.number])
    correlation = numeric_df.corr()
    sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm')
    st.write(correlation)

    with st.sidebar:
        st.header("Filter Options")

    st.header("Average Yield by Crop Type")
    avg_yield = df.groupby('Crop_type')['Annual_yield'].mean().reset_index()
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Crop_type', y='Annual_yield', data=avg_yield)
    plt.title('Average Crop Yield by Crop Type')
    plt.xlabel('Crop Type')
    plt.ylabel('Average Yield')
    st.pyplot(plt)

    # Filter options
    st.header("Filter Data")
    crop_type_filter = st.selectbox("Select Crop Type", options=df['Crop_type'].unique())
    filtered_data = df[df['Crop_type'] == crop_type_filter]

    st.write(f"Showing data for {crop_type_filter} Crop:")
    st.dataframe(filtered_data)

