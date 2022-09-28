# Mengambil data dari User

# Data yang dimasukan pasti string
data = input ("Masukan Nama: ")

print("data =",data,",type =",type(data))

# JIka kita ingin mengambil data integer, maka
data_int = int(input("Masukan angka:"))

print ("data =",data_int,",type =",type(data_int))

# bagaimana dengan float dan boolean
# Rubah dulu kedalam integer

biner = bool(int(input("Masukan nilai bolean:")))

print ("data =",biner,",type=",type(biner))