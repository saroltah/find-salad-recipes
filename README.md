# Find Sallad Recipes

![Live website link]()

---

### Idea of the applicaton

 - Original idea: Users write an ingredient that is in their fridge, so the program gives them recipes.
 - The goal is for the user to use up what they have, so save food, don't throw out.
 
 </br>
 
### Otput and implemented idea:
 - BUT for this app it should be too big data base, that needs lot of time to creat 
 - So I created the small version, where users choose a vegetable (I call it favourite, but of course what they have), and they get a recommended sallad recipe.
 
 <br>
 
 ### Future functions:
 - Bigger data base
 - Being able to see more options, and choose the one they like
 - Adding more ingredients to restrict the circle
 - Having option to add own recipe
 - Maybe clean up data, because it contain some fruit and herbs also. For me they all go to the same category - plants. But add your favourite edible plant sounds silly.
 
 </br>
 
 ---

  
 ### Planning
 - I draw a diagram, from which function - which action what triggers, what is the next step.
 - I also planned out in text form.
 
  </br>
  
 ### User need:
 - Easy text and questions, easy to understand and follow
 - Error-handling, when their answer is incorrect, it gives information why, and gives another opportunity to correct it.
 - Browsing through cooking books or videos takes up too much time and energy, so this should be a quick opportunity to help inspire the user about that days meal.
   Also it saves money if you can use up the ingredients you already have.

 </br>
 
### Follow through the app:
- Introduction - welcome text.

- The users are asked to type a vegtable - if it is not text, it throws an error, that they should write a text. Other characters are not allowed.

- Then the program loops through its data base, to find if the wished veggie is matching with the ingredients of one of the recipes. Meanwhile it lets user know that it is loading looking for recipes...

  - If there is match, it says "Horray.." 

  - It shows the recipe's name, and show's the other veggies that are needed. It asks the users, if they want to see the whole recipe.

	- If they do want to see the whole recipe, it shows the link of the website where they can find it. Then the program asks, if they want to find another recipe or not. 

		- If they do want to find another recipe, they can start adding a veggie again.

		- If they don't want to look for more recipes, the program says bye, and exit.

		- If the users chose that they don't want to see the recipe, they have the option to look for something else.

			- If they want to find another recipe, they can start adding a veggie again.

			- If they don't want to look for more recipes, the program says bye, and exit.

	- If there is no match for the recipe, It says "Oh no.. "

	- Then program asks if they want to look for something else:

		- If they want to find another recipe, they can start adding a veggie again.

		- If they don't want to look for more recipes, the program says bye, and exit.
		
</br>

---

## Process of coding, Errors and solutions

</br>

### Workflow

- I try out everything continuosly. I am using print() for every new variable or function to try, and run the project every single time anything is added.
- I also wrote down which function triggers what, so I can compare it how my code follows, where is the error.
- I made some variables global, so i can access them later.
- I define all functions, and after that the app starts with print() and calling the functions.
 
 </br>

### Progress, errors and solutions

</br>

### 1. 
**Define how program would work, make a diagram.**

 </br>

### 2. 
**Set up api for google sheet**
   
! write it out from videos
 
</br>

### 3. 
**Set up python**
- integrate API, hide creds.json file

</br>

### 4. 
**Install python libraries**

 </br>

### 5. 
**ask_for_veggie() function:**
- Add presentation of app: "Are you craving for some yummy sallad? Tell your favourite veggie, and I show you what you can make out of it.
- Add  the favoruite_veggie input with example.
	
	 </br>

### 6. 
**validate_favoruite_veggie() function:** 
 Make favourite_veggie input data valid: 
- Make all the input lower case 
- I put ask_for_veggie into a while loop, so when validation fails, it will ask again, until the input is correct.
- If the user writes anything silly that is not a veggie, then nothing happens, it is an ingredient that the program can not find.
	
**- Error 1:** 
  
Def validate function was not working

**- Solution:** 
  
validate_favourite_veggie was inside the ask_for_veggie function, I needed to take it out.
	
**- Error 2:** 
  
Isistance, type(), didn't work.

**- Solution:** 
  
I used isnumeric() first. But to handle special characters and empty spaces I changed it to not isalpha().
	
**- Error 3:** 
  
It was not validating again.

**- Solution:** 
  
return was after break, so I chancged and now break is after return.
   
</br>

### 7. 
**get_columns() function:**
- Creates column-lists from the index of the rows.
  - Checks length of the first row - that is the range it will loop through,
  - Then creates a column from all the rows same index-number values
  - Then puts these lists into one big all_columns list
	
</br>

### 8. 
**find_matching_recipe() function:**
- It checks if the given favourite_veggie input data is found in the data-base. Then with if-else function shows message if data was found or not.
- (It was show matching recipe first, but i rather devided it into two functions.)
- For checking errors I print all_ingredients - there was many empty cells.(I created empty_table function, but in the end deleted and chose to delete spaces within show_matching_recipe function) Also it checks the rows - I want to check columns. -> I created get_columns function.
	
**-Error 1-2:** 
  
When it loops through all ingredients, it writes out many times if there is match or no. Also it says no match, when there is match.

**- Solution:** 

-There was no break. So when I added break, it stopped after the first matching column. But If the first matching column was the 3rd, it wrote out 2times no solution, then 3rd found it. So I added pass instead of break for no matches. But then I couldn't have no-match message.  
- Then I noticed the columns were nested. The reason of error is that it looped through the columns one by one. So it only looped through the first one, when it had a break. So i created flattened columns, which united all the separate column lists to one list, so the function can look thorugh all data. Now I could check if the input is in the list. So don't need to loop anymore, and I can add message.
							
