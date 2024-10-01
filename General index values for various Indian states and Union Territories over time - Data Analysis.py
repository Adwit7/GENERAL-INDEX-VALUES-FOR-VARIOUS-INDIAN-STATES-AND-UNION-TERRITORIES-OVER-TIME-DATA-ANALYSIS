# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:09:38 2024

@author: adwit
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


df = pd.read_csv ("C:/Users/adwit/OneDrive/Documents/Python Scripts/archive/Statewise_General_Index_Upto_Feb24.csv")

# Data Cleaning: Filling missing values with the mean of respective columns for analysis
df_cleaned = df.fillna(df.mean(numeric_only=True))

# Q1: Overall trend in index values across all states over time
def plot_trend_over_time(df):
    df_grouped = df_cleaned.groupby(['Year', 'Name']).mean(numeric_only=True)
    df_grouped.plot(figsize=(10, 6))
    plt.title('Overall Trend of Index Values Over Time')
    plt.xlabel('Time (Year, Month)')
    plt.ylabel('Average Index Value')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Q2: State with the highest average index value
def state_with_highest_avg(df):
    state_means = df_cleaned.iloc[:, 3:].mean()
    highest_state = state_means.idxmax()
    highest_value = state_means.max()
    return highest_state, highest_value

# Q3: Comparing rural, urban, and combined sector index values for a state (e.g., Andhra Pradesh)
def compare_sectoral_values(df, state):
    state_data = df_cleaned[['Sector', 'Year', 'Name', state]].groupby(['Sector', 'Year']).mean(numeric_only=True).unstack('Sector')
    state_data.plot(figsize=(10, 6), title=f'Sectoral Comparison for {state}')
    plt.ylabel('Index Value')
    plt.xlabel('Year')
    plt.tight_layout()
    plt.show()

# Q4: States with the most volatility in index values (highest standard deviation)
def most_volatile_states(df):
    state_stds = df_cleaned.iloc[:, 3:].std()
    most_volatile = state_stds.idxmax()
    volatility_value = state_stds.max()
    return most_volatile, volatility_value

# Q5: Differences in index values between northern and southern states (geographical classification)
def compare_regions(df, northern_states, southern_states):
    north_data = df_cleaned[northern_states].mean().mean()
    south_data = df_cleaned[southern_states].mean().mean()
    return north_data, south_data

# Q6: Performance of Union Territories vs. states
def compare_uts_vs_states(df, uts, states):
    uts_data = df_cleaned[uts].mean().mean()
    states_data = df_cleaned[states].mean().mean()
    return uts_data, states_data

# Q7: Monthly variations in index values for a specific year for key states (e.g., Delhi or Maharashtra)
def monthly_variations(df, year, states):
    monthly_data = df_cleaned[(df_cleaned['Year'] == year)][['Name'] + states].groupby('Name').mean()
    monthly_data.plot(figsize=(10, 6), title=f'Monthly Variations in {year}')
    plt.ylabel('Index Value')
    plt.xlabel('Month')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Q1: Plot the overall trend
plot_trend_over_time(df_cleaned)

# Q2: Get state with the highest average index
highest_state, highest_value = state_with_highest_avg(df_cleaned)
print(f"State with Highest Average Index Value: {highest_state}, Value: {highest_value}")

# Q3: Compare sectoral index values for Andhra Pradesh
compare_sectoral_values(df_cleaned, 'Andhra Pradesh')

# Q4: Get the most volatile state
most_volatile, volatility_value = most_volatile_states(df_cleaned)
print(f"Most Volatile State: {most_volatile}, Volatility Value: {volatility_value}")

# Q5: Compare northern and southern states
northern_states = ['Delhi', 'Haryana', 'Punjab', 'Uttar Pradesh', 'Uttarakhand', 'Jammu and Kashmir']
southern_states = ['Andhra Pradesh', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Telangana']
north_avg, south_avg = compare_regions(df_cleaned, northern_states, southern_states)
print(f"Northern States Average Index: {north_avg}, Southern States Average Index: {south_avg}")

# Q6: Compare Union Territories and states
uts = ['Chandigarh', 'Andaman and Nicobar', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Lakshadweep', 'Puducherry']
states = df_cleaned.columns[3:].difference(uts)
uts_avg, states_avg = compare_uts_vs_states(df_cleaned, uts, states)
print(f"Union Territories Average Index: {uts_avg}, States Average Index: {states_avg}")

# Q7: Plot monthly variations for Delhi and Maharashtra in 2011
monthly_variations(df_cleaned, 2011, ['Delhi', 'Maharashtra'])












































