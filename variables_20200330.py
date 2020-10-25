my_boo = "Danny" # this is a variable
print(f"My boo's name is {my_boo}\n")

# This is a comment

def my_info(name, age):
    print(f"My name is {name}. I'm {age}.\n")
    
my_info("Danny", 22)

###

def cases(people): # this is a function
    return f"The confirmed cases of coronavirus are {people} people.\n"

num_people = cases(20) # the variable containts a funtion
print(num_people)

###

myfriend = ["Danny", "Lance", "Tony", "Lacy", "Tom"]
myfriend.append("David")
print(myfriend)

print(f"\nThe friend's name in 3nd position is {myfriend[3-1]}")

del myfriend[2]
print(f"\nThe current list is {myfriend}")

myfriend.pop()
print(f"\n{myfriend}")

myfriend = ["Danny", "Lance", "Tony", "Lance"]
myfriend.remove("Lance")
print(myfriend)
