# randomness - random library
# my number 
# computers number

# while my num doesnt equal computers num
# numbers don't match

#if my num = computers number
# well done code finished

import random 

my_num = 13

rand_num = random.randint(1,50)

counter = 0
while my_num != rand_num:
    print(f" My number {my_num} does not equal the randomly generated number {rand_num}")
    counter +=1
    rand_num = random.randint(1,50)
else:
    print(f"The two numbers matched! and it took {counter+1} times")