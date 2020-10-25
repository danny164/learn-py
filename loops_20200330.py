pizza_toppings = ["cheese", "pepperoni", "mushrooms"]

for topping in pizza_toppings:
    print(topping)
    
##############################
print("\n")

for my_topping in pizza_toppings:
    message = f"I would like {my_topping} on my pizza"
    print(message)

### using loop

my_numbers = [1, 2, 3]
my_square_numbers = []

print(f"\n{my_numbers}")

for number in my_numbers: # 'number' is the variables 1, 2, 3 in loop
#   print(number) 
    my_square_numbers.append(number**2) # **2 = ^2
print(my_square_numbers)


### using range
print ("\n")

for i in [1, 2, 3, 4, 5]:
    print(i)
    
##############################
print("\n")

for i in range(1, 11): # from 1 to 10
    print(i)
    
##############################
print("\n")

print(list(range(1, 11)))




