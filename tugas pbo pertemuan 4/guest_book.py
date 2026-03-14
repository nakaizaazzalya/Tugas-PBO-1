names = []

while True:
    name = input("Masukkan nama (ketik 'q' untuk berhenti): ")
    
    if name == 'q':
        break
    
    names.append(name)

with open("guest book.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print("Semua nama telah disimpan ke guest book.txt")