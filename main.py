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

print("\nInput String :", str)
print("\n")
print('###############')
print("\n")
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

if(a > b):
  print("a is greater than b.")
else:
  if(a == b):
    print("a equal to b")
  else:
    print("b is greater than a.")

if(a > b):
  print("a is greater than b.")
elif a == b:
  print("a equal to b")
else:
  print("b is greater than a.")


if(a > b):
  pass
else:
  pass

