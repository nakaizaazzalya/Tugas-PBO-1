while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        hasil = angka1 + angka2
        print("Hasil penjumlahan:", hasil)

    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar!")
    lagi = input("Hitung lagi? (y/n): ")
    if lagi.lower() != 'y':
        break