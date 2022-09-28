# Latihan Operasi Aritmatika

a = 10
b = 3

# Operasi Tambah (+)
hasil = a + b
print(a, '+',b,'=',hasil)

# Operasi Pengurangan (-)
hasil = a - b
print(a, '-',b,'=',hasil)

# Operasi Perkalian (*)
hasil = a * b
print(a, '*',b,'=',hasil)

# Operasi Pembagian (/)
hasil = a / b
print(a, '/',b,'=',hasil)

# Operasi eksponen / Pangkat (**)
hasil = a ** b
print(a, '**',b,'=',hasil)

# Operasi modulus / Sisa Pembagian (%)
hasil = a % b
print(a, '%',b,'=',hasil)

# Operasi Floor Division / Dibulatkan Pembagian (//)
hasil = a // b
print(a, '//',b,'=',hasil)

# Prioritas Operasi, Operasi yang di dahulukan
'''
    1. ()
    2. exponen **
    3. Perkalian dan teman temannya * / ** % //
    4. Penjumlahan dan Pengurangan


'''
x = 3
y = 2
z = 4
hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

## Nyoba
hasil = x + y * x / y
print(x,'+',y,'*',x,'/',y,'=',hasil)

hasil = (x + y) * x / y # Kurung akan didahulukan
print(x,'+',y,'*',x,'/',y,'=',hasil)