lst = []
while True:
    num = input()
    if num != ".":
        lst.append(float(num))
    else:
        break
print(min(lst))
