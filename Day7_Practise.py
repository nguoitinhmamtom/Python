#Exercise 01:
#Create a function named cube that takes a number and returns its cube
numbers = [2,5,3]
cube = list(map(lambda x: x**3,numbers))
print(cube)

#Exercise 02:
#Write a function celsius_to_fahrenheit that takes a temperature in Celsius and converts it to Fahrenheit. The formula is:
#Fahrenheit = (Celsius × 9/5) + 32.
Celsius = [32,40,36.7,37]
celsius_to_fahrenheit = list(map(lambda x: (x*9/5)+32, Celsius))
print(celsius_to_fahrenheit)

#Exercise 03:
#Create a function is_divisible_by_three that takes a number as input and returns True if the number is divisible by 3, and False otherwise.
divisible_by_three = lambda x: True if x%3==0 else False
divisible_by_three(6)

#Exercise 04:
#Create a function circle_area that takes the radius of a circle and returns the area. (Use the formula: Area = π * radius^2).
import math
circle_area = lambda x: math.pi * x**2
circle_area(3.7)

#Exercise 05:  Write a function that removes duplicates from a list
#Write a function remove_duplicates that takes a list as input and returns a new list with all duplicates removed.
lst = [4,89,90,56,89,45,33,22,56]
remove_duplicates = list(dict.fromkeys(lst)) #hàm loại bỏ duplicate trong list
print(remove_duplicates)

#Exercise 06: Write a function to find the sum of squares of numbers in a list
#Create a function sum_of_squares that takes a list of numbers and returns the sum of the squares of those numbers.
from functools import reduce
lst = [2,5,11,10]
squares_of_lst = list(map(lambda x: x**2,lst))
sum_of_squares = reduce(lambda a,b: a+b, squares_of_lst)
print(sum_of_squares)

#Exercise 07:
#Write a program to generate and print another tuple whose values are even numbers in the given tuple (20,1,8,6,4,9,5,9,3,8,7).
my_tuple = (20,1,8,6,4,9,5,9,3,8,7)
the_even_numbers = tuple(filter(lambda x: True if x%2==0 else False, my_tuple))
print(the_even_numbers)

#Exercise 08:
#Write a function count_character that takes a string and a character as arguments, and returns the number of times that character appears in the string.
def my_string(s,c):
  count = 0
  for i in range(len(s)):
    if (s[i]) == c:
      count = count + 1
  return count
my_string('IcouldlovePythonforfourdays','o')

#Exercise 09:
#Write a Python function find_roots(a, b, c) that finds the real roots of a quadratic equation ax^2+bx+c=0.
import cmath #import module cmath để làm việc với số phức
def find_root(a,b,c):
  if a == 0:
    if b == 0:
      return ()
    else:
      return(-c/b)
  if a != 0:
    delta = b**2 - 4*a*c
    if delta > 0:
      root1 = (-b + round(delta**0.5))/2*a
      root2 = (-b - round(delta**0.5))/2*a
      return (root1,root2)
    elif delta == 0:
      root = -b/2*a
      return (root)
    else:
      return ()
print(find_root(1,-49,-50))

#Exercise 10:
#Write a Python function process_message(message)  that takes a string containing words and spaces as input. The function should:
#Remove all duplicate words from the message. (using split())
#Sort the words alphabetically. (using sort())
#Return a new string with the processed words (separated by spaces) (using join)
def process_message(message):
  words = message.lower().split()
# code in  Python được thực hiện từ trái sang phải
  unique_words = sorted(list(set(words)))
  processed_message = " ".join(unique_words)
# để dùng được lệnh join phải có một list hoặc tuple để gộp các phần tử
# "" dùng để xác định mỗi phần tử trong list hay tuple được gộp lại cách nhau bằng dấu cách dấu phẩy  - hyphen, /\slash, — dash, _ underline/undersroce
# .join() gom nhóm các phần tử trong list, tuple thành một chuỗi string được ngăn cách nhau bằng dấu được xác định ở dấu "" quotation marks
  return words, unique_words, processed_message
process_message('I could live Python four seasons, senven days')

#Exercise 11:
#Write a Python function count_characters_and_digits(message: str) -> Tuple[int, int] that takes a message as input and returns:
#The number of alphabetic characters (letters) in the message.
#The number of digits (0-9) in the message.
#The function should not count spaces or any non-alphabetic/non-digit characters.
def count_characters_and_digits(message):
  alp = 0
  dig = 0

  for x in message:
    if x.isalpha():
      alp += 1
    elif x.isdigit():
      dig += 1

  return alp, dig
count_characters_and_digits('I could love Python for 7 days 4 seasons')

#Exercise 12:
#Write a Python function count_upper_lower(message: str) -> Tuple[int, int] that:
#Takes a string message as input.
#Returns a tuple containing:
#The number of upper-case letters in the message.
#The number of lowercase letters in the message.
#The function should ignore spaces and non-alphabetic characters.
def count_upper_lower(message):
  
    upper_count = 0 
    lower_count = 0 
     
    for i in message: 
        if i.isupper(): 
            upper_count += 1 
        elif i.islower(): 
            lower_count += 1 
             
    return upper_count, lower_count 
count_upper_lower('I could love Python for 7 days 4 seasons')
