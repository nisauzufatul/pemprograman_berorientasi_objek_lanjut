
print("Tugas Minggu 1")
print("="*55)

# NIM : 210511001
# NAMA : Nisa Uzufatul Jannah
# KELAS : Karyawan 1 (K1)

# ===============================================================


class SuhuFarenheit:
    def __init__(self, farenheit):
        self.farenheit = farenheit

    def celcius(self):
        return 5/9 * (self.farenheit - 32)

    def kelvin(self):
        return 5/9 * (self.farenheit - 32) + 273

    def reamur(self):
        return 4/9 * (self.farenheit - 32)


# ===============================================================

print("Suhu Farenheit")
print("")
farenheit1 = SuhuFarenheit(75)
print(f"Konversi dari Farenheit ke Celcius: {farenheit1.celcius()}")
farenheit2 = SuhuFarenheit(60)
print(f"Konversi dari Farenheit ke Kelvin: {farenheit2.kelvin()}")
farenheit3 = SuhuFarenheit(90)
print(f"Konversi dari Farenheit ke Reamur: {farenheit3.reamur()}")
