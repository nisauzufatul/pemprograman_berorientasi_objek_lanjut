# NAMA  : Nisa Uzufatul Jannah
# NIM   : 210511001
# KELAS : K1

class SuhuCelcius:
    def __init__(self, celcius):
        self.celcius = celcius
    def kelvin(self):
        return (self.celcius + 273.15)

print("Suhu Celcius")
celcius1 = SuhuCelcius(75)
print(f"Konversi dari Celcius ke Kelvin: {celcius3.kelvin()}")
print("="*50)

