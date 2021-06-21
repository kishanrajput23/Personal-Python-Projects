user_input = input("Enter your sentence ")

text = user_input.split()

acronym = ""

for i in text:
    acronym += i[0].upper()

print(acronym)