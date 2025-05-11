#q1
a = str(input("name:"))
b = int(input("year:"))
print(a+ "," , "you are", 2025-b, "years old")

#q2
print("malibu", "tesla")

#q3
c = str(input())
print(len(c))
print(c.upper())
print(c.lower())

#q4
d = input()
if str(d)[::-1] == str(d):
    print('palindrome')
else:
    print('not palindrome')

#q5
e = str(input())
vowelcount = 0
vowels = "aeiou"
for x in e:
    if x.lower() in vowels:
        vowelcount+=1
print(vowelcount, "vowels", len(e)-vowelcount, "consonants")

#q6
f = str(input())
g = str(input())
print(f in g)

#q7
h = str(input())
j = str(input())
k = str(input())
if j in h == False:
    print('Error')
else:
    print(h.replace(j, k))

#q8
l = str(input())
print(l[0], l[-1])

#q9
m = str(input())
print(m[::-1])

#q10
n = str(input())
print(n.count(" ")+1)

#q11
o = str(input())
for x in o:
    if x.isdigit:
        print(True)
        break
    else:
        print(False)

#q12
p = str(input())
print(p.replace("", "-"))

#q13
print(str(input()).replace(" ", ""))

#q14
print(str(input())==str(input()))

#q15
q = input()
acr = ""
for x in q.split():
    acr += x[0].upper()
print(acr)

#q16
r = str(input())
s = str(input())
print(r.replace(s, ""))

#q17
text = input()
vowels = "aeiouAEIOU"
result = ""
for char in text:
    if char in vowels:
        result += "*"
    else:
        result += char
print(result)


#q18
sentence = input()
start = input()
end = input()

if sentence.startswith(start) and sentence.endswith(end):
    print("True")
else:
    print("False")
