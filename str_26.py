text = input("Enter a string: ")
ch = input("Enter a character: ")

if ch in text:
    print("First occurrence index:", text.find(ch))
    print("Last occurrence index:", text.rfind(ch))
else:
    print("Character not found")