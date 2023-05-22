import csv
from datetime import datetime
import os.path

# function to update CSV file with run data
def update_csv(file_path, date, duration, notes):
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode='a', newline='') as csv_file:
        fieldnames = ['Date', 'Duration', 'Notes']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # add header row if file is empty
        if not file_exists:
            writer.writeheader()

        # write new row to CSV file
        writer.writerow({'Date': date, 'Duration': duration, 'Notes': notes})


# get user input
date = input('Enter date (YYYY-MM-DD HH:MM:%S): ')
duration = input('Enter run duration (minutes): ')
notes = input('Enter notes (optional): ')

# update CSV file with run data
update_csv('run_data.csv', date, duration, notes)
