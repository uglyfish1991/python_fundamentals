# def say_hello():
#     print("Hello")

# say_hello()

# def say_goodbye():
#     print("Goodbye")

# say_goodbye()

# def say_something(something):
#     print(f"{something}")

# say_something("Hello again")  # hard coded argument
# say_something(input("what do you want it to say?"))  # sara's example - dynamic, user input

# def cash_withdrawal(amount, accnum):
#     print(f"You have withdrawn {amount} from {accnum}")

# cash_withdrawal(100, 12345678)

# cash_withdrawal(300, 87654321)

# cash_withdrawal(int(input("How much do you want to withdraw")), input("What is your account number?"))

# drink_size = "large" 

# drink_type = "hot chocolate"

# print(f"You have ordered a {drink_size} {drink_type}") 

# drink_size = "small"

# drink_type = "mocha"

# print(f"You have ordered a {drink_size} {drink_type}") 

# drink_size = "medium"

# drink_type = "tea"

# print(f"You have ordered a {drink_size} {drink_type}") 


balance = 1000


def cash_withdraw(amount, accnum):
    global balance
    print(f"You have {balance}")
    print(f"You are withdrawing {amount} from {accnum}")
    balance = balance - amount
    print(f"You now have {balance}")

cash_withdraw(20, 12345678)
cash_withdraw(120, 12345678)

