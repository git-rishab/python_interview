# a. Write a Python program that takes a string input from the user and prints out the reversed string.

# For instance, if a user inputs: "Python is fun"

# Expected output:
# nuf si nohtyP


def reverse(str):
  res = ""
  length = len(str)
  for i in range(length - 1, -1, -1):
    res += str[i]
  return res


print(reverse("Python is fun"))
