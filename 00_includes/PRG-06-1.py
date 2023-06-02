import random

#Assign an empty list to a variable: 
random_numbers = []
for i in range(5):
    #Add 5 random numbers to the variable list:
    random_numbers.append(random.randint(0, 99))
#print the random number list.
for num in random_numbers:
    print(num)