text = input()
for i in text:
    if i.isalpha():
        print("vowel" if i in 'aeiou' else "consonant")
    else:
        break
