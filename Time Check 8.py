import pandas as pd

def check_time_coverage(df):
    full_week_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
    df['startTime'] = pd.to_datetime(df['startTime'], errors='coerce', format='%H:%M:%S').dt.time
    df['endTime'] = pd.to_datetime(df['endTime'], errors='coerce', format='%H:%M:%S').dt.time
    grouped = df.groupby(['id', 'id_2'])

    def is_coverage_complete(group):
        days = set(group['startDay']).union(set(group['endDay']))
        if group['startTime'].isnull().any() or group['endTime'].isnull().any():
            return False
        earliest_start_time = min(group['startTime'])
        latest_end_time = max(group['endTime'])
        days_covered = days == full_week_days
        time_covered = (earliest_start_time <= pd.to_datetime("00:00:00").time() and
                        latest_end_time >= pd.to_datetime("23:59:59").time())
        return days_covered and time_covered

    coverage_check = grouped.apply(lambda x: not is_coverage_complete(x), include_groups=False)
    return coverage_check

file_path = 'dataset-1.csv'  
df = pd.read_csv(file_path)
result = check_time_coverage(df)
print(result)