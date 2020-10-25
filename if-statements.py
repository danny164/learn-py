numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_greater_than_five = []

for i in numbers:
    if i > 5:
        numbers_greater_than_five.append(i)

print(numbers_greater_than_five)

#############
print("\n")

pizza_toppings = ["cheese", "pepperoni"]
print("We have the following toppings:")

for topping in pizza_toppings:
    if topping == "cheese":
        print(f"{topping} (free)")
    else:
        print(f"{topping} ($1.00)")

print("\n")

### building blocks: variables, functions, list, loops, conditionals
#########################################
# Expected output
# Welcome to Julie's Pizzeria
# Our available toppings are:
# Cheese (Free)
# Pepperoni ($1 Extra)
#########################################

# the variable 'pizza_toppings' saved our toppings
pizza_toppings = ["cheese", "pepperoni"] #3 

# define format_topping function
def format_topping(topping): #4
    if topping == "cheese":
        return f"{topping.title()} (Free)" #4.1
    else:
        return f"{topping.title()} ($1 Extra)" #4.2

# define print_menu function
def print_menu(toppings): #2 argument 'toppings' refers to 'pizza_toppings'
    # and get the list of toppings
    print("Welcome to Julie's Pizzeria") #3.1
    print("Our available toppings are:") #3.2
    for topping in toppings: # loop 'topping' in toppings["cheese", "pepperoni"]
        print(format_topping(topping)) #4, 4.1, 4.2

# call print_menu function        
print_menu(pizza_toppings) #1 pizza_toppings gives the value passed by reference

# print_menu() We got an error.
# It's saying TypeError: print_menu is missing
# one required positional argument: toppings.
# That means that our print_menu's function is asking
# for the list of toppings but down here we didn't actually pass it anything.

# Our toppings are saved in the variable 'pizza_toppings'
# So put it into our function 'print_menu(pizza_topings)'













