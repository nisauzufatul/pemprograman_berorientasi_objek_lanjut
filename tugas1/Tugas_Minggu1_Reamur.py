
print("Tugas Minggu 1")
print("="*55)

# NIM : 210511001
# NAMA : Nisa Uzufatul Jannah
# KELAS : Karyawan 1 (K1)

# ===============================================================


class SuhuReamur:
    def __init__(self, reamur):
        self.reamur = reamur

    def celcius(self):
        return (5/4 * self.reamur)

    def farenheit(self):
        return (9/4 * self.reamur) + 32

    def kelvin(self):
        return (5/4 * self.reamur) + 273


# ===============================================================

print("Suhu Reamur")
print("")
reamur1 = SuhuReamur(75)
print(f"Konversi dari Reamur ke Celcius: {reamur1.celcius()}")
reamur2 = SuhuReamur(60)
print(f"Konversi dari Reamur ke Farenheit: {reamur2.farenheit()}")
reamur3 = SuhuReamur(90)
print(f"Konversi dari Reamur ke Kelvin: {reamur3.kelvin()}")
