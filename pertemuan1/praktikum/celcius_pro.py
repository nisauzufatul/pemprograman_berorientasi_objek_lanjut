# NIM   : 210511001
# Nama  : Nisa Uzufatul Jannah
# Kelas : TI21K (K1)

class KonversiSuhu: 
    @staticmethod
    def celcius_to_fahrenheit(celcius): return (celcius * 9/5) + 32

    @staticmethod
    def celcius_to_reamur(celcius): return celcius * 4/5

    @staticmethod
    def celcius_to_kelvin(celcius): return celcius + 273.15

# Konversi suhu 35 derajat Celsius ke Fahrenheit 
fahrenheit = KonversiSuhu.celcius_to_fahrenheit(37)
print("konversi suhu",35, "derajat celcius adalah ",fahrenheit, "derajat fahrenheit")

# Konversi suhu 40 derajat Celsius ke Reamur 
reamur = KonversiSuhu.celcius_to_reamur(47)
print("konversi suhu",40, "derajat celcius adalah ",reamur, "derajat reamur")

# Konversi suhu 38 derajat Celsius ke Kelvin 
kelvin = KonversiSuhu.celcius_to_kelvin(27)
print("konversi suhu",38, "derajat celcius adalah ",kelvin, "derajat kelvin")
