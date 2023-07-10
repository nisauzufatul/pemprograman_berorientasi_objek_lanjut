
print("Tugas Minggu 1")
print("="*55)

# NIM : 210511001
# NAMA : Nisa Uzufatul Jannah
# KELAS : Karyawan 1 (K1)

# ===============================================================


class SuhuKelvin:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    def celcius(self):
        return (self.kelvin - 273)

    def farenheit(self):
        return 9/5 * (self.kelvin - 273) + 32

    def reamur(self):
        return 4/5 * (self.kelvin - 273)


# ===============================================================

print("Suhu Kelvin")
print("")
kelvin1 = SuhuKelvin(75)
print(f"Konversi dari Kelvin ke Celcius: {kelvin1.celcius()}")
kelvin2 = SuhuKelvin(60)
print(f"Konversi dari Kelvin ke Farenheit: {kelvin2.farenheit()}")
kelvin3 = SuhuKelvin(90)
print(f"Konversi dari Kelvin ke Reamur: {kelvin3.reamur()}")
