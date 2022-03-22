# find the count of vowels in a string
name = "hello world"
count = 0
for i in name:

    if i in ("a,e,i,o,u"):
        count = count + 1
print(count)

# two
name = "python is a programming"
count = 0
for i in name:
    if i in ("a,b,c,d,e,f"):
        count = count + 1
print(count)

# WAP that accept list of integers and check the length and fifth element
a = [19, 19, 15, 5, 5, 5, 1, 2]
m = len(a)
n = (a.count(5))
if m == 8 and n >= 3:
    print("True")

# if len(a) == 8 and a.count(5) >= 3:
    # print("true")

b = [6, 9, 2, 5, 8, 7, 4]
if len(b) == 7:
    print("Truth")


'''# even numberd length words to python
x = "hi hello python iam a programming language"
l = []
a = x.split(" ")
for i in a:
    if len(i) % 3 == 0:
        l.append(i)
print(l)'''

y = ["i", "iam", "a", "python", "programmer"]
l = []
for i in y:
    if len(i) % 2 == 0:
        l.append(i)
print(i)

# smallest numbers
a = 100
b = 20
c = 10
if a < b and a < c:
    print("a is small")
elif b < a and b < c:
    print("b is small")
elif c < a and c < b:
    print("c is small")
else:
    print("c is small")

a = 70
b = 80
c = 90
if a > b and b > c:
    print("a is smaller")
elif b > a and b > c:
    print("b is smaller")
elif c > a and c > b:
    print("c is bigger")
else:
    print("not applicable")


n = "pythonlaungage"
for i in n:
    if i == "h":
        print(i)

name = "assessement"
for i in name:
    if i == "m":
        print("m")


name = "hi hello python welcome to world"
l = []
a = name.split(" ")
for i in a:
    if len(i) % 5 == 0:
        l.append(i)
print(l)


name1 = "hi hello python and world to welcome bro"
l = []
a = name1.split(" ")
for i in a:
    if len(i) % 3 == 0:
        l.append(i)
print(l)

 