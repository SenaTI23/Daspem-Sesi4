a = int(input("bilangan a :"))
b = int(input("bilangan b :"))
c = int(input("bilangan c :"))

k = a + b + c
s = (a + b + c) / 2
l = (s*(s-a)*(s-b)*(s-c))**0.5

print("keliling nya adalah :",k)
print("luasnya adalah :",l)