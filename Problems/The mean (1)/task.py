total = 0
count = 0
while True:
    num = input()
    if num != ".":
        num = int(num)
        total += num
        count += 1
    else:
        break
print(total / count)
