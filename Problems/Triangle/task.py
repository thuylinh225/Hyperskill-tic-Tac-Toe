num = int(input())
max_len = num * 2 - 1
for i in range(1, num + 1):
    print(("#" * ((i * 2) - 1)).center(max_len))
