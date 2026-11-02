# 4.1 pizza
pizzas = ["pepperoni", "margherita", "hawaiian", "four cheese"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("\nI really love pizza!")

# 4.2 animals
animals = ["cat", "rabbit", "hamster"]

for animal in animals:
    print(f"A {animal} would make a great pet.")

print("\nAny of these animals would make a great pet!")

# 4.3 counting to twenty
for number in range(1, 21):
    print(number)

# 4.4 one million
numbers = list(range(1, 1_000_001))

for number in numbers:
    print(number)

# 4.5 summing a million
numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4.6 odd numbers
odd_numbers = list(range(1, 20, 2))

for number in odd_numbers:
    print(number)

# 4.7 threes
threes = list(range(3, 31, 3))

for number in threes:
    print(number)

# 4.8 cubes
cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)

for cube in cubes:
    print(cube)

# 4.9 cube comprehension
cubes = [value ** 3 for value in range(1, 11)]

print(cubes)

# 4.10 slices
pizzas = ["pepperoni", "margherita", "hawaiian", "four cheese", "BBQ chicken", "veggie"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("\nI really love pizza!")

print("\nThe first three items in the list are:")
print(pizzas[:3])

print("\nThree items from the middle of the list are:")
print(pizzas[1:4])

print("\nThe last three items in the list are:")
print(pizzas[-3:])

# 4.11 my pizzas your pizzas
pizzas = ["pepperoni", "margherita", "hawaiian", "four cheese"]

friend_pizzas = pizzas[:]

pizzas.append("BBQ chicken")
friend_pizzas.append("veggie")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4.12 foods
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)