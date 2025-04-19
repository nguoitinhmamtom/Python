#Exercise 1
#Write a program to list all numbers that are divisible by 5 not divisible 13, between 1900 and 2030 (both included).
#All numbers are displayed in a comma-separated sequence on a single line.
b = [i for i in range(1900,2031) if i%5 == 0 if i%13 != 0]
print(b)

#Exercise 2
#Find and print the min and max of (20, 18, 23, 4, 8, 3, 19, 16, 45, 25).
lst = [20, 18, 23, 4, 8, 3, 19, 16, 45, 25]
print(min(lst))

#Exercise 3
#Find all square numbers smaller than 2030.
a = [i for i in range(0,2030) if i**2 < 2030]
print(a)

#Exercise 4
#Find all pairs of numbers with an even product
#Description:
#Given two lists of integers list1 and list2.
#Find all pairs of numbers (x,y) that x*y is even.
#Skip pairs if either number is odd (use continue).
#Stop immediately after finding 5 matching pairs (use break).
list1 = [43,62,96]
list2 = [92,53,560]
count = 0
c = []
for x in list1:
  for y in list2:
    if (x * y) % 2 == 0:
      count = count + 1
      c.append((x,y))
      if count == 5: #dòng lệnh có thể không cần vì vòng lặp y sẽ quay để lấy hết toàn bộ cặp xy
        break
    if count == 5: #nếu bỏ break trong vòng lặp y thì vòng lặp x sẽ dừng tại cặp xy count=5
      break
print(c)

#Exercise 5
#Find and print out even numbers in (20, 18, 23, 4, 8, 3, 19, 16, 45, 25). Finally, print the sum of these even numbers.
d = [20, 18, 23, 4, 8, 3, 19, 16, 45, 25]
print(sum(d))

#Exercise 6
#Count the number of pairs divisible by 3
#Description:
#Given two lists of integers list1 and list2.
#Count all pairs of numbers (x,y)(x, y)(x,y) such that x+yx + yx+y is divisible by 3.
#Print the total number of such pairs.
lst1 = [56,88,33,21,67]
lst2 = [64,29,64,185,40]
e = []
for x in lst1:
  for y in lst2:
    if (x + y * x + y * x + y) % 3 == 0:
      e.append((x,y))
print(e)

#Exercise 7
#Write a program to calculate the sum of powers of 2 which are smaller than 200.
f = [i for i in range(0,201) if i**2 < 200]
print(sum(f))

#Exercise 8
#Write a program to find all factor numbers of 2020.
g = 2020
factor_numbers = [i for i in range (1,g + 1) if g%i==0]
print(factor_numbers)

#Exercise 9
#Write a program to find and print all prime number smaller than 100.
h = [] #tạo tập rỗng
for i in range(1,101): #tạo vòng lặp từ với i = 1 đến i = 100
  num = 0 #tạo biến num gán cho giá trị bằng 0
  for j in range(2,int(i**0.5)+1): #tạo vòng lặp với j = 2 đến j = i**0.5
    if i%j == 0:
      num = num + 1
      break
  if i!=1 & num==0:
    h.append(i)
print(h)

#Exercise 10
#Write a program to find and print all Fibonacci number smaller than 100.
#Số Fibonacci là một số trong dãy Fibonacci, được xác định bởi công thức:
#F(0) = 0, F(1) = 1
#F(n) = F(n-1) + F(n-2) (với n ≥ 2)
#Dãy Fibonacci bắt đầu như sau: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#Mỗi số sau là tổng của hai số liền trước nó.
fibonacci = []
a = 1
b = 0
fibonacci.append(b)
fibonacci.append(a)
for i in range(0,100): #vòng lặp được thực hiện từ i = 0 đến i = 99 nghĩa là vòng lặp được thực hiện 100 lẩn
  c = b                #i = 0 => c = b = 0
  b = a                #i = 0 => b = a = 1 
  a = c + b            #i = 0 => a = c + b = 0 + 1 = 1
  if a < 100:          #đảm bảo a < 100 sau khi a = c + b
    fibonacci.append(a)
print(fibonacci)

#Exercise 11
#Write a program to check true if a string contains only A-Z, a-z, 0-9. For example, 'Fresher @cademy' is false.
#Gợi ý: hàm isalnum() sẽ kiểm tra 1 chuỗi có chỉ chứa các kí tự A-Z, a-z, 0-9
mystring = 'IcanlovePythonfor4days'
check_mystring = mystring.isalnum()
print(check_mystring)
