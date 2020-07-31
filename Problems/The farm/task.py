amount = int(input())
if amount < 23:
    print("None")
elif amount < 678:
    number = amount // 23
    print(number, "chickens" if number > 1 else "chicken")
elif amount < 1296:
    number = amount // 678
    print(number, "goats" if number > 1 else "goat")
elif amount < 3848:
    number = amount // 1296
    print(number, "pigs" if number > 1 else "pig")
elif amount < 6769:
    number = amount // 3848
    print(number, "cows" if number > 1 else "cow")
else:
    number = amount // 6769
    print(number, "sheep")
