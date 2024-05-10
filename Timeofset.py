import csv
from datetime import datetime, timedelta

# Define the path to your CSV file
file_path = 'Labeled_Data/CJ77TAL 2024-05-08 10-13.csv'

# Initialize empty lists to store the data
new_rows = []

# Define the offset duration (50 minutes and 24 seconds)
offset = timedelta(minutes=50, seconds=24)

# Open the CSV file and read its contents
with open(file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Extract timestamp and label from each row
        original_timestamp = datetime.strptime(row['Timestamp'], '%Y-%m-%d %H:%M:%S.%f')

        # Apply the offset
        offset_timestamp = original_timestamp + offset

        # Update the row with the offset timestamp
        row['Timestamp'] = offset_timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')

        # Append the updated row to the new list of rows
        new_rows.append(row)

# Write the modified data back to the CSV file
with open(file_path, 'w', newline='') as csv_file:
    fieldnames = ['Timestamp', 'Label']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    csv_writer.writeheader()

    # Write the updated rows
    csv_writer.writerows(new_rows)

print("File has been updated with new timestamps.")
