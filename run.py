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

print(data)

