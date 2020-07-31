data = str(input())
array = []
for i in data[:-1]:
    cal = (int(i) + int(i) + 1) / 2
    array.append(cal)
print(array)
