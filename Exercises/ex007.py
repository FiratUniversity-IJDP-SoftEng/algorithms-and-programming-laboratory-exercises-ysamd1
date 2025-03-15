# Your Student ID:220543009
# Your Name and Surname:Yaşam Doğa Çevik

text = input("Enter a string: ")

char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print("\nCharacter frequencies:")
for char in sorted(char_count):
    print(f"{char}: {char_count[char]}")
