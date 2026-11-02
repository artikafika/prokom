
person = {
    'first_name': 'Budi',
    'last_name': 'Santoso',
    'age': 20,
    'city': 'Surakarta',
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6.2 Favorite Numbers
favorite_numbers = {
    'andi': 7,
    'budi': 3,
    'citra': 21,
    'dewi': 8,
    'eka': 14,
}

print(f"Andi's favorite number is {favorite_numbers['andi']}.")
print(f"Budi's favorite number is {favorite_numbers['budi']}.")
print(f"Citra's favorite number is {favorite_numbers['citra']}.")
print(f"Dewi's favorite number is {favorite_numbers['dewi']}.")
print(f"Eka's favorite number is {favorite_numbers['eka']}.")

# 6.3 Glossary
glossary = {
    'variable': 'A name that stores a value.',
    'list': 'An ordered collection of items that can be changed.',
    'tuple': 'An ordered collection of items that cannot be changed.',
    'loop': 'A way to repeat a block of code for each item.',
    'string': 'A series of characters, such as text.',
}

print(f"variable:\n    {glossary['variable']}\n")
print(f"list:\n    {glossary['list']}\n")
print(f"tuple:\n    {glossary['tuple']}\n")
print(f"loop:\n    {glossary['loop']}\n")
print(f"string:\n    {glossary['string']}\n")

# 6.4 Glossary 2
glossary = {
    'variable': 'Menyimpan nilai.',
    'list': 'Kumpulan item berurutan.',
    'tuple': 'List yang tidak bisa diubah.',
    'loop': 'Mengulang kode.',
    'string': 'Teks.',
    'dictionary': 'Pasangan key-value.',
    'function': 'Blok kode bernama.',
    'integer': 'Bilangan bulat.',
    'boolean': 'True atau False.',
    'comment': 'Catatan yang diabaikan Python.',
}

for word, meaning in glossary.items():
    print(f"{word}: {meaning}\n")

# 6.5 Rivers
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers:
    print(river.title())

for country in rivers.values():
    print(country.title())

# 6.6 Polling
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust'}
people = ['jen', 'budi', 'edward', 'sinta']

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}!")
    else:
        print(f"{person.title()}, please take the poll!")

# 6.7 People
person_1 = {'first_name': 'Budi', 'last_name': 'Santoso', 'age': 20, 'city': 'Surakarta'}
person_2 = {'first_name': 'Sinta', 'last_name': 'Dewi', 'age': 21, 'city': 'Solo'}
person_3 = {'first_name': 'Andi', 'last_name': 'Wijaya', 'age': 19, 'city': 'Jakarta'}

people = [person_1, person_2, person_3]

for person in people:
    print(f"{person['first_name']} {person['last_name']}, "
          f"{person['age']}, {person['city']}")

# 6.8 Pets
pets = [
    {'animal': 'cat', 'owner': 'Budi'},
    {'animal': 'dog', 'owner': 'Sinta'},
    {'animal': 'bird', 'owner': 'Andi'},
]

for pet in pets:
    print(f"{pet['owner']} has a {pet['animal']}.")

# 6.9 Favorite Places
favorite_places = {
    'budi': ['Bali', 'Yogyakarta'],
    'sinta': ['Bandung'],
    'andi': ['Lombok', 'Raja Ampat', 'Bromo'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places: {', '.join(places)}")

# 6.10 Favorite Numbers
favorite_numbers = {
    'andi': [7, 21],
    'budi': [3],
    'citra': [8, 14, 30],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers: {numbers}")

# 6.11 Cities
cities = {
    'jakarta': {'country': 'Indonesia', 'population': 10_500_000,
                'fact': 'It is the capital of Indonesia.'},
    'tokyo': {'country': 'Japan', 'population': 14_000_000,
              'fact': 'It has the busiest crossing in the world.'},
    'paris': {'country': 'France', 'population': 2_100_000,
              'fact': 'It is home to the Eiffel Tower.'},
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")

# 6.12 Extensions
people = [
    {'name': 'Budi', 'age': 20, 'hobby': 'football'},
    {'name': 'Sinta', 'age': 21, 'hobby': 'painting'},
    {'name': 'Andi', 'age': 19, 'hobby': 'gaming'},
]

for person in people:
    print(f"{person['name']} ({person['age']}) likes {person['hobby']}.")


