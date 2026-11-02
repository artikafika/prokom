# 7.1 Rental Car
car = input("What kind of rental car would you like? ")

print(f"Let me see if I can find you a {car.title()}.")

# 7.2 Restaurant Seating    
people = input("How many people are in your dinner group? ")
people = int(people)

if people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

# 7.3 Multiples of Ten
number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

# 7.4 Pizza Toppings
prompt = "\nEnter a pizza topping (or 'quit' to finish): "

topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")

# 7.5 Movie Tickets
prompt = "\nHow old are you? (enter 'quit' to finish) "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

# 7.6 Three Exits
prompt = "\nEnter a pizza topping (or 'quit' to finish): "

topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")

# variable active is used to control the loop
prompt = "\nEnter a pizza topping (or 'quit' to finish): "

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")

# variable break is used to exit the loop
prompt = "\nEnter a pizza topping (or 'quit' to finish): "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")

# 7.7 Infinites
while True:
    print("This loop never ends...")

# 7.8 Deli
sandwich_orders = ['tuna', 'egg', 'chicken', 'veggie']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

# 7.9 No Pastrami
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'egg', 'veggie', 'pastrami']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

# 7.10 Dream Vacation
responses = {}

polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place

    repeat = input("Would another person like to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name} would like to visit {place}.")


