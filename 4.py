text = input("Enter a string: ")

seen = ""

for character in text:
    if character in seen:
        print("First repeated character:", character)
        break
    seen = seen + character
    