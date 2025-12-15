import csv # to save and read data in CSV files
from datetime import date # to automatically get today's date
import os # to check if the CSV file already exists

File_name = "study_balance_tracker.csv" # name


def create_csv_file_if_not_exist():
    if not os.path.exists(File_name): # check if file already exists
        with open(File_name, mode="w", newline="") as file: # creates new file
            writer = csv.writer(file) # it prepares CSV file
            writer.writerow([ # writes the collumn headings
                "Date",
                "Study Hours",
                "Break Hours",
                "Sleep Hours",
                "Mood",
                "Notes"
            ])

