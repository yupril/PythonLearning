data = "ini adalah string" # String adalah kumpulan karakter
print(data)
print(type(data))

# 1. cara membuat string
'''
    1. Membuat string dengan single quote('...')
    2. Membuat string menggunakan double quote ("...")

'''
data ='ini menggunakan single quote'
print(data)

data ="ini menggunakan double quote"
print(data)

print('"Kamu siapa, kata deny?"')
print("Hari ini hari jum'at")

# 2. Membuat string menggunakan tanda \

# Membuat tanda single quote (') menjadi string
print('Mari kuta sholat jum\'at')
print('g\'day, isn\'t it?')

# backslash (\)
print("C:\\user\\document")

# tab (\t)
print ("Ucup\t\tMaman, Berjauhan ")

# Backspace (\b)
print("ucup \botong, deketan")

# Newline (\n) (\r)
print("Baris pertama.\nBaris Kedua.") # LF -> Line Feed
print("Baris pertama.\rBaris Kedua.") # CR -> carriage return
print("Baris pertama.\r\nBaris Kedua.") # CRLF -> carriage return line feed

# 3. Membuat string literal atau raw

# hati-hati
print('C:\new folder') # Path akan salah

# Menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# Multiline literal string
print(r"""
Nama : Ucup
Kelas : 1 SMK\new normal
Website : www.noahucup.co.id/ucup
""")
    