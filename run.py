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
SHEET = GSPREAD_CLIENT.open('find_sallad_recipes')

ingredients = SHEET.worksheet('ingredients')

data = ingredients.get_all_values()

print("Are you craving for some yummy sallad?")
print("Tell your favourite veggie, and I show you what can you make out of it.")
print("example: tomato")
favourite_veggie = input("Type one vegetable \n").lower()
print(favourite_veggie)