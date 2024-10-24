import re

def find_all_dates(text):
    # Regular expressions for the different date formats
    date_patterns = [
        r'\b\d{2}-\d{2}-\d{4}\b',  # dd-mm-yyyy
        r'\b\d{2}/\d{2}/\d{4}\b',  # mm/dd/yyyy
        r'\b\d{4}\.\d{2}\.\d{2}\b' # yyyy.mm.dd
    ]
    
    # List to store all the found dates
    all_dates = []
    
    # Find all dates that match any of the patterns
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        all_dates.extend(matches)
    
    return all_dates

# Test the function
text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
dates = find_all_dates(text)
print(dates)
