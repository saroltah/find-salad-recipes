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

ingredients_sheet = SHEET.worksheet('ingredients')
all_ingredients = ingredients_sheet.get_all_values()

print("Are you craving for some yummy sallad?")
print("Tell your favourite veggie, and I show you what you can make out of it.")
def ask_for_veggie():
    """
    Get user's favourite vegetable
    """
    while True:
        global favourite_veggie
        favourite_veggie_input = input("Type one vegetable. For example: tomato \n")
        favourite_veggie = favourite_veggie_input.lower()
        if validate_favourite_veggie(favourite_veggie):
            print ("I am looking for recipes..")
            break
        return favourite_veggie

def validate_favourite_veggie(value):
    try:
        if value.isnumeric():
            raise ValueError
    except ValueError as e:
        print("Please type a vegtable") 
        return False
    return True

def get_columns():
    """
    Makes the columns list
    """
    all_columns=[]
    for columns_index in range(len(all_ingredients[0])):
        columns = [row[columns_index] for row in all_ingredients]
        all_columns.append(columns)
    #print(all_columns)
    return(all_columns)

def clean_columns(all_columns):
    """
    removes empty values
    """
    clean_columns = []
    for column in all_columns:
        for x in column:
            if x.strip() != '':
                #print(x)
                clean_columns.append(x)
    #print(clean_columns)

def find_matching_recipe(value, column):
    """
    Find recipes, which contain the input ingredient.
    """
    for ingredient in column:
        if value in ingredient:
            print("Hurray, I show you your match!")
            return(value)
        else:
            print("Oh no, I haven't found any recipes, try it again with something else.")
        #all_functions()
    
def all_functions():
    """
    Plays the whole sequence.
    """
    ask_for_veggie()
    get_columns()
    #clean_columns(get_columns())
    find_matching_recipe(favourite_veggie, get_columns())
    

all_functions()


