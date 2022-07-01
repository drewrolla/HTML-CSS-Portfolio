foods = ["pizza", "tacos", "dim sum", "sushi"]

print(foods[1])

#for PLACEHOLDER in THE_LIST_WE_WANT_TO_LOOK_AT:
    # this is a code block
    # this code block
    # will run every item in the list

for food in foods:
    print(
        f"I like to eat {food}"
        )
    print(type(food))

print("loop is over")

for food in foods:    
    if food == "dim sum":
        continue # continue skips item in list, break stops loop after item listed
    print(f"I like {food} because they are yummy")

#loop of the index
print(list(range(4)))
print(len(foods))

for index in range(len(foods)):
    print(index)
    print(foods[index])

print(list(enumerate(foods)))
for index, food in enumerate(foods):
    print(f"My no. {index + 1} food is {food.title()}")

#tuples
#cannot be changed, can be reassigned but cannot be changed
my_string = "Steve"
my_string = my_string + " smells like Teen Spirit"
print(my_string)

my_tup = 1, 2
print(my_tup)
my_tup = (1, 2)
print(my_tup)

for num in my_tup:
    print(num)

my_tup = my_tup + (3, 4)
print(my_tup)

#Slicing
my_string = "Hey Guys Lets Learn Python"
my_list = ["pizza", "tacos", "dim sum", "sushi"]

#example: slicing is like range, follows same pattern - 0 is h, 1 is e, 2 is y, 3 is the space, and so on
print(my_string[1:4])

print(my_list[1:4:2])                                                     