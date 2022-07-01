#different ways to define a dictionary 
my_dict = {}
my_dict = dict()

#key value pair
my_dict = {
    "key": "value"
}

#key word argument
my_dict = dict(key="value")

#dictionaries are a collection of key-value pairs
#immutable types: floats, integers, strings, tuples
steve = {
    "name" : "Steve",
    "weight" : 155.5,
    "height" : 70,
    "foods" : ["country fried steak", "fried chicken", "collards"],
    "ice_cream" : {
        "vanilla":False,
        "chocolate":True,
        "coffee":False
    },
    10 : "this has an integer key"
}

#name_of_dict[KEY]
print(steve["foods"])
print(type(steve["foods"]))
print(steve["ice_cream"])
print(type(steve["ice_cream"]))

#how to index into a list within a dictionary
print(steve["foods"][1])

# how to index into a dict within a dict
print(steve["ice_cream"]["vanilla"])
print(type(steve["ice_cream"]["vanilla"]))

#safer way to index into a dict
print(steve.get("candies")) # will either return none or will return target
print(steve.get("candies", "No Candy List")) # if you enter a second value it will also return the second value

#change value of a key
steve["name"] = "Joe"
print(steve)

my_list = [1,2,3]
my_list[1]="wow"
print(my_list)

# name update
steve.update({"candies":["snickers", "mars", "m&ms"]})
print(steve)

#delete something
del steve["candies"]
print(steve)

#looping through dict
for key in steve: #this will get just the key
    print(key)
    print(type(key)) # gets the data type of the keys
    print(steve[key]) # this will get the value of the keys

# getting just the values
print(steve.values())
for value in steve.values():
    print(value)
    print(type(value))

print(steve.items()) # this will work similar to enumerate - will give us back the key and the value as tuples
for key, value in steve.items():
    print(key, end=" ")
    print(value)

for key, value in steve.items():
    if isinstance(value, list):
        print(f"The list is at {key}")

