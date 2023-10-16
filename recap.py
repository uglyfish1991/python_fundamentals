# print("This allows us to see outputs")

# print("1234")

# print(1234)

# print(12.34)

# print(5.0)

# print(True)
# print(False)

# print(None)

# print("hello".upper())

# my_name = "Katy"

# print(my_name)

# print(f"Welcome to your account, {my_name}")

# print("Welcome to your account, " + my_name)

# print("Welcome to your account,", my_name)

# print("Welcome to your account, {}".format(my_name))

# print(5+9)

# print(9-5)

# print(3*2)

# print(3**3)

# print(15/3)

# print(15%3)

# user_name = input("What is your name?")

# print(f"Hello {user_name}")

balance = 100

amount_to_withdraw = int(input(" How much to do you want to withdraw  >   "))

# # balance = balance - amount_to_withdraw

# # print(f"your new balance is {balance}")

while amount_to_withdraw > balance:
    print("insufficient funds")
    amount_to_withdraw = int(input(" How much to do you want to withdraw  >   "))
else:
    balance = balance - amount_to_withdraw
    print(f"your new balance is {balance}")


# if amount_to_withdraw < balance:
#     balance = balance - amount_to_withdraw
#     print(f"your new balance is {balance}")
# else:
#     print("Insufficient funds")


# == 
# != 
# <= 
# >=
# >
# <

# and 

# or 

# day = "Saturday"
# bank_holiday = False

# if day == "Saturday" or day == "Sunday" or bank_holiday==True:
#     print("A day off!")
# else:
#     print("Off to work we go")

# and 

# True + True = True
# False + True = False 
# False + False = False

# or 

# True + True = True
# False + True = True
# False + False = False