class Calculator:

    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    def bagi(self, a, b):
        if b == 0:
            raise ValueError("Tidak bisa membagi dengan nol")
        return a / b

if __name__ == "__main__":
    calc = Calculator()

    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))

    print("Penjumlahan:", calc.tambah(a, b))
    print("Pengurangan:", calc.kurang(a, b))
    print("Perkalian:", calc.kali(a, b))
    print("Pembagian:", calc.bagi(a, b))