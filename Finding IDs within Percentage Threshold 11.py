import pandas as pd
import numpy as np

def calculate_distance_matrix(file_path):
    df = pd.read_csv(file_path)
    unique_ids = pd.concat([df['id_start'], df['id_end']]).unique()  # Use pd.concat instead of append
    distance_matrix = pd.DataFrame(np.inf, index=unique_ids, columns=unique_ids)
    
    for _, row in df.iterrows():
        distance_matrix.at[row['id_start'], row['id_end']] = row['distance']
        distance_matrix.at[row['id_end'], row['id_start']] = row['distance']

    np.fill_diagonal(distance_matrix.values, 0)
    
    return distance_matrix

def unroll_distance_matrix(distance_matrix):
    unrolled_data = []
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end:
                distance = distance_matrix.at[id_start, id_end]
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})
    return pd.DataFrame(unrolled_data)

def find_ids_within_ten_percentage_threshold(unrolled_df, reference_id):
    distances = unrolled_df[unrolled_df['id_start'] == reference_id]['distance']
    
    if distances.empty:
        return []
    average_distance = distances.mean()
    
    lower_bound = average_distance * 0.9
    upper_bound = average_distance * 1.1
    
    result_ids = unrolled_df[(unrolled_df['id_start'] != reference_id) & 
                              (unrolled_df['distance'] >= lower_bound) & 
                              (unrolled_df['distance'] <= upper_bound)]
    
    return sorted(result_ids['id_start'].unique())

# Example usage
distance_matrix = calculate_distance_matrix('dataset-2.csv')
unrolled_df = unroll_distance_matrix(distance_matrix)
reference_id = 1001400  # Example reference ID
result_ids = find_ids_within_ten_percentage_threshold(unrolled_df, reference_id)
print(result_ids)