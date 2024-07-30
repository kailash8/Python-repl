import time

# print("Hello World. \nhello")
# print(9)
#
# a = 'string'
# b = "string"
# c = '''string'''
# d = True
# e = False
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
#
# print(type(int("2") + float("12.0")))

# user_input = input("Enter anything : ")
# print("User Input data is :", user_input)
#
# p = """
# Hi
# Me
# Here
# Hello
# I
# Me
# am
# """
#
# print(p)


def rotate_array(arr, k):
  n = len(arr)
  k = k % n
  arr = arr[n - k:] + arr[:n - k]
  return arr


'''
arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = rotate_array(arr, k)
print(f"Input array: {arr}")
print(f"Rotated array: {rotated_arr}")
'''

# p = """
# Hi
# Me
# Here
# Hello
# I
# Me
# am
# """
#
# for x in p :
#   print(x)

# Python String Methonds

str = 'all string Methods returns new values. They do NOT change the original string.'
'''
print("\nInput String :", str)
print("\n")
print('###############')
print("\n")
'''
#print(str.capitalize())
#print(str.casefold())
#p = repr(str.center(20))
#print(str.count('o'))
#print(str.encode())
#print(str.endswith('.'))
#print(str.expandtabs(2
#print(str.find("NOT"))
#print("I {} here.".format('was'))
data = {"name": "kailash", "age": 90}
#print("My name is {} and I am {} years old.".format(data["name"], data["age"]))
#print(str.index("NOT"))
#print(str.isalnum())
#print(str.islower())
#print(str.isupper())
#print(str.isspace())
arrayWords = ["I", "am", "Kailash", "Choudhary"]
listWords = ("I", "am", "Kailash", "Choudhary")

#print(" ".join(arrayWords))
#print(" ".join(listWords))
#print(str.replace(" ","=="))
#print(type(str.split()))

#for x in str.split():
#  print(x)

#print(" Kailash ")
#print(" Kailash ".strip())
#print(str.swapcase())
#print(str.upper())

a = 30
b = 30
''' 
if (a > b):
  print("a is greater than b.")
else:
  if (a == b):
    print("a equal to b")
  else:
    print("b is greater than a.")

if (a > b):
  print("a is greater than b.")
elif a == b:
  print("a equal to b")
else:
  print("b is greater than a.")

if (a > b):
  pass
else:
  pass

'''
#print(time.strftime("%H:%M:%S"))

#match - case
'''
value = 10
match value:
  case 1:
    print("its 1")
  case 2:
    print("its 2")
  case 3:
    print("its 3")
  case _:
    print("something else...")

'''


#basic
def match_example(value):
  match value:
    case 1:
      print("One")
    case 2:
      print("Two")
    case 3:
      print("Three")
    case _:
      print("Somthing else...")


'''
match_example(1)
match_example(2)
match_example(3)
match_example(4)
'''
#multiple patterns


def match_example_multiple_pattern(value):
  match value:
    case 1 | 2 | 3:
      print(f"its {value}")
    case _:
      print("Other...")


'''
match_example_multiple_pattern(1)
match_example_multiple_pattern(2)
match_example_multiple_pattern(3)
match_example_multiple_pattern(4)
'''
#variable bindings


def match_example_variable_bindings(value):
  match value:
    case 0:
      print("ZERO")
    case x:
      print(f"Got {x}")


'''
match_example_variable_bindings(0)
match_example_variable_bindings(20)
'''
#sequence pattern


def match_example_sequence_pattern(value):
  match value:
    case []:
      print("Empty list")
    case [x]:
      print(f"Single element : {x}")
    case [x, y]:
      print(f"Two elements : {x} and {y}")
    case _:
      print("Some other sequance")


'''
match_example_variable_bindings([])
match_example_variable_bindings([1])
match_example_variable_bindings([1, 2])
match_example_variable_bindings([1, 2, 3])
'''


#dictioanry pattern
def match_example_dictioanry_pattern(value):
  match value:
    case {"key": x}:
      print(f"Found key with value {x}")
    case _:
      print(f"Something else : {value}")


'''
match_example_dictioanry_pattern({"key": 1})
match_example_dictioanry_pattern({"key": "value"})
match_example_dictioanry_pattern({"key": "value", "key2": "value2"})

print("\n\n")
'''

#class patterns
'''
class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y
'''

#for loop
'''
for i in range(5):
  print(i)


numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers :
  print("So the number is : " , number)

for char in str.upper() :
  print(char)

'''
'''
matrix = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
for row in matrix:
  for element in row:
    print(element, end=" ")
  print()
else:
  print("Loop completed.")
'''
'''
# Star patterns
n = 5
print("pattern value of n : ", n)

print("\n")
for i in range(1, n + 1):
  print(i * "o")

print("\n")
for i in range(n, 0, -1):
  print('o' * i)

print("\n")
for i in range(n):
  print(' ' * (n - i - 1) + 'o' * (2 * i + 1))

print("\n")
for i in range(n, 0, -1):
  #print("iteration : " , i)
  print(' ' * (n - i) + 'o' * (2 * i - 1))

#Diamond pattern
print("\n")
for i in range(5):
  print(' ' * (n - i - 1) + 'o' * (2 * i + 1))
for i in range(n - 1, 0, -1):
  print(' ' * (n - i) + 'o' * (2 * i - 1))

print("\n")
for i in range(n):
  print(' ' * (n - 1 - i) + 'o' * (i + 1))

#Hourglass Pattern
print("\n")
for i in range(n, 0, -1):
  print(' ' * (n - i) + 'o' * (2 * i - 1))
for i in range(1, n):
  print(' ' * (n - 1 - i) + 'o' * (2 * i + 1))

#Hollow Square Pattern
print("\n")
for i in range(n):
  if i == 0 or i == n - 1:
    print('o' * n)
  else:
    print('o' + ' ' * (n - 2) + 'o')
'''

# while loops
'''
n = 5
i = 1
while i <= n:
  j = 1
  while j <= i:
    print(j, end=' ')
    j += 1
  print()
  i += 1

print("==================")

n = 9
i = 1
while i <= n:
  j = 1
  while j <= i:
    print(i, end=' ')
    j += 1
  print()
  i += 1

print("==================")
'''

# break and continue

print("Break \n")
for i in range(10):
  if i == 5:
    break
  print(i)

print("\nContinue  \n")
for i in range(10):
  if i % 2:
    continue
  print(i)
# functions
