total = 0
square = 0
while True:
    num = int(input())
    total += num
    square += (num ** 2)
    if total == 0:
        print(square)
        break
