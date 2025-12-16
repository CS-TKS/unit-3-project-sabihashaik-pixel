import matplotlib.pyplot as plt
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



def log_daily_data():
    today = date.today()  # this get today date automatically
    study_hours = (float(input("How many Hours do you study each day: "))) # user input
    break_hours = (float(input("How many break hours do you have today: "))) # user input
    sleep_hours = (float(input("How many Hours you do sleep each day: "))) # user input
    mood = (input("What is your mood today: "))
    notes = (input("What notes to you have for today: ")) # extra notes

    with open(File_name, mode="a", newline="") as file: # this opens file in data
        writer = csv.writer(file) # prepares CSV writer
        writer.writerow([
            "today",
            "study_hours",
            "break_hours",
            "sleep_hours",
            "mood",
            "notes"
    ])


print("Data successfully saved!")


def show_menu():
    print("\n🍀 Study Balance Tracker")
    print("1. Log Today's Data")
    print("2. Review Past Records")
    print("3. Show Graph")
    print("4. Reflection Chatbot")
    print("5. Exit")


def main():
    create_csv_file_if_not_exist() # ensure the CSV exists

    while True:
        show_menu()
        choice = input("Please Choose An Option (1-5)")

        if choice == "1":
            log_daily_data()
        elif choice == "2":
            view_past_records()
        elif choice == "3":
            show_graphs()
        elif choice == "4":
            reflection_chatbot()
        elif choice == "5":
            print("Goodbye, stay Balanced")
            break
        else:
            print("Invalid Option, try again")



def view_past_records():
    if not os.path.exists(File_name): # checks if file exists
        print("NO RECORDS FOUND YET")
        return



with open(File_name, mode="r") as file:  # opens file to read
    reader = csv.writer(file)
    next(reader)
    print("/n Past Study Records ")
    for row in reader:
        print(f"Date: {row[0]}, Study: {row[1]}h, Break: {row[2]}h, Sleep: {row[3]}h, Mood: {row[4]}, Notes: {row[5]}")
        # this prints the names and info neatly in each row.



def show_graphs():
    if not os.path.exists(File_name):
        print("NO DATA TO DISPLAY")
        return

    dates = []
    study_hours = [] # stores study hours
    break_hours = [] # stores break hours
    sleep_hours = [] # stores sleep hours

    with open(File_name, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            dates.append(row[0])
            study_hours.append(float(row[1]))
            break_hours.append(float(row[2]))
            sleep_hours.append(float(row[3]))

        if len(dates) == 0:
            print(" NO DATA TO DISPLAY.")
            return


        x = range(len(dates))
        plt.figure(figsize=(10,5))
        plt.bar(x, study_hours, width=0.4, label="Study Hours", color="green", align="center")
        plt.bar(x, break_hours, width=0.4, label="Break Hours", color="blue", align="edge")
        plt.xticks(x, dates, rotation=45)
        plt.xlabel("Date")
        plt.ylabel("Hours")
        plt.title("Study vs Break Hours")
        plt.legend()
        plt.tight_layout()
        plt.show()

# Line graph: Sleep Hours Over Time
        plt.figure(figsize=(10,5))
        plt.plot(dates, sleep_hours, marker='o', color="purple", label="Sleep Hours")
        plt.xticks(rotation=45)
        plt.xlabel("Date")
        plt.ylabel("Hours")
        plt.title("Sleep Hours Over Time")
        plt.legend()
        plt.tight_layout()
        plt.show()




def reflection_chatbot():
    print("\n Reflection Chatbot")  # title

    # Ask simple reflection questions
    focus = input("How focused did you feel today on your studies? (1-5): ")
    mood = input("How would you rate your mood today? (1-5): ")
    breaks = input("Did taking breaks help you concentrate? (yes/no): ")
    improvement = input("What is one thing you would like to improve tomorrow? ")

    # Give simple feedback based on answers
    print("\n Feedback:")

    if focus.isdigit():
        if int(focus) >= 4:
            print(" Great focus today! Keep it up.")
        else:
            print(" Try to limit distractions for better focus tomorrow.")

    if mood.isdigit():
        if int(mood) >= 4:
            print(" Glad you felt good today!")
        else:
            print(" Remember to take care of yourself and relax when needed.")

    if breaks.lower() == "yes":
        print(" Good job taking breaks! They help your brain recharge.")
    else:
        print(" Try taking short breaks to improve focus and avoid burnout.")

    print(f" Note for tomorrow: {improvement}")
    print(" Reflection complete!\n")



