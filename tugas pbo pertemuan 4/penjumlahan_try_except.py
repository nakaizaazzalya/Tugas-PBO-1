try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    hasil = angka1 + angka2
    print("Hasil penjumlahan:", hasil)

except ValueError:
    print("Input harus berupa angka, bukan teks!")