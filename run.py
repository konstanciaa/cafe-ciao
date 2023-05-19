import gspread
from google.oauth2.service_account import Credentials
from statistics import mean

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET_C = GSPREAD_CLIENT.open('cafe-ciao')
SHEET_R = GSPREAD_CLIENT.open('cafe-ciao-review')

review = SHEET_C.worksheet('review')
improve = SHEET_R.worksheet('improve')

data = review.get_all_values()


def print_welcome():
    # 1st screen
    print("Thank you for visiting cafe 'Ciao'\n")
    print("Please take a few moments to leave us your review.")
    print("It will help us to improve our service.\n")


def get_review():
    """
    Get user's review asking four questions.
    Get a point from 1 to 5 for each question.
    1 is bad, 5 is good.

    Returns:
        a list of integers
    """
    # 2nd screen
    while True:
        print("Answer four questions below:")
        print("For each question give a point from 1 to 5, where 1 is bad and 5 is good\n")

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
    Update review worksheet, add new row with the list data provided.
    Print average review point.
    """
    review_worksheet = SHEET_C.worksheet("review")
    review_worksheet.append_row(data)
    # 3rd screen
    average = mean(data)
    print(f"Your review: {round(average, 1)}")
    print("Thank you!")
    
    return round(average, 1)

        
def main():
    """
    Run all program functions
    """
    print_welcome()
    data = get_review()
    review_data = [int(num) for num in data]
    average_review = update_review_worksheet(review_data)
    # new_function(average_review)


main()