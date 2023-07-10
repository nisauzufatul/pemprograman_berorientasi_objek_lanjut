class KonversiSuhu:
    def __init__ (self, celcius): 
        self.celcius = celcius

    def to_reamur(self):
        return (4/5) * self.celcius

    def to_kelvin(self):
        return self.celcius + 273.15

    def to_fahrenheit(self):
        return (9/5) * self.celcius + 32

suhu = KonversiSuhu(36) 
fahrenheit = suhu.to_fahrenheit() 
kelvin = suhu.to_kelvin()
reamur = suhu.to_reamur()

print(f"{suhu.celcius} derajat Celcius = {reamur} derajat Reamur") 
print(f"{suhu.celcius} derajat Celcius = {kelvin} Kelvin") 
print(f"{suhu.celcius} derajat Celcius = {fahrenheit} Fahrenheit")
 
