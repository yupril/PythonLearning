# Operasi dan manipulasi string

# 1. Menyambung string (concatenate)
nama_pertama = "Ucup"
nama_tengah = "Duloh"
nama_akhir = "Saikan"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang karakter dari: " + nama_lengkap + " = " + str(panjang))

# 3. Operator untuk string

# Mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print(d + " " "ada di " + nama_lengkap + " = " + str(status))

u = "u"
status = u in nama_lengkap
print(status)