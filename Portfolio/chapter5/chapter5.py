#booleans can be two things ON or OFF True or False Yes or No
my_bool = True
print(my_bool)
my_bool = False
print(my_bool)
print(bool(0))
#empty strings will return False
#non-empty strings will return True

#boolean expressions
#> < >= <= == != 

print("dog" == "cat")
print("dog" == "dog")
print("dog" == "Dog".lower())
print(4 < 6)
print(6 >= 6)
print(69 > 70)

x=10
print(5 < x < 20)

#letters have number values
print(ord("a"))
print(ord("A"))
letter = "a"
print(letter > "b")
letter = "c"
print(letter > "b")
letter = "A"
print(letter > "a")
letter = "a"
print(letter > "A")

x = 10
y = 10
z = 20
print(x == 10 and y == 10 and z == 10) #will return False
print(x == 10 and y == 10) #will return True
print(x == 10 or z == 10) # will return True because x == 10
# AND - both are true; OR - one is true

x = 8
y = 9
print(x == y)
print(x != y)
print(not True or False)
print(not True and True)


# if BOOLEAN OR BOOLEAN EXP:
    # code block
    #for if true
# else:
    # for the if false code block

height = 73

# Must be 5 ft tall to ride
# Must be under 6ft tall to ride
if height < 60:
    print("Sorry, you are too short to ride")
    print("Please get off")
elif height > 72:
    print("Sorry, you are too tall")
    print("Please get off")
else:
    print("Enjoy your ride!")
print("Thanks for visiting!")

