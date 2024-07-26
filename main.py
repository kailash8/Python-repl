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


arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = rotate_array(arr, k)
print(f"Input array: {arr}")
print(f"Rotated array: {rotated_arr}")
