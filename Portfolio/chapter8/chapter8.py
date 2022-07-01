# Functions
# saves codes for later

# def NAME_OF_FUNCTION(PARAMETERS):
    # these lines
    # belong 
    # to the code block
    # for the function

# def hello():
#     print("Hello")

# hello()

# what if you try to print a function?
# print(hello()) --> inside function will ALWAYS happen first
# this will print, Hello \n None
# python always uses a return None at end of function
# returning is what the function becomes
# if you print function without executing it (aka using the parenthesis at the end), it will tell you that it is a function

# def hello():
#     return "Hello"

# print(hello())  

# Print vs Return
# print - writes to the CLI
# print is better for debugging code
# return - will make value of function executed | i.e., hello() the object that is returned from the function
# return is better for real world applications


# def hello(name, age = 55):
#     print(f"hello {name}, you are {age} years old")

# # will get error if try running without giving parameter

# hello("Drew", 24)

# order of the parameters matter when you are putting the values in
# using code from above, if you were to do this:
# hello(24, "Drew")
# the code will print/return:
# hello 24 you are Drew years old
# a fix: hello(age = 24, name = "Drew")
# can set default values for parameters - any input you give will override the default
# however, default arguments must be set at end of parameters
# i.e. this will give an error: def hello(name = "John", age)
# i.e. this will not: def hello(age, name = "John")

# def my_function(num):
#     while num < 10:
#         print(num)
#         if num == 6:
#             return
#         num += 1

# my_function(4)

def say_hello(name, age):
    print(f"Hello {name}, you are {age} years old.")

def say_goodbye():
    print("Goodbye.")

def greet_back(feeling):
    if feeling == "good":
        print("Awesome! I feel good too!")
    elif feeling == "bad":
        print("I am so sorry")
    elif feeling == "stressed":
        print("Haha, mood. Coding is difficult to learn.")
    else:
        print("Well, have a day.")

# Driver Code
while True:
    response = input("What do you want to do? Say hello [H], say goodbye [G], talk to me [T], or quit [Q]? ")
    if response.lower() == 'q':
        print("Goodbye friend.")
        break
    elif response.lower() == 'h':
        name = input("What is your name? ")
        age = input("What is your age? ")
        say_hello(name, age)
    elif response.lower() == 'g':
        say_goodbye()
    elif response.lower() == 't':
        feeling = input("How are you today? ")
        greet_back(feeling)
    else:
        print("Invalid input.")

