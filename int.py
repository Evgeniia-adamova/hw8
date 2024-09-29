a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
if a > b:
    x = a
    a = b
    b = x
if b > c:
    x = b
    b = c
    c = x
if a > b:
    x = a
    a = b
    b = x
print(a, b, c)