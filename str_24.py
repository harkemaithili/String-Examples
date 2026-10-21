text = input("Enter a string: ")
digits = ""

for ch in text:
    if ch.isdigit():
        digits = digits + ch

print("Digits:", digits)