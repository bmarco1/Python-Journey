magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ' that was a trick!')
    print("I can't wait to see your next trick, " + magician.title() +".\n")
    print("Thank you, everyone. That was a great magic show!")

for value in range(1,9):
    print(value)


squares = []
for value in range(1,22):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

dimension = (200,50)
print('Original dimension:')
for dimension in dimension:
    print(dimension)
r
dimension = (400,200)
print("\nModified dimension:")
for dimension in dimension:
    print(dimension)

    answer = 42

    if answer != 57:
        print ("That is the incorrect answer")

car = 'subaru'
print("Is car == 'subaru'? I predict True")

print("nIs car == 'audi'? I predict false")
print(car == 'audi')

requested_toppings = ['mushrooms', 'extra_cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra_cheese' in requested_toppings:
    print("Adding extra_cheese")
print("\nFinished making your pizza!")

alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    points = 5
else:
    points = 10
print("Your score is " + str(points))

age = 12
if age <4:
    price = 0
elif age <18:
    price = 5
elif age <65:
    price = 10
elif age >= 65:
    price = 5
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

age = 3
if age <2:
    stage = 'baby'
elif age <4:
    stage = 'toddler'
elif age <=13:
    stage = 'teenager'
elif age >13:
    stage = 'adult'
elif age >65:
    stage = 'elder'
print("You are a " + str(stage))

alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
