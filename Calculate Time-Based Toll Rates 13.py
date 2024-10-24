import pandas as pd
import numpy as np
from datetime import time

# Sample distance matrix for demonstration
data = {
    'A': [0, 10, 15],
    'B': [10, 0, 25],
    'C': [15, 25, 0]
}
distance_matrix = pd.DataFrame(data, index=['A', 'B', 'C'])

def unroll_distance_matrix(distance_matrix):
    unrolled_data = []
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end:
                distance = distance_matrix.at[id_start, id_end]
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})
    return pd.DataFrame(unrolled_data)

def calculate_toll_rate(unrolled_df):
    toll_rates = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    for vehicle, rate in toll_rates.items():
        unrolled_df[vehicle] = unrolled_df['distance'] * rate

    return unrolled_df

# Calculate toll rates
unrolled_df = unroll_distance_matrix(distance_matrix)
toll_rate_df = calculate_toll_rate(unrolled_df)

# Define time-based toll rates function
def calculate_time_based_toll_rates(toll_rate_df):
    time_ranges = {
        'weekday': [
            (time(0, 0, 0), time(10, 0, 0), 0.8),
            (time(10, 0, 0), time(18, 0, 0), 1.2),
            (time(18, 0, 0), time(23, 59, 59), 0.8)
        ],
        'weekend': [(time(0, 0, 0), time(23, 59, 59), 0.7)]
    }

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    new_rows = []

    for index, row in toll_rate_df.iterrows():
        id_start = row['id_start']
        id_end = row['id_end']
        distance = row['distance']
        
        # Handle weekdays
        for day in days_of_week[:5]:  # Weekdays (Monday to Friday)
            for start_time, end_time, discount in time_ranges['weekday']:
                new_row = {
                    'id_start': id_start,
                    'id_end': id_end,
                    'distance': distance,
                    'moto': row['moto'] * discount,
                    'car': row['car'] * discount,
                    'rv': row['rv'] * discount,
                    'bus': row['bus'] * discount,
                    'truck': row['truck'] * discount,
                    'start_day': day,
                    'start_time': start_time,
                    'end_day': day,
                    'end_time': end_time
                }
                new_rows.append(new_row)

        # Handle weekends
        for day in days_of_week[5:]:  # Weekends (Saturday and Sunday)
            start_time = time(0, 0, 0)
            end_time = time(23, 59, 59)
            discount = time_ranges['weekend'][0][2]
            new_row = {
                'id_start': id_start,
                'id_end': id_end,
                'distance': distance,
                'moto': row['moto'] * discount,
                'car': row['car'] * discount,
                'rv': row['rv'] * discount,
                'bus': row['bus'] * discount,
                'truck': row['truck'] * discount,
                'start_day': day,
                'start_time': start_time,
                'end_day': day,
                'end_time': end_time
            }
            new_rows.append(new_row)

    time_based_toll_rate_df = pd.DataFrame(new_rows)
    return time_based_toll_rate_df

# Calculate time-based toll rates
time_based_toll_rate_df = calculate_time_based_toll_rates(toll_rate_df)
print(time_based_toll_rate_df)
