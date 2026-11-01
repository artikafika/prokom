# 3.1 names
names = ["Andi", "Budi", "Citra", "Dewi"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3.2 greetings
names = ["Andi", "Budi", "Citra", "Dewi"]

print(f"Hello, {names[0]}! Hope you're having a great day.")
print(f"Hello, {names[1]}! Hope you're having a great day.")
print(f"Hello, {names[2]}! Hope you're having a great day.")
print(f"Hello, {names[3]}! Hope you're having a great day.")

# 3.3 transportation
vehicles = ["Honda motorcycle", "Toyota car", "Yamaha scooter", "mountain bike"]

print(f"I would like to own a {vehicles[0]}.")
print(f"I would like to own a {vehicles[1]}.")
print(f"I would like to own a {vehicles[2]}.")
print(f"I would like to own a {vehicles[3]}.")

#  3.4 guest_list
guest_list = ["Albert Einstein", "Ada Lovelace", "Soekarno"]

print(f"Dear {guest_list[0]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[1]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[2]}, I would be honored if you would join me for dinner.")

# 3.5 changing guest list
guest_list = ["Albert Einstein", "Ada Lovelace", "Soekarno"]

print(f"Dear {guest_list[0]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[1]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[2]}, I would be honored if you would join me for dinner.")

print(f"\n{guest_list[1]} can't make it to the dinner.\n")

guest_list[1] = "Marie Curie"

print(f"Dear {guest_list[0]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[1]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[2]}, I would be honored if you would join me for dinner.")

# 3.6 more guests
guest_list = ["Albert Einstein", "Marie Curie", "Soekarno"]

print("Good news, I found a bigger dinner table!\n")

guest_list.insert(0, "Nikola Tesla")    # di awal list
guest_list.insert(2, "Kartini")         # di tengah list
guest_list.append("Isaac Newton")       # di akhir list

print(f"Dear {guest_list[0]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[1]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[2]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[3]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[4]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[5]}, I would be honored if you would join me for dinner.")

# 3.7 shrinking guest list
guest_list = ["Nikola Tesla", "Albert Einstein", "Kartini",
              "Marie Curie", "Soekarno", "Isaac Newton"]

print("Sorry, my new dinner table won't arrive in time. "
      "I can only invite two people for dinner.\n")

# Hapus tamu satu per satu sampai tersisa dua
popped_guest = guest_list.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

print()

# Dua tamu yang masih diundang
print(f"Dear {guest_list[0]}, you are still invited to dinner.")
print(f"Dear {guest_list[1]}, you are still invited to dinner.")

# Kosongkan list dengan del
del guest_list[0]
del guest_list[0]

print(f"\n{guest_list}")

# 3.8 seeing the world
locations = ["Japan", "Iceland", "Brazil", "Egypt", "New Zealand"]

print("Original order:")
print(locations)

print("\nsorted() alphabetical:")
print(sorted(locations))
print("Still original:")
print(locations)

print("\nsorted() reverse alphabetical:")
print(sorted(locations, reverse=True))
print("Still original:")
print(locations)

locations.reverse()
print("\nAfter reverse():")
print(locations)

locations.reverse()
print("After reverse() again:")
print(locations)

locations.sort()
print("\nAfter sort():")
print(locations)

locations.sort(reverse=True)
print("After sort(reverse=True):")
print(locations)

# 3.9 dinner guests
guest_list = ["Albert Einstein", "Ada Lovelace", "Soekarno"]

print(f"Dear {guest_list[0]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[1]}, I would be honored if you would join me for dinner.")
print(f"Dear {guest_list[2]}, I would be honored if you would join me for dinner.")

print(f"\nI am inviting {len(guest_list)} people to dinner.")

# 3.10 every function
mountains = ["Everest", "K2", "Kilimanjaro", "Fuji"]
print(f"Start: {mountains}")

mountains.append("Semeru")
print(f"append(): {mountains}")

mountains.insert(0, "Rinjani")
print(f"insert(): {mountains}")

mountains.remove("K2")
print(f"remove(): {mountains}")

popped_mountain = mountains.pop()
print(f"pop() removed {popped_mountain}: {mountains}")

del mountains[0]
print(f"del: {mountains}")

print(f"sorted() (temporary): {sorted(mountains)}")
print(f"Original unchanged: {mountains}")

mountains.sort()
print(f"sort(): {mountains}")

mountains.reverse()
print(f"reverse(): {mountains}")

print(f"len(): {len(mountains)} mountains in the list")