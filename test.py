# count how many times something appears in a list
# we can't use .count() -  we are making our own .count()

# list of things
# input - what are we searching for?
# counter variable

# for loop - for each item in list:
# if item I'm searching for == item I'm looking at
# count it - counter +=1

list_of_things = ["apple", "banana", "orange", "grape", "apple"]

searching_for = input("What do you want to search for   > ")

counter = 0

for i in list_of_things:
    if searching_for == i:
        counter +=1

print(f"You searched for {searching_for} and it appeared {counter} times")
# print("You searched for {} and it appeared {} times".format(searching_for,counter))
# print("You searched for", searching_for, "and it appeared", counter,  "times")
