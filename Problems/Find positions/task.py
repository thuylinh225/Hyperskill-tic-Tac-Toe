# put your python code here
data1 = str(input()).split()
data2 = str(input())
pos = []
for position, item in enumerate(data1):
    if item == data2:
        pos.append(position)
if len(pos) != 0:
    print(" ".join([str(i) for i in pos]))
else:
    print("not found")
