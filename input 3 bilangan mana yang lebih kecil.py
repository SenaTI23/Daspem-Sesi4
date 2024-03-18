a = int(input("masukan bilangan :"))
b = int(input("masukan bilangan :"))
c = int(input("masukan bilangan :"))

if a < b and a < c :
	print(f"angka {a} lebih kecil dari angka {b} dan {c}")
elif b < a and b < c :
	print(f"angka {b} lebih kecil dari angka {a} dan {c}")
elif c < b and c < a :
	print(f"angka {c} lebih kecil dari angka 	{b} dan {a}")
	