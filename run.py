import gspread
from google.oauth2.service_account import Credentials
from statistics import mean
import os
import time


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cafe-ciao')

review = SHEET.worksheet('review')
improve = SHEET.worksheet('improve')

data = review.get_all_values()


def print_welcome():
    """
    Prints welcoming message
    Clears the first screen
    """
    # 1st screen
    print("Thank you for visiting cafe 'Ciao'\n")
    print("Please take a few moments to leave us your review.")
    print("It will help us to improve our service.\n")
    for i in range(5, 0, -1):
        print(f"{i}", end="\r", flush=True)
        time.sleep(1)
    os.system("clear")


def get_review():
    """
    Gets user's review asking four questions.
    Gets a point from 1 to 5 for each question.
    1 is bad, 5 is good.

    Returns:
        a list of strings
    """
    # 2nd screen
    while True:
        print("Answer four questions below:")
        print("For each question give a point from 1 to 5,")
        print("where 1 is bad and 5 is good\n")

        data_str_food = input("How tasty was the food?\n")
        if validate_data(data_str_food):
            data_str_service = input("How friendly was our staff?\n")
            if validate_data(data_str_service):
                data_str_clean = input("How clean is our cafe?\n")
                if validate_data(data_str_clean):
                    data_str_vibe = input("How do you like the atmosphere?\n")
                    if validate_data(data_str_vibe):
                        break

    return [data_str_food, data_str_service, data_str_clean, data_str_vibe]


def validate_data(value):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if the given point is higher than 5.

    Args:
        value (str) the value to validate

    Returns:
        True if valid, False otherwise
    """
    try:
        if int(value) > 5:
            raise ValueError(
                f"Points from 1 to 5 required, you gave {int(value)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_review_worksheet(data):
    """
    Updates review worksheet, adds new row with the list data provided.
    Prints average review point.
    Clears the screen
    """
    review_worksheet = SHEET.worksheet("review")
    review_worksheet.append_row(data)
    # 3rd screen
    average = mean(data)
    print(f"Your review: {round(average, 1)}")
    print("Thank you!")
    for i in range(2, 0, -1):
        print(f"{i}", end="\r", flush=True)
        time.sleep(1)
    os.system("clear")

    return round(average, 1)


def ask_recommendations(data):
    """
    Gets user's recommendations asking another question.
    Gets text input.
    Appends average review point and recommendations to "improve" sheet.
    """
    # 4th screen
    print("We'll be happy if you share with us your thoughts")
    print("on what we can improve ;)\n")
    print("Please type 'yes' if you want to give us some recommendations or")
    yes_no = input("type 'no' if you want to finish and exit the program:\n")
    if yes_no == "yes":
        # 5th screen
        time.sleep(1)
        os.system("clear")
        recommends = input("Please share with us your tips:\n")

        # 6th screen
        time.sleep(1)
        os.system("clear")
        print("Thank you very much!")
        print(f"We'll take your recommendation '{recommends}' into account.")
        print("We hope to see you again!\n")

        improve_worksheet = SHEET.worksheet("improve")
        insertRow = [data, recommends]
        improve_worksheet.append_row(insertRow)
    elif yes_no == "no":
        # 5th screen
        time.sleep(1)
        os.system("clear")
        print("Thank you for your time. We hope to see you again!\n")
        improve_worksheet = SHEET.worksheet("improve")
        insertRow = [data]
        improve_worksheet.append_row(insertRow)
    else:
        print(f"Invalid input: {yes_no}. Please type 'yes' or 'no'")
        time.sleep(3)
        os.system("clear")
        ask_recommendations(data)

    print("Analysing our performance for the last five visitors...\n")


# code for this function is taken from the Love Sandwiches project
def get_last_5_entries_review():
    """Collects collumns of data from review worksheet,
    collecting the last 5 entries for each kind of service,
    and returns the data as a list of lists
    """
    review = SHEET.worksheet("review")

    columns = []
    for ind in range(1, 5):
        column = review.col_values(ind)
        columns.append(column[-5:])

    return columns


# code for this function is taken from the Love Sandwiches project
def calculate_performance(data):
    """
    Calculates average review for each type of service
    """
    average_performance = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        average_performance.append(round(average, 2))

    return average_performance


def analyse_performance(data):
    """
    Creates dictionary from the list of average performance.
    Keys are headings in review worksheet.
    Iterates through dictionary to find the smallest and the biggest number.
    Prints out poor and good performance according to the result.
    """
    review = SHEET.worksheet("review").get_all_values()
    keys = review[0]
    performance = {keys[i]: data[i] for i in range(len(keys))}

    print(performance)
    print("")

    for key, value in performance.items():
        poor_performance = min(performance.values())
        best_performance = max(performance.values())
        if poor_performance == value:
            print(f"Poor performance: {key}.")
            print(f"We're going to improve our {key}.\n")

        if best_performance == value:
            print(f"Good performance: {key}.")


def main():
    """
    Run all program functions
    """
    print_welcome()
    data = get_review()
    review_data = [int(num) for num in data]
    average_review = update_review_worksheet(review_data)
    ask_recommendations(average_review)
    columns_list = get_last_5_entries_review()
    average_performance = calculate_performance(columns_list)
    analyse_performance(average_performance)


main()
