# Simple data parser for my ROBLOX analytics server. Useful for understanding user patterns.
# This is also my first legitimate Python project.
import pandas as pd
import os

# Let's get the file from the user using the built-in input function (very nice, python)
file = input("Enter data file (CSV): ");

# Detect if the file exists, if not, exit with error code 1
if os.path.exists(file):
    data = pd.read_csv(file);
else:
    print("That file doesn't exist"), exit(1);

# Assign a duration to each entry using (LeaveTime and ServerStart, ie, LeaveTime - ServerStart = DurationInSeconds)
data['DurationInSeconds'] = data['LeaveTime'] - data['ServerStart']

# Output the average duration of all entries
print(f"Average Visit Length: {(data['DurationInSeconds'].mean() / 60).__round__(1)} minutes")
print(f"Longest Visit Length: {(data['DurationInSeconds'].max() / 60).__round__(1)} minutes")

# Output the average duration of all entries (excluding the entries below 5 minutes in seconds)
print(f"Average Visit Length (excluding < 5 minutes): {(data[data['DurationInSeconds'] > 300]['DurationInSeconds'].mean() / 60).__round__(1)} minutes")