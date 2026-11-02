# 5.1 conditional tests
car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')

print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')

print("\nIs car != 'toyota'? I predict True.")
print(car != 'toyota')

age = 20

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs age >= 18 and age <= 25? I predict True.")
print(age >= 18 and age <= 25)

print("\nIs age > 30 or age < 10? I predict False.")
print(age > 30 or age < 10)

print("\nIs 'sub' in car? I predict True.")
print('sub' in car)

print("\nIs 'honda' in ['toyota', 'suzuki']? I predict False.")
print('honda' in ['toyota', 'suzuki'])

# 5.2 More conditional tests
car = 'subaru'

# Kesamaan dan ketidaksamaan string
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

# Method lower()
print("\nIs 'SUBARU'.lower() == car? I predict True.")
print('SUBARU'.lower() == car)

print("\nIs 'Audi'.lower() == 'Audi'? I predict False.")
print('Audi'.lower() == 'Audi')

# Tes numerik
age = 20

print("\nIs age == 20? I predict True.")
print(age == 20)

print("\nIs age == 21? I predict False.")
print(age == 21)

print("\nIs age != 25? I predict True.")
print(age != 25)

print("\nIs age != 20? I predict False.")
print(age != 20)

print("\nIs age > 18? I predict True.")
print(age > 18)

print("\nIs age > 20? I predict False.")
print(age > 20)

print("\nIs age < 30? I predict True.")
print(age < 30)

print("\nIs age < 20? I predict False.")
print(age < 20)

print("\nIs age >= 20? I predict True.")
print(age >= 20)

print("\nIs age >= 21? I predict False.")
print(age >= 21)

print("\nIs age <= 20? I predict True.")
print(age <= 20)

print("\nIs age <= 19? I predict False.")
print(age <= 19)

# Keyword and dan or
print("\nIs age > 18 and age < 30? I predict True.")
print(age > 18 and age < 30)

print("\nIs age > 18 and age < 20? I predict False.")
print(age > 18 and age < 20)

print("\nIs age < 18 or age > 19? I predict True.")
print(age < 18 or age > 19)

print("\nIs age < 18 or age > 25? I predict False.")
print(age < 18 or age > 25)

# Item ada di dalam list
cars = ['subaru', 'toyota', 'honda']

print("\nIs 'toyota' in cars? I predict True.")
print('toyota' in cars)

print("\nIs 'audi' in cars? I predict False.")
print('audi' in cars)

# Item tidak ada di dalam list
print("\nIs 'audi' not in cars? I predict True.")
print('audi' not in cars)

print("\nIs 'toyota' not in cars? I predict False.")
print('toyota' not in cars)

# 5.3 Alien Colors #1
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

# 5.4 Alien Colors #2
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")

# 5.5 Alien Colors #3
alien_color = 'green'   # coba juga 'yellow' dan 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

# 5.6 Stages of Life
age = 25

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

# 5.7 Favorite Fruit
favorite_fruits = ['mango', 'banana', 'apple']

if 'mango' in favorite_fruits:
    print("You really like mangoes!")

if 'banana' in favorite_fruits:
    print("You really like bananas!")

if 'apple' in favorite_fruits:
    print("You really like apples!")

if 'orange' in favorite_fruits:
    print("You really like oranges!")

if 'grape' in favorite_fruits:
    print("You really like grapes!")

# 5.8 Hello Admin
usernames = ['admin', 'jaden', 'sinta', 'budi', 'maya']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")

# 5.9 Hello Admin (No Users)
usernames = ['admin', 'jaden', 'sinta', 'budi', 'maya']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# 5.10 Checking Usernames
current_users = ['admin', 'John', 'sinta', 'Budi', 'maya']
new_users = ['JOHN', 'dewi', 'Maya', 'rudi', 'Andi']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, '{new_user}' is already taken. "
              "Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")

# 5.11 Ordinal Numbers
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")


