nama = input("nama anda :")
kelamin = input("kelamin anda : [laki laki],[perempuan] :")
usia = int(input("usia anda :"))
bb = int(input("berat badan :"))
tinggi = int(input("tinggi badan :"))
nilai = int(input("nilai anda :"))
skill = input("skill yang anda kuasai : [memanah],[menembak],[berkuda] :")
cacat = input("ada cacat tubuh ? [ya],[tidak] :")



if kelamin == "perempuan" and bb >=45 and bb <=50 and tinggi >=165 and usia <=20 and nilai >=90 and usia <30 and cacat == ("tidak") :
	 print("anda memenuhi kriteria")
	 if cacat == "tidak" :
	 	print("selamat anda diterima")
	 else :
	 	print("anda tidak diterima")
elif kelamin == "laki laki" and bb >=70 and tinggi >=170 and usia <=25 and nilai >=90 and usia <=29 and cacat == ("tidak") :
	print("anda memenuhi kriteria")
	if skill == ("memanah","menembak","berkuda") and cacat == "tidak":
		print("selamat anda diterima")
	else : 
		print("anda tidak diterima")	
else :
	print("anda tidak diterima")
	


	

	