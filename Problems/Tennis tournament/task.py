number = int(input())
names = [str(input()) for line in range(number)]
count = 0
new = []
for name in names:
    if "win" in name:
        count += 1
        hint = name.split(" ")[0]
        new.append(hint)
print(new)
print(count)
