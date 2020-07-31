scores = input().split()
count1 = 0
count2 = 0
for i in scores:
    if i == "I":
        count1 += 1
    elif i == "C":
        count2 += 1
    if count1 == 3:
        print("Game over", count2, sep="\n")
        break
if count1 < 3:
    print("You won", count2, sep="\n")