**-Error 3:** 
    
For the case there was no matching recipe, I added ask_for_veggies function, but it didn't show anything 
    
**- Solution:** 
  
I created all_functions, where i put the whole sequence, and called that when the program needs to start again. I changed it later to Start_again function.	

- If there is match, it triggers show_recipe function. If there is no match, it triggers start_again() function.	
	
</br>

### 8. 
**Show_matching_recipe function:**
- It writes the name and the rest of the ingredients of the matching recipe. It shows 1 - the first matching recipe. - Future function: it shows all the matches, so user can choose.
	
- My goal was to find which column has that ingredient, I used enumerate() function, so it has the number of the columns. So I can loop through and get the list. I can find the favourite-veggie in the list, and call it back. 
In the end I removed enumerate function, because i had no need for the index numbers.
         modified code: 
		 for column in spaceless_columns:
         instead of:
		 for index, column in enumerate(spaceless_columns):
			num_list = f"{index} : {column}"
	
**- Error:** 

some values are not found.

**- Solution:** 

Remove empty values! : columns = [x for x in columns if x != ''] but it's not working. So i created a new list spaceless_columns. The values were not returning in list, because I returned x directly back to spaceless_columns. Instead I created a spaceless_column list too, return x back to spaceless_column and  returned spaceless_column back to spaceless_columns. 
	
_-initial ideas for this function:_
	- 1: idea: define row first: 
		Get the rows as a list - 0, 1: 2:
		Then loop through rows: avocado, beatroot, pea pl.
		Then get avocados place: pl row-index 0
		Then add+1 so get the column, since column numbers starts from 1

		OR

	- idea 2, get columns as lists:[sallad1], [sallad2]  and loop through where avocado is. I used this idea. The function loops through the spaceless columns, checks in which recipe the favoruite_veggie is, then it breaks.  
	That is why it shows only one option. The column(list) where is founds the veggie is a list with "normal" index numbers, so I could call the name of the recipe with [0] and the rest of the ingredients with [1:]
  In future when I add chose_recipe function, I remove break, so it shows all the options.
				
I reunited the find_matching_recipe and show_matching recipe, which was working the same fine, but I think it is better to have smaller functions, so I rather leave them separate.

 </br>

### 9. 
**show_the_whole_recipe function:**
-  The function asks the users if they want to see the whole recipe. The answer can be yes or no, with an if-elif statement the yes triggers show_recipe_link function, and no triggers start_again function.
-  I get the values of the link sheet of my google sheet (link_sheet), and call the values from it (all_links). Also I called again the get_columns() function, to make columns, just with different argument. 
- I used valide_answer() function, to check if the answer is anything else then yes or no. I used the same while True expression as in the first ask_for_veggie function.
  
**- Error:** 
  
Validation didn't work, it returned false always.

**- Solution:** 
   
I used yes or no - I changes it to yes AND no

 </br>

### 10. 
**show_recipe_link:**
-  It loops through the link_sheet columns, and if there is match with the name of the recipe, then it prints its link. 
- When the user gets the recipe, it triggers start_again() function.
             
 </br>

### 11. 
**adding start again() function:**
 - It can have same yes-no answer, as in show_whole_recipe() function, with the same while True loop and validate_answer() function. When the user says yes, it replays all the functions all_functions(), if the answer is no, it wished a nice day and exits the program.
 
**- Error 1:** 
    
It exits, but still show the show_whole_recipe function.

**- Solution:** 

In the main sequence  show_matching_recipe() is later then find_matching_recipe() function. Find_matching_recipe() can trigger start_again(), and even if it exits program, show_matching_recipe() would still be played. So I moved show_matching_recipe() into the find_matching__recipe, so it is only triggered by the user's answer.
             
**-  Error 2:**

If there are more matches, it playes through with the first match, exit, then it plays through with the second. 

**- Solution:** 

that was also fixed with getting flattened_list.

</br>

### 13. 
**Optimization:**

- I had functions for validating yes-no answered, I refactored them into one, and I use it with different arguments. I also reused get_columns function with different arguments.
	
- Making expressions shorter

1.  spaceless_column=[]
		for x in column:
			if x.strip() != '':
				spaceless_column.append(x)
       
spaceless_column=[x for x in column if x.strip() != '']

2.		columns = []
			for row in sheet:
				columns.append(row[columns_index])

columns = [row[columns_index] for row in sheet]

</br>

---

</br>

### Credits:  

**1. Getting columns from rows:**

for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
	
**SOURCE:** ![Python.org](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)


**2. Making flattened list**

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = []
for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)
		
**SOURCE:** ![Io flood](https://ioflood.com/blog/python-flatten-list-how-to-flatted-nested-lists-in-python/)
		
**3. I learned about how to make expressions shorter:**

**SOURCE:** ![Spark by examples]( https://sparkbyexamples.com/python/write-python-for-loop-in-one-line/)

**4. Making string from list:**
 
my_list = ['apple', 'banana', 'orange']
delimiter = ', '
my_string = delimiter.join(my_list)
print(my_string)
Output: apple, banana, orange

**SOURCE:** ![Simpli learn](https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python)

</br>

---

</br>

##Deployment
 !?
  </br>
---
 </br>

## Technology I used:
 
 - ![GitHub]()
 - ![Heroku]()
 - ![Google Sheet]()
 - ![VS Code]()
  
**Libraires:**
-  gspread
- Credentials from google.oauth2.service_account 
 
