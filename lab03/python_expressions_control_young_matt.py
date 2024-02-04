#Matt Young Lab 3 Part 2

#booleans
print(f"Is 50 < 5: {50 < 5}")
print(f"Does 3 = 3: {3 == 3}")
print(f"Does 5 = 7: {5 == 7}")
print(f"Is 37 > 12: {37 > 12}")

#boolean conversion
print(f"This will be a 0: {int(7 == 6)}")
print(f"This will be a 1: {int(3 >= 3)}")

#literals and variables
name = "Ethelred"
age = 7
print(f"a: {777}") #integer literal
print(f"b: {"Example"}") #string literal
print(f"c: {True}") #boolean literal
print(f"d: {name}") #string variable
print(f"e: {age}") #integer variable

#operation precedence
print(5 + 6 - 7)
print(5 - 6 + 7)
print(18 / 2 + 1)
print(18 + 1 / 2)

#boolean operators
name = "Edward"
print("Is my name Edward: ", name == "Edward")
print("Is my name Alfred: ", name == "Alfred")
print("Name check: ", name)


print(f"Comparing two strings: {"abc" > "abd"}")
print(f"Comparing two numbers: {18 > 19}")

num1 = 7
num2 = 10
print(f"Comparison operator: {num1} is greater than {num2}" if num1 > num2 else "False")
print(f"Comparison operator: {num1} is less than {num2}" if num1 < num2 else "False")
print(f"Comparison operator: {num1} is greater than or equal to {num2}" if num1 >= num2 else "False")
print(f"Comparison operator: {num1} is less than or equal to {num2}" if num1 <= num2 else "False")

tautology = True
contradiction = False
print(f"Logical AND test: {tautology and contradiction}")
print(f"Logical OR test: {tautology or contradiction}")
print(f"Logical XOR test: {tautology ^ contradiction}")
print(f"Logical NOT test: {not tautology}")
print(f"Bitwise AND test: {tautology & contradiction}")
print(f"Bitwise OR test: {tautology | contradiction}")

#if statments
spoons = 17

if spoons > 15:
    print("Too many spoons.")
elif spoons > 7:
    print("That's enough spoons.")
else:
    print("Not enough spoons.")

spoons = 12

if spoons > 15:
    print("Too many spoons.")
elif spoons > 7:
    print("That's enough spoons.")
else:
    print("Not enough spoons.")

spoons = 3

if spoons > 15:
    print("Too many spoons.")
elif spoons > 7:
    print("That's enough spoons.")
else:
    print("Not enough spoons.")

#ternary operators
cats = 12
print("Get more cats." if cats < 7 else "You're good on cats.")
cats = 4
print("Get more cats." if cats < 7 else "You're good on cats.")

#while loop
mines = 10
while mines > 0:
    print("Place mine.")
    mines -= 1

#for loop
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for color in rainbow:
    print(color)

for i in range(3):
    print(i)