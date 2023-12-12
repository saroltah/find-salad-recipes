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

def ask_for_veggie():
    """
    Ask the user about their favorite vegetable.
    """

    while True:
        global favorite_veggie
        favorite_veggie_input = input("Type a vegetable. For example: tomato \n")
        favorite_veggie = favorite_veggie_input.lower()

        if validate_favorite_veggie(favorite_veggie):

            print ("I am looking for recipes..")
            return favorite_veggie
            break

def validate_favorite_veggie(veggie):
    """
    Check if the answer is not numeric. If it is, it gives an error message.
    """

    try:
        if not veggie.isalpha():
            raise ValueError ("Numbers and characters are not acceptable")
    except ValueError as e:
        print("Numbers and characters are not acceptable") 
        return False
    
    return True

def get_columns(sheet):
    """
    Get the columns from the googsheet.
    The column index is the length of the first row.
    """

    all_columns=[]

    for columns_index in range(len(sheet[0])):
        columns = [row[columns_index] for row in sheet]
        all_columns.append(columns)

    return(all_columns)


def find_matching_recipe(veggie, columns):
    """
    Find recipes, which contain the input ingredient.
    Let the user know if there is a recipe found, or not.
    If there is a recipe found, it will be shown after.
    If there is no recipe found, the user has an option to start it again.

    """

    nested_columns = columns
    flattened_columns = []

    for sublist in nested_columns:
        for item in sublist:
            flattened_columns.append(item)

    if veggie in flattened_columns:
        print("Hurray, I show you your match!")
        show_matching_recipe(favorite_veggie, get_columns(all_ingredients))    
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
        spaceless_column=[x for x in column if x.strip() != '']
        spaceless_columns.append(spaceless_column)
        
    for column in spaceless_columns:
        global recipe_name
        recipe_name = column[0]
            
        ingredients = column[1:]
        delimiter = ', '
        other_ingredients = delimiter.join(ingredients)

        if veggie in ingredients:
            matching_recipes = f"Name: {recipe_name}. All veggies you need: {other_ingredients}"
            print(matching_recipes)   
            show_the_whole_recipe()
            break

def show_the_whole_recipe():
    """
    Ask users if they want to see the whole recipe.
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

        if validate_answer(recipe_answer):

            if recipe_answer == "yes":
                show_recipe_link(recipe_name, get_columns(all_links))
            elif recipe_answer == "no":
                start_again()
            break

def validate_answer(answer):
    """
    Check if the answer is yes or no.
    """

    try:
        if answer != "yes" and answer != "no":
            raise ValueError ("only yes or no is acceptable")
    except ValueError as e:
        print("Please type yes or no") 
        return False

    return True

def show_recipe_link(name, links):
    """
    Show the link to the recipe.
    """

    for link in links:
        if name in link:
            print(f"You can find the whole recipe on this link: \n {link[1]}")
    start_again()

def start_again():
    """
    Ask users if they want to find another recipe.
    If they say yes, they can start again by adding an ingredient.
    If they don't, they exit the program.
    """

    while True:
        print("Would you like to look for another recipe?")
        start_again_answer_input = input("Type yes or no.\n")
        start_again_answer = start_again_answer_input.lower()
        if validate_answer(start_again_answer):  

            if start_again_answer == "yes":
                all_functions()
            elif start_again_answer == "no":
                print("Have a nice day")
                exit
            break

def all_functions():
    """
    Play the whole sequence.
    """

    ask_for_veggie()
    get_columns(all_ingredients)
    find_matching_recipe(favorite_veggie, get_columns(all_ingredients))
    #show_matching_recipe(favorite_veggie, get_columns(all_ingredients))
    #show_the_whole_recipe()
    
print("Are you craving some yummy salad?")
print("Tell your favorite veggie, and I show you what you can make out of it.")

all_functions()
 