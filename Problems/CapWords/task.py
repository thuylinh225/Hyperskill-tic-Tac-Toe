data = input().lower()
word = [word[0].upper() + word[1:] for word in data.split("_")]
print("".join(word))
