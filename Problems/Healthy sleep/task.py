sleep_min = int(input())
sleep_max = int(input())
sleep_hour = int(input())
if sleep_hour > sleep_max:
    print("Excess")
elif sleep_hour < sleep_min:
    print("Deficiency")
else:
    print("Normal")
