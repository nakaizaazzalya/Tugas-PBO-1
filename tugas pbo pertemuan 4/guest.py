name = input("Masukkan nama Anda: ")

with open("guest.txt", "w") as file:
    file.write(name)

print("Nama berhasil disimpan ke guest.txt")