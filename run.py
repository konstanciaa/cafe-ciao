import gspread
from google.oauth2.service_account import Credentials

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


def get_review():
    """
    Get user's review asking three questions.
    Get a point from 1 to 5 for each question.
    1 is bad, 5 is good.
    """
    # second screen
    print("Please answer three questions below:")
    print("For each question give a point from 1 to 5, where 1 is bad and 5 is good")

    data_str_food = int(input("How tasty was the food?\n"))
    validate_data(data_str_food)
    data_str_service = int(input("How friendly was our staff?\n"))
    validate_data(data_str_service)
    data_str_clean = int(input("How clean is our cafe?\n"))
    validate_data(data_str_clean)
    data_str_vibe = int(input("How do you like the atmosphere?\n"))
    validate_data(data_str_vibe)
    

def validate_data(value):
    """
    Inside the try converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if the given point higher than 5.
    """
    try:
        if value > 5:
            raise ValueError(
                f"Points from 1 to 5 required, you provided {value}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


# first screen
print("Thank you for visiting cafe 'Ciao'")
print("Please take a few moments to leave us your review. It will help us to improve our service.")
get_review()