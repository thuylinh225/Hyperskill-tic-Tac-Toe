data = input()
remove_char = ",.!?"
for char in remove_char:
    data = data.replace(char, "")
print(data.lower())
