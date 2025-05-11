#q1
a = float(input())
print(round(a, 2))

#q2
b,c,d = map(int, input().split())
print(max(b,c,d))
print(min(b,c,d))

#q3
e = float(input())
print(e*1000, "meters or", e*10000, "centimeters")

#q4
f, g = map(int, input().split())
print("divisor:", f // g, "remainder:", f % g)

#q5
h = float(input())
print(h*(9/5)+32)

#q6
j = input().strip()
j = j.replace(".", "")
j = j.replace("-", "")
print(j[-1])

#q7
if (int(input())%2==0):
    print("even")
else:
    print("not even")