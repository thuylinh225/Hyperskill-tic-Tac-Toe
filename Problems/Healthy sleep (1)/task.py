min_time = int(input())
max_time = int(input())
sleep_time = int(input())
if sleep_time < min_time:
    print("Deficiency")
elif sleep_time > max_time:
    print("Excess")
else:
    print("Normal")
