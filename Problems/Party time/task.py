lst = []
while True:
    name = input()
    if name == ".":
        break
    lst.append(name)
print(lst, len(lst), sep="\n")
