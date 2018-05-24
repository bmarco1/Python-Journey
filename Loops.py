for i in range(1,11):
    print (i)


i = 1
while i <= 10:
    print (i)
    i += 1

a = 10
b = 20
if a < b:
    print ("{} is less than {}".format(a,b))
elif a == 20:
    print ("{} is equal to {}".format(a,b))
else:
    print ("{} is greater than {}".format(a,b))

def fib(num):
    a,b = 0,1
    for i in range (0, num):
        yield "{}: {}".format(i+1, a)
        a, b = b, a + b

for item in fib(10):
    print (item)


for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print ("FizzBuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)

a, b = 0, 1
for i in range(0, 10):
    print (a)
    a, b = b, a + b

import random

secretNumber = random.randint(1,45)
print ("I am thinking of a number between 1 and 45.")

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")

    elif guess > secretNumber:
        print("Your guess is too high.")

    else:
        break
if guess == secretNumber:
    print ("Good Job! You guessed my number in " + str(guessesTaken) +" guesses!")
else:
    print ("Nope. The number I was thinking of was " + str(secretNumber))
