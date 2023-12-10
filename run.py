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
    Ask the user about their favourite vegetable.
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
    Check if the answer is not numeric. If it is, it gives an error message.
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
    Get the columns from the ingredients sheet.
    """

    all_columns=[]

    for columns_index in range(len(sheet[0])):
        columns = [row[columns_index] for row in sheet]
        all_columns.append(columns)

    return(all_columns)


def find_matching_recipe(veggie, columns):
    """
    Find recipes, which contain the input ingredient.
    Let the user know if there is recipe foind, or not.
    If there is recipe found, it will be shown after.
    If there is no recipe found, the user has an option to start it again.
    """

    nested_columns = columns
    flattened_columns = []

    for sublist in nested_columns:
        for item in sublist:
            flattened_columns.append(item)

    if veggie in flattened_columns:
        print("Hurray, I show you your match!")
        show_matching_recipe(favourite_veggie, get_columns(all_ingredients))    
    else:
        print("Oh no, I haven't found any recipes, try it again with something else.")
        start_again()
       
def show_matching_recipe(veggie, columns):
    """ 
    Delete empty objects from list.
    Show the user the matching recipe with the rest of the ingredients.
    """

    spaceless_columns=[]

    for column in columns:
        spaceless_column=[]
        for x in column:
            if x.strip() != '':
                spaceless_column.append(x)
        spaceless_columns.append(spaceless_column)
        
    for index, column in enumerate(spaceless_columns):
        num_lists = f"{index} : {column}"

        if veggie in num_lists:
            global recipe_name
            recipe_name = column[0]
            
            ingredients = column[1:]
            delimiter = ', '
            other_ingredients = delimiter.join(ingredients)

            matching_recipes = f"Name: {recipe_name}. All ingredients: {other_ingredients}"
            print(matching_recipes)   
            show_the_whole_recipe()
            break

def show_the_whole_recipe():
    """
    Ask user if they want to see the whole recipe.
    If they say yes, they will be shown the link.
    If they say no, they have the option to start again.
    """

    link_sheet = SHEET.worksheet('link')
    all_links = link_sheet.get_all_values()
    get_columns(all_links)

    while True:
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
    Check if the answer is yes or no.
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
    Show the link of the recipe. 
    """

    for link in links:
        if name in link:
            print(f"You can find the whole recipe on this link: \n {link[1]}")
    start_again()

def start_again():
    """
    Ask user if they want to find another recipe.
    If they say yes, they can start again adding ingredient.
    If they don't, they exit the program.
    """

    while True:
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
    Check if the answer is yes or no.
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
    Play the whole sequence.
    """

    ask_for_veggie()
    get_columns(all_ingredients)
    find_matching_recipe(favourite_veggie, get_columns(all_ingredients))
    #show_matching_recipe(favourite_veggie, get_columns(all_ingredients))
    #show_the_whole_recipe()

all_functions()
 