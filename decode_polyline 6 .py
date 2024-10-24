import polyline
import pandas as pd
from geopy.distance import geodesic

def decode_polyline_to_dataframe(encoded_polyline):
    # Decode the polyline string
    coordinates = polyline.decode(encoded_polyline)
    
    # Create a DataFrame from the list of coordinates
    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])
    
    # Initialize a column for distances
    df['distance'] = 0.0
    
    # Calculate distances using the Haversine formula (geodesic from geopy)
    for i in range(1, len(df)):
        # Get the previous and current coordinates
        prev_point = (df.loc[i-1, 'latitude'], df.loc[i-1, 'longitude'])
        curr_point = (df.loc[i, 'latitude'], df.loc[i, 'longitude'])
        
        # Calculate the distance between them in meters
        distance = geodesic(prev_point, curr_point).meters
        df.loc[i, 'distance'] = distance

    return df

# Example polyline string (can replace with an actual polyline)
encoded_polyline = "_p~iF~ps|U_ulLnnqC_mqNvxq`@"

# Call the function and print the DataFrame
df = decode_polyline_to_dataframe(encoded_polyline)
print(df)
