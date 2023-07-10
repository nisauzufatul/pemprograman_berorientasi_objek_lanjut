# Nama   : Nisa Uzufatul Jannah
# NIM    : 210511001
# Kelas  : K1
# Matkul : Pemrogaman Berorientasi Objek 2

class Matematika:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c=0):
        return a + b + c


mat = Matematika()
B = mat.add(7, 10, 1)
print(B)
mut = Matematika()
C = mut.add(7, 10)
print(C)
