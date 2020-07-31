score = int(input())
max_ = int(input())
grade = (score / max_) * 100
if grade < 60:
    print("F")
elif grade < 70:
    print("D")
elif grade < 70:
    print("D")
elif grade < 80:
    print("C")
elif grade < 90:
    print("B")
else:
    print("A")
