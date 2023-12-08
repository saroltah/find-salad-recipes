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
        print(favourite_veggie)
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

def clean_table(value):
    clean_column=[]
    for column in value:
        stripped_columns = []  
        for cells in column:
            spaceless_cells = cells.strip()  
            if spaceless_cells != '':
                stripped_columns.append(spaceless_cells)  
        clean_column.append(stripped_columns)  
    clean_row = []
    for row in value:
        for cells in row:
            if cells != '':
                clean_row.append(cells) 
    print(clean_row)
    return clean_column

def show_matching_recipe(value, table_value):
    """
    Find the recipes, which contain the input ingredient.
    """ 
    match = False
    for ingredient in table_value:
        if value in ingredient:
            match = True  
            break  
    if match:
        print("hurray")
    else:
        print("oh no")



ask_for_veggie()
clean_table(all_ingredients)
show_matching_recipe(favourite_veggie, clean_table(all_ingredients))

