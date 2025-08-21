# VAYU AQI PREDICTION
# AQI Prediction Model for Indian Cities
Machine learning model that predicts Air Quality Index (AQI) values for various cities in India using historical data. The dataset is sourced from Kaggle, and this project aims to process, analyze, and predict AQI values across different Indian cities.

## Table of Contents
- Introduction
- Dataset
- Model Workflow
- Results
- Libraries Used

## Introduction
Air pollution has become a significant concern in India, with cities often recording AQI levels far exceeding safe limits. This project builds a data-driven approach to predict AQI values for Indian cities, leveraging historical air quality data. The results can help raise awareness and guide further research on environmental health concerns in the region.

## Dataset
The dataset used in this project is from Kaggle's [Air Quality Data in India]<https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india>. The dataset includes AQI measurements, city names, dates, and AQI bucket categories.

Key features used in the model:

- City: The name of the city
- Date: The date of the AQI recording
- AQI: The recorded AQI value
- AQI_Bucket: The category of AQI, e.g., Good, Moderate, Poor, etc.

## Model Workflow
The process follows these steps:
* Data Loading: Loaded and parsed the dataset using Pandas.

* Data Preprocessing:
Parsed the date column to convert it into a datetime format.
Filtered and selected only the relevant columns: City, Date, AQI, and AQI_Bucket.
Handled any missing data and cleaned up the dataset.

* City-wise AQI Data Creation:
For each city in the dataset, created separate columns for AQI values and AQI bucket categories.

*Boxplots of AQI values of the various cities*
![image](https://github.com/user-attachments/assets/c318345e-c97c-45ec-907f-1ed433b94234)

* DataFrame Initialization:
Initialized a time-based DataFrame, with the date range from January 1, 2015, to May 2, 2020. For each city, populated the corresponding AQI values into the columns.

* Handling Missing Values:
If the AQI data exceeded the available rows, we expanded the DataFrame to accommodate the additional data.

* Final DataFrame:
Created a comprehensive DataFrame that included city-wise AQI values over the entire time period.

*Plotting predicted vs actual AQI values graph*
![image](https://github.com/user-attachments/assets/cb28762c-f288-4c94-b92f-373f3d515b3c)

## RESULTS
![image](https://github.com/user-attachments/assets/ec969ede-aceb-4795-bfe4-df4ffcf75d83)


## Libraries Used
- *numpy* for numerical operations
- *pandas* for data manipulation
- *matplotlib* for visualization
- *seaborn* for enhanced data visualizations
- *datetime* for date manipulation

## Research paper
https://www.aqmd.gov/home/research/publications/50-years-of-progress
