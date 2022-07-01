# the while loop
# while Boolean or Boolean Expression: 
    # code block
    # to run while
    # condition is true

# You must be over 5 ft to ride
# I have a magic potion that will let you grow one inch everytime you use it!
# height = 65

# height = int(input("What is your height in inches? ")) # gives back whatever the user puts in (will be a string)
# while height < 60:
#     height += 1
#     if height < 58:
#         continue
#     print(f"You are too {height} inches tall \n and too short to ride!")
#     print("Drink my magic potion")

# print("Thanks for coming!")

# while True statements
while True:
    response = input("What do you want to do? Say hi [h], Say goodbye [g], or Quit? [q] ")
    if response.lower() == "h":
        print("hello")
    elif response.lower() == "g":
        print("goodbye")
    elif response.lower() == "q":
        break
    else:
        print("Invalid option.")
