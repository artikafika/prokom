# 2-1. Simple Message
message = "Halo, ini pesan pertama saya!"
print(message)

# 2-2. Simple Messages
message = "Belajar Python itu menyenangkan."
print(message)

message = "Sekarang saya mengganti isi variabel dengan pesan baru."
print(message)

# 2-3. Personal Message
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

# 2-4. Name Cases
name = "ada lovelace"

print(name.lower())
print(name.upper())
print(name.title())

# 2-5. Famous Quote
print('Alan Kay once said, "The best way to predict the future is to invent it."')

# 2-6. Famous Quote 2
famous_person = "Alan Kay"
message = f'{famous_person} once said, "The best way to predict the future is to invent it."'

print(message)

# 2-7. Stripping Names
name = "\t Eric Matthes \n"

print(name)           # whitespace di awal dan akhir terlihat
print(name.lstrip())  # hapus whitespace di kiri
print(name.rstrip())  # hapus whitespace di kanan
print(name.strip())   # hapus whitespace di kedua sisi

# 2-8. File Extensions
filename = 'python_notes.txt'

print(filename.removesuffix('.txt'))

# 2-9. Number Eight
print(5 + 3)
print(10 - 2)
print(4 * 2)
print(16 / 2) 

# 2-10. Favorite Number
favorite_number = 8
message = f"My favorite number is {favorite_number}."

print(message)

# 2-11. Adding Comments
# Nama: Budi
# Tanggal: 1 November 2026
# Program ini mencetak sebuah nama dalam huruf kecil, huruf besar, dan title case.

name = "ada lovelace"

print(name.lower())   # semua huruf kecil
print(name.upper())   # semua huruf besar
print(name.title())   # huruf pertama tiap kata jadi kapital

# Nama: Budi
# Tanggal: 1 November 2026
# Program ini menyimpan angka favorit dalam variabel lalu menampilkannya dalam sebuah pesan.

favorite_number = 7
message = f"My favorite number is {favorite_number}."

print(message)

