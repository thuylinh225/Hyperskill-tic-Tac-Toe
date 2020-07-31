text = input().split(" ")
for word in range(1, len(text)):
    text[word] = text[word].capitalize()
print("".join(text))
