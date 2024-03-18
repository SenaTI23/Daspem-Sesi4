alex = input("pilihlah Alex : [gunting],[kertas],[batu] :")
ucok = input("pilihlah Ucok : [gunting],[kertas],[batu] :")


if alex == "batu" and ucok == "gunting" :
	print("alex win")
elif alex == "batu" and ucok == "kertas" :
	print("ucok win")
elif alex == "gunting" and ucok == "batu" :
	print("ucok win")
elif alex == "gunting" and ucok == "kertas" :
	print("alex win")
elif alex == "kertas" and ucok == "batu" :
	print("alex win")
elif alex == "kertas" and ucok == "gunting" :
	print("ucok win")
elif alex == ucok :
	print("seri")
