import pandas as pd
import numpy as np

# Function to load the distance matrix from a CSV file
def calculate_distance_matrix(csv_file):
    return pd.read_csv(csv_file, index_col=0)

# Unroll the distance matrix into a DataFrame
def unroll_distance_matrix(distance_matrix):
    unrolled_data = []
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end:
                distance = distance_matrix.at[id_start, id_end]
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})
    return pd.DataFrame(unrolled_data)

# Calculate toll rate for different vehicles
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

# Example usage
distance_matrix = calculate_distance_matrix('dataset-2.csv')  # Ensure the CSV exists
unrolled_df = unroll_distance_matrix(distance_matrix)
toll_rate_df = calculate_toll_rate(unrolled_df)

print(toll_rate_df)
