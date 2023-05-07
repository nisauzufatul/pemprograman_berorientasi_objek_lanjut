class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("Nisa", 17)
# Menambah atribut address secara dinamis
person.address = "Jl. Kembang Desa"
# Mengubah nilai atribut age secara dinamis
person.age = 35
print(person.name)
print(person.age)
print(person.address)