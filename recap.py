# print("hello world")

# #this will not execute, but we can see it

# print("what data type is this")
# print("12345")

# print(12345)

# print(123.45)

# print(None)

# print(True)
# print(False)

# # object.method()

# print("hello".upper())

# print("HELLO")

# print(len("Hello"))

# print("123456".isnumeric())

# print("how do I capitAlise every starting letter".title())

# print("I am going to use .split()".split())

# print("This is another interesting split".split("i"))

# print("All aro"+ "All around the world".upper()[7]+ "nd the world")

print("All around the world".upper()[7])

print("All around the world"[7].upper())


# this is a variable - we will cover these shortly!
example = "testingstring is here"

#take the string and show us the starting character to one before the 7th
# then add the 7th
# then get the 8th and continue to the end
print(example[0:7] + example[7].upper() + example[8:])