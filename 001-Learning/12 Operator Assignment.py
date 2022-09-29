# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment


a = 5 # ini adalah assigment
print('Nilai a =',a)

a += 1 # ini artinya adalah a = a + 1
print('Nilai a += 1 ,nilai a menjadi',a)

a -= 2 # ini artinya adalah a = a - 2
print('Nilai a -= 2 ,nilai a menjadi',a)

a *= 5 # ini artinya adalah a = a * 5
print('Nilai a *= 5 ,nilai a menjadi',a)

a /= 2 # ini artinya adalah a = a / 2
print('Nilai a /= 2 ,nilai a menjadi',a)

b = 10
print('\nNilai B =',b)

# Modulus dan Floor Division
b %= 3
print('Nilai b %= 3 ,nilai a menjadi',b)

b = 10
print('\nNilai B =',b)

b //= 3
print('Nilai b //= 3, nilai a menjadi',b)

# Pangkat atau eksponen
a = 5
print('nilai a =', a)
a **= 3
print('Nilai a **= 3, nilai a menjadi',a)

# Operasi Bitwise

# OR
c = True
print('\nNilai c =', c)
c |= False
print('Nilai c |= false, nilai c menjadi',c)
c = False
print('\nNilai c =', c)
c |= False
print('Nilai c |= false, nilai c menjadi',c)

# AND
c = True
print('\nNilai c =', c)
c &= False
print('Nilai c &= false, nilai c menjadi',c)
c = True
print('\nNilai c =', c)
c &= True
print('Nilai c &= true, nilai c menjadi',c)

# XOR
c = True
print('\nNilai c =', c)
c ^= False
print('Nilai c ^= false, nilai c menjadi',c)
c = True
print('\nNilai c =', c)
c ^= True
print('Nilai c ^= true, nilai c menjadi',c)

# Geser geser
d= 0b0100
print('\nNilai d =', format(d, '04b'))
d >>= 2
print('\nNilai d >>= 2, nilai d menjadi ', format(d, '04b'))
d <<= 1
print('\nNilai d <<= 1, nilai d menjadi ', format(d, '04b'))