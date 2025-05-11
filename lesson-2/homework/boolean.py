#q1
username = input()
password = input()
if username and password:
    print("Username and password accepted.")
else:
    print("Username and password cannot be empty.")

#q2
a = int(input())
b = int(input())
if a == b:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

#q3
n = int(input())
if n > 0 and n % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is not positive and even.")

#q4
x = int(input())
y = int(input())
z = int(input())
if x != y and y != z and x != z:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")

#q5
s1 = input()
s2 = input()
if len(s1) == len(s2):
    print("The strings have the same length.")
else:
    print("The strings do not have the same length.")

#q6
l = int(input())
if l % 3 == 0 and l % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

#q7
m = float(input())
n = float(input())
if m + n > 50.8:
    print("The sum is greater than 50.8")
else:
    print("The sum is not greater than 50.8")

#q8
v = int(input("Enter a number: "))
if 10 <= v <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")