# Lab 3: For Loops Practice

## Instructions


#In this lab, we will practice using for-loops and strings. Each problem will require you to consider how to use for-loops to solve the problem. You will need to think about how many times you need to loop, what you need to do each time you loop, and how to use the loop variable to solve the problem. At the beginning, you'll need to ask the user which problem they want to run. You'll then need to use a conditional statement to run the correct problem.

import random

print("Options: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
run = input("Enter the problem you want to run: ")
run = int(run)

## Problems

#1. Write a program that prints out the numbers 1 to 1000. (+5 points)

if run == 1:
    print("Running problem 1...")
    for count in range(1001):
        print(count)

#2. Write a program that prints out the odd numbers between 1 and 1000. (+5 points)

if run == 2:
    for count in range(1,1001,2):
        print(count)

#3. Write a program that prints out the numbers between 0 and 1000 that are divisible by 3. (+10 points)
        
if run == 3:
    for count in range(0,1001,2):
        if count % 3 == 0:
            print(count)


#4. Write a program that prints out the numbers between 1 and 1000 that are divisible by 3 or 5. (+10 points)

if run == 4:
    for count in range(0, 1001,2):
        if count % 3 == 0 or count % 5 == 0:
            print(count)

#5. Write a program that asks the user to enter a number and prints out all the numbers between 1 and that number that are divisible by 11 or 13. The number entered should be greater than 200. (+10 points) Extra credit if the programs asks again if the number is less than 200. (+5 points)

if run == 5:
    while True:
        user = input("Enter a number equal to or greater than 200:")
        user = int(user)
        if user >= 200:
            for count in range(0, user):
                if count % 11 == 0 or count % 13 == 0:
                    print(count)
            break
        else:
            print("Number must be equal to or greater than 200. Please enter a valid number.")

#6. Write a program that prints out each letter of a string line by line (+5 points)

if run == 6:        
    string = input("Enter a word: ")
    for l in range(len(string)):
        print(string[l])

#7. Write a program that asks the user to enter a string and outputs every second letter. The string must be more than 10 letters long. (+10 points)

if run == 7:
    while True:
        string = input("Enter a string of text more than 10 letters long: ")
        if len(string) >= 10:
            for l in range(2, len(string), 2):
                print(string[l])
                break
        if len(string) < 10:
            input("The string of text you input is less than 10 characters. Please enter a string of text:")
#8. Write a program that rolls 1000 dice and prints out the number of times each number was rolled. (+15 points)

ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

if run == 8:
    for roll in range(0, 1000):
        dice = random.randint(1,6)
        if dice == 1:
            print("you rolled a 1")
            ones += 1
        elif dice == 2:
            print("you rolled a 2")
            twos += 1
        elif dice == 3:
            print("you rolled a 3")
            threes += 1
        elif dice == 4:
            print("you rolled a 4")
            fours += 1
        elif dice == 5:
            print("you rolled a 5")
            fives += 1
        elif dice == 6:
            print("you rolled a 6")
            sixes += 1
    print(f"After 100 dice rolls, we rolled {ones} 1s, {twos} 2s, {threes} 3s, {fours} 4s, {fives} 5s, and {sixes} 6s")

#9. Write a program that checks if a given number is a prime number. A prime number is a number that is only divisible by 1 and itself. The user enters a number and the programs prints out whether the number is a prime number or not. (+15 points)

if run == 9:
    user = int(input("Enter a number to check if it's a prime number: "))
    prime = True
    for i in range(2, int(user**0.5) + 1):
        if user % i == 0:
            prime = False
            break
    if user > 1 and prime:
        print(f"The number {user} is indeed a prime number!")
    else:
        print(f"The number {user} is not a prime number...")

#10. Write a program that prints out the prime numbers less than 1000. (+20 points)

if run == 10:
    for num in range(2, 1001):
        prime = True
        for primes in range(2, int(num**0.5) + 1):
            if num % primes == 0:
                prime = False
                break

        if prime:
            print(num)