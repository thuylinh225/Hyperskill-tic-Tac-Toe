biggest = 0
name = ""
while True:
    text = input().split(" ")
    if text[0] == "MEOW":
        break
    if int(text[1]) > biggest:
        biggest = int(text[1])
        name = text[0]
print(name)
