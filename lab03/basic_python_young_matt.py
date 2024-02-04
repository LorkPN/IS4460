#Matt Young Lab 3 Part 1

#literals
print("Hello World!")
print(17.8)

#variables and variable names
Name = "Henry"
name = "Robert"

print(Name)
print(name)

pi = 3.14159
print(pi)

#concatenation
print("Long live king " + Name + ", may he reign forever.")
print(f"Hopefull he lasts longer than king {name}.")

#variable typing
id = "u1285039"
id = 1285039
print(str(id)[0:5])

#function definition
def factorial(a):
  if(a == 1):
    return 1
  else:
    return a * factorial(a - 1)

print(factorial(7))

#function parameters
def power(a, b):
  result = 1
  for i in range(b):
    result *= a
  return result

print(power(2, 5))
print(power(b=2, a=5))

#variable scopes
userName = "Harold"

def say_hello():
  userName = "William"
  print(userName)

say_hello()
print(userName)