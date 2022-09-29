# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah boolean (True/False)

#>,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# Lebih besar dari
print("============Lebih Besar Dari==========")
hasil = a > 3
print(a, '>', 3, '=', hasil)

hasil = b > 3
print(b, '>', 3, '=', hasil)

# Lebih kecil dari
print("============Kurang Besar Dari==========")
hasil = a < 3
print(a, '<', 3, '=', hasil)

hasil = b < 3
print(b, '<', 3, '=', hasil)

# Lebih dari atau sama dengan
print("======Lebih Dari Atau Sama Dengan=======")
hasil = a >= 3
print(a, '>=', 3, '=', hasil)

hasil = b >= 1
print(b, '>=', 1, '=', hasil)

# Kurang dari atau sama dengan
print("======Kurang Dari Atau Sama Dengan=======")
hasil = a <= 3
print(a, '<=', 3, '=', hasil)

hasil = b <= 5
print(b, '<=', 5, '=', hasil)

# Sama dengan
print("======Sama Dengan=======")
hasil = a == 4
print(a, '==', 4, '=', hasil)

hasil = b == 5
print(b, '==', 5, '=', hasil)

# Tidak sama dengan
print("======Tidak Sama Dengan=======")
hasil = a != 4
print(a, '!=', 4, '=', hasil)

hasil = b != 5
print(b, '!=', 5, '=', hasil)

# 'is' Sebagai Komparasi Object Identitiy
x = 5 #ini adalah assigment membuat pbject
y = 5
print("======is=======")
print('nilai x =,',x,'id = ',hex(id(x)))
print('nilai y =,',y,'id = ',hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 5 #ini adalah assigment membuat pbject
y = 7
print("======is=======")
print('nilai x =,',x,'id = ',hex(id(x)))
print('nilai y =,',y,'id = ',hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 5 #ini adalah assigment membuat pbject
y = 7
print("======is=======")
print('nilai x =,',x,'id = ',hex(id(x)))
print('nilai y =,',y,'id = ',hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)