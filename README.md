# ECE143-Project: Prediction and Estimation Model for Taxi drivers in Airport Area
Group 6 Members: Nghi Tran Lu, Ya Chen Tsai, Ziyi Zhong, Mingyang Lyu, Hong Tang
# Project Description: 
The purpose of this project is to help out taxi’ drivers to decide whether they should stay at the airport waiting for the passengers or go back Downtown to make money in city based on the projected wait time and the cost of a fuel consumption. 

Firstly, we build a prediction model that will predict taxi wait time. We process our data and select time slot of taxi arriving at parking lot, number of taxies waiting at this time slot, and arrival flights during the period as our features, and select wait time as our labels. We train and select the best model fits our goal. 

Secondly, we build a mathematical estimation model for taxi drivers based our predictive model and help them decide whether they should leave or wait.

# Modules used: All the modules we used for our specific project.
a. Data Processing&Visualization:
   Pandas,
   numpy,
   matplotlib.pyplot

b. Calculations & Mathematical Modeling:
   collections,
   math: radians, sin, cos, asin, sqrt, 
   warnings,
   statistics: stdev,mean

c. Predictive Models:
   sklearn:ensemble, model_selection.train_test_split, linear_model, ExtraTreeRegressor, DecisionTreeRegressor, LinearRegression, svm
   
# Dataset: 
a. There are total of 24 folders and 24*60 files. The 24 folders contains all the taxi data in that specific hour, and the each file in that folder contains all the taxi data in that specific minute(hour:min). Each file contains all the operating information of every Taxi in Shanghai Area at that specific time(hour:min:sec), 

b. Flight.csv, which contains the schedules of all arrival planes on April 1st 2018.
# File Overview: 
