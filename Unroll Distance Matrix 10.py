import pandas as pd
import numpy as np

def calculate_distance_matrix(file_path):
    df = pd.read_csv(file_path)
    unique_ids = pd.unique(df[['id_start', 'id_end']].values.ravel('K'))
    distance_matrix = pd.DataFrame(np.nan, index=unique_ids, columns=unique_ids)

    for _, row in df.iterrows():
        distance_matrix.at[row['id_start'], row['id_end']] = row['distance']
        distance_matrix.at[row['id_end'], row['id_start']] = row['distance']

    np.fill_diagonal(distance_matrix.values, 0)

    for k in unique_ids:
        for i in unique_ids:
            for j in unique_ids:
                if pd.notna(distance_matrix.at[i, k]) and pd.notna(distance_matrix.at[k, j]):
                    new_distance = distance_matrix.at[i, k] + distance_matrix.at[k, j]
                    if pd.isna(distance_matrix.at[i, j]) or new_distance < distance_matrix.at[i, j]:
                        distance_matrix.at[i, j] = new_distance

    return distance_matrix

def unroll_distance_matrix(distance_matrix):
    unrolled_data = []

    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end: 
                distance = distance_matrix.at[id_start, id_end]
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    return pd.DataFrame(unrolled_data)


file_path = 'dataset-2.csv'
distance_matrix = calculate_distance_matrix(file_path)
unrolled_df = unroll_distance_matrix(distance_matrix)

print(unrolled_df)