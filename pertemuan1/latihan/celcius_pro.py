# NAMA  : Nisa Uzufatul Jannah
# NIM   : 210511001
# KELAS : K1

class Suhu:
    @staticmethod
    def celcius_to_kelvin(c):
        k = c + 273
        return k
    
#Contoh penggunaan
C = 20
K = Suhu.celcius_to_kelvin(C)

print("Konversi", C, "derajat Celcius adalah:", K, "derajat Kelvin")
