nama = input("nama anda :")
tempatlahir = input("tempat lahir anda :")
tanggallahir = input("tanggal lahir :")
bulanlahir = input("bulan lahir :")
tahunlahir = int(input("tahun lahir :"))
kelamin = input("kelamin anda : [laki laki],[perempuan] :")
english = int(input("nilai inggris :"))
mtk = int(input("nilai mtk :"))
indonesia = int(input("nilai indonesia :"))

nilai = (english + mtk + indonesia) / 3
usia = 2024 - tahunlahir
if kelamin == "laki laki" and nilai >=80 :
	jurusan = "teknik"
elif kelamin == "perempuan" and nilai >= 80 :
	jurusan = "sistem"
else :
	jurusan = "dkv"
if usia <=25 :
	print("")
	print("=" * 40)
	print("anda diterima")
	print("nama :",nama)
	print("tempat lahir :",tempatlahir)
	print("tanggal lahir :",tanggallahir)
	print("bulan lahir :",bulanlahir)
	print("tahun lahir :",tahunlahir)
	print("usia :",usia,"tahun")
	print("penjurusan :",jurusan)
else :
	print("")
	print("=" * 40)
	print("anda ditolak karena umur anda melebihi 25 tahun")

	
