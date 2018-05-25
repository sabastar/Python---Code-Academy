# Write a function that checks if number x is divisible by 2

def is_even(x):
  if x%2 == 0:
    return True
  else:
    return False

# ******* IS_INT ************
# Note: here a number with a decimal 0 is also an integer > ex. 7.0

# define a function is_int that takes a number x
def is_int(x):
  # return True if number is an integer and False otherwise
  # The difference between a number and that same number rounded is greater than zero
  if (x-round(x)) >= 0:
    return True
  else:
    return False
# ****** DIGIT_SUM *********
# Summing the digits of a number
# Takes positive int n and returns sum of all that number's digits
# Ex: 1234 should return 10 (assume always positive number)

def digit_sum(n):
  # convert n to string and iterate over and back into int
  sum = 0
  #strg = str(n)
  for i in str(n):
    sum += int(i)
  return sum

# ***** FACTORIAL *******
# Factorial of pos int x > multiply all ints from 1 to x
# Ex: factorial(4) = 4*3*2*1
def factorial(x):
  # calculate and return the factorial of number x 
  if x == 0:
    return 1
  else:
    return x*factorial(x-1)
  
print factorial(4)

# **** ANTI-VOWEL ******

# Define a function that takes a string input and returns it with all the vowels removed
def anti_vowel(text):
  new = ''
  for i in text:
    if i not in "aeiouAEIOU":
      new += i 
  return new

print anti_vowel("Hey You!")

# 
