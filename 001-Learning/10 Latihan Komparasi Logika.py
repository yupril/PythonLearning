# Latihan Logika dan Komparasi

# Membuat gabungan area rentang dari angka

#++++++3---------10+++++++

inputUser = float(input("Masukan angka yang bernilai\n kurang dari 3,\n atau lebih besar dari 10 : "))

#+++++3---------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)
#-----------------10+++++++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

isBenar = isKurangDari or isLebihDari
print ("Angka yang anda masukan: ", isBenar)

# -------3++++++++10------ Angka lebih dari 3 kurang dari 10
# Kasus irisan

inputUser = float(input("Masukan angka yang bernilai\n lebih dari 3,\n dan kurang dari 10 : "))

#----3++++++++++++++
isLebihDari = (inputUser > 3)
print ("Lebih dari 3 =", isLebihDari)

#+++++++++10--------
isKurangDari = (inputUser < 10)
print ("Kurang dari 10 =", isKurangDari)

isBenar = isLebihDari and isKurangDari
print("Angka yang anda masukan :", isBenar)

# Tugas 
# 1. -----0++++++5------8++++11---
print("==========Tugas 1==========")
inputUser = float(input("Masukan angka yang\n >0 dan <5 Atau >8 dan <11 : "))

isLebihDari0 = (inputUser > 0 )
isKurangDari5 = (inputUser < 5)
isBenar05 = isLebihDari0 and isKurangDari5
print ("Angka >0 dan <5 =", isBenar05)

isLebihDari8 = (inputUser > 8 )
isKurangDar11 = (inputUser < 11)
isBenar811 = isLebihDari8 and isKurangDar11
print ("Angka >8 dan <11 =",isBenar811)

isBenar = isBenar05 or isBenar811
print("Angka yang anda masukan: ",isBenar)

# 2. ++++0-----5++++8-----11+++++++
print("==========Tugas 2==========")
inputUser = float(input("Masukan angka yang\n <0 atau >5 dan <8 atau >11 : "))

isKurang0 = (inputUser < 0)
isLebihDari11 = (inputUser > 11)
isBenar011 = (isKurang0 or isLebihDari11)
print ("Angka <0 atau >11 =",isBenar011)

isLebihdari5 = (inputUser > 5)
isKurangdari8 = (inputUser < 8)
isBenar58 = (isLebihdari5 and isKurangdari8)
print ("Angka >5 dan <8 =",isBenar58)

isBenar = (isBenar011 or isBenar58)
print ("Angka yang kamu masukan :",isBenar)