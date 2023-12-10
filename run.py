import gspread
from google.oauth2.service_account import Credentials
from random import choice

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

def validate_favourite_veggie(veggie):
    """
    Check if the answer is not numeric
    """
    try:
        if veggie.isnumeric():
            raise ValueError ("Numbers are not acceptable")
    except ValueError as e:
        print("Please type a vegtable") 
        return False

    return True

def get_columns(sheet):
    """
    Makes the columns list
    """
    all_columns=[]
    for columns_index in range(len(sheet[0])):
        columns = [row[columns_index] for row in sheet]
        all_columns.append(columns)

    return(all_columns)


def find_matching_recipe(veggie, columns):
    """
    Find recipes, which contain the input ingredient.
    """
    for ingredient in columns:
        if veggie in ingredient:
            print("Hurray, I show you your match!")
            show_matching_recipe(favourite_veggie, get_columns(all_ingredients))
            break 
        else:
            print("Oh no, I haven't found any recipes.")
            start_again()
            break
    
def show_matching_recipe(veggie, columns):
    """ 
    Delete empty objects from list, then shows which list has the favorite_veggie ingredient.
    """
    spaceless_columns=[]
    for column in columns:
        spaceless_column=[]
        for x in column:
            if x.strip() != '':
                spaceless_column.append(x)
        spaceless_columns.append(spaceless_column)
        
    for index, column in enumerate(spaceless_columns):
        #print(f"index {index} : {column}")
        num_lists = f"{index} : {column}"
        #print(num_lists)
        if veggie in num_lists:
            global recipe_name
            recipe_name = column[0]
            ingredients = column[1:]
            delimiter = ', '
            other_ingredients = delimiter.join(ingredients)
            global matching_recipes
            matching_recipes = f"Name: {recipe_name}. Other ingredients: {other_ingredients}"
            print(matching_recipes)   
            show_the_whole_recipe()
            break

def show_the_whole_recipe():
    """
    Ask user if want to see the whole recipe
    """
    link_sheet = SHEET.worksheet('link')
    all_links = link_sheet.get_all_values()
    get_columns(all_links)

    while True:
        global recipe_answer
        print("Would you like to see the whole recipe?")
        recipe_answer_input = input("Type yes or no.\n")
        recipe_answer = recipe_answer_input.lower()

        if validate_recipe_answer(recipe_answer):

            if recipe_answer == "yes":
                show_recipe_link(recipe_name, get_columns(all_links))
            elif recipe_answer == "no":
                start_again()
            break

def validate_recipe_answer(answer):
    """
    Check if the answer is yes or no
    """
    try:
        if answer != "yes" and answer != "no":
            raise ValueError 
    except ValueError as e:
        print("Please type yes or no") 
        return False
    return True

def show_recipe_link(name, links):
    """
    show the link of the recipe. [1] is the first row in the link_sheet, where the links are.
    """
    for link in links:
        if name in link:
            print(f" You can find the whole recipe on this link: \n {link[1]}")
    start_again()

def start_again():
    """
    replayes all the functions from the beginning
    """
    while True:
        global start_again_answer
        print("Would you like to look for another recipe?")
        start_again_answer_input = input("Type yes or no.\n")
        start_again_answer = start_again_answer_input.lower()

        if validate_start_again_answer(start_again_answer):   
            if start_again_answer == "yes":
                all_functions()
            elif start_again_answer == "no":
                print("Have a nice day")
                exit
            break

def validate_start_again_answer(answer):
    """
    Check if the answer is yes or no
    """
    try:
        if answer != "yes" and answer != "no":
            raise ValueError 
    except ValueError as e:
        print("Please type yes or no") 
        return False
    return True

def all_functions():
    """
    Plays the whole sequence.
    """
    ask_for_veggie()
    get_columns(all_ingredients)
    find_matching_recipe(favourite_veggie, get_columns(all_ingredients))
    #show_matching_recipe(favourite_veggie, get_columns(all_ingredients))
    #show_the_whole_recipe()

all_functions()


