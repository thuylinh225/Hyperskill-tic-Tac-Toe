col = int(input())
row = int(input())
if col in (1, 8):
    if row in (1, 8):
        print(3)
    else:
        print(5)
elif col not in (1, 8):
    if row not in (1, 8):
        print(8)
    else:
        print(5)
