# Latihan Konversi Satuan Temperature
'''
    1. Celcius
    2. Reamur
    3. Fahrenheit
    4. Kelvin
'''
# Program konversi celcius ke satuan lain

print("\nProgram Konfersi Temperatur\n")

celcius = float(input("Masukan Suhu Dalam Celcius : "))
print("Suhu adalah ",celcius, "Celcius")

# Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ",reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ",kelvin, "Kelvin")

# Tugas 1 Konversi Fahrenheit kedalam Kelvin
print("\nProgram Konfersi Temperatur F To K\n")

fahrenheit = float(input("Masukan Suhu Dalam Fahrenheit : "))
celcius = (5/9) * (fahrenheit - 32)
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ",kelvin, "Kelvin")

# Tugas 2 Konversi Kelvin Kedalam Fahrenheit
print("\nProgram Konfersi Temperatur K To F\n")

kelvin = float(input("Masukan Suhu Dalam Kelvin : "))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")
