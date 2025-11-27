Urban Taxi Fare Prediction with Machine Learning

Predict taxi fare amounts for urban rides using a trained Decision Tree model with one-hot encoded categorical features — deployed via an interactive Gradio web app.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Data Preprocessing](#data-preprocessing)
4. [Feature Engineering](#feature-engineering)
5. [Model Building](#model-building)
6. [Evaluation](#evaluation)
7. [Conclusion](#conclusion)

🚖 Project Overview

This project builds a machine learning model to predict taxi fare amounts based on key trip features such as passenger count, trip distance, duration, rate code, payment type, time of day, and weekday.

The model leverages:

Decision Tree Regressor trained on historical taxi trip data

One-Hot Encoding for categorical features like time and weekday

A Gradio web interface for interactive user input and instant fare predictions

🎯 Features

Inputs:

Passenger Count

Trip Distance (km)

Trip Duration (minutes)

Rate Code

Payment Type

Time of Day (4AM-8PM or 8PM-4AM)

Trip Date (weekday extracted automatically)

Outputs:

Predicted taxi fare amount (USD)

🚀 Usage

Ensure the following files are present in the project root:

model.pkl (your trained decision tree model)

encoder.pkl (your one-hot encoder)

Run the Gradio app:

python app.py


Open the provided local URL in your browser.

Enter trip details using the interactive form and click Predict to get the fare estimate instantly.

## Feature Engineering

- Time-based features: Extracted features like hour, minute, date, day of the week, month, and year from the pickup date and time.
- Distance calculation: Used the Haversine formula to compute the distance between pickup and dropoff locations based on their longitude and latitude.

🧪 Model Training (Optional)

If you want to retrain or improve the model, you can:

Use taxi trip datasets with the relevant features

Encode categorical variables using one-hot encoding

Train a Decision Tree Regressor or any other regression model

Save the model and encoder using pickle

## Evaluation

The evaluation metrics and results for the taxi fare prediction model will be provided after running different algorithms.

## Conclusion

This project demonstrates a complete pipeline for cleaning, feature engineering, and predicting taxi fares. The final model aims to provide accurate predictions by leveraging various features extracted from the dataset.
