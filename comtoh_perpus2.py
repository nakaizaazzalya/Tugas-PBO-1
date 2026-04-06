from abc import ABC, abstractmethod

# =========================
# ABSTRACT BASE CLASS
# =========================
class Transaksi(ABC):
    @abstractmethod
    def proses(self):
        pass


# =========================
# CLASS BUKU
# =========================
class Buku:
    def __init__(self, id_buku, judul, stok):
        self.__id_buku = id_buku      # PRIVATE (name mangling)
        self.__judul = judul          # PRIVATE
        self.__stok = stok            # PRIVATE

    # ===== PROPERTY (GETTER) =====
    @property
    def stok(self):
        return self.__stok

    @property
    def judul(self):
        return self.__judul

    # ===== PROPERTY (SETTER) =====
    @stok.setter
    def stok(self, nilai):
        if nilai < 0:
            raise ValueError("Stok tidak boleh negatif")
        self.__stok = nilai

    # ===== METHOD =====
    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus > 0")
        self.__stok += jumlah

    def kurangi_stok(self):
        if self.__stok <= 0:
            raise ValueError("Stok habis")
        self.__stok -= 1

    def info(self):
        return f"ID: {self.__id_buku} | Judul: {self.__judul} | Stok: {self.__stok}"


# =========================
# CLASS ANGGOTA
# =========================
class Anggota:
    def __init__(self, nama):
        self.__nama = nama                 # PRIVATE
        self._pinjaman = []               # PROTECTED

    @property
    def nama(self):
        return self.__nama

    def pinjam(self, buku):
        try:
            buku.kurangi_stok()
            self._pinjaman.append(buku)
            print(f"{self.__nama} meminjam {buku.judul}")
        except Exception as e:
            print("Error:", e)

    def kembali(self, buku):
        if buku in self._pinjaman:
            buku.tambah_stok(1)
            self._pinjaman.remove(buku)
            print(f"{self.__nama} mengembalikan {buku.judul}")
        else:
            print("Buku tidak ditemukan dalam pinjaman")


# =========================
# CLASS TRANSAKSI TURUNAN
# =========================
class Peminjaman(Transaksi):
    def __init__(self, anggota, buku):
        self.anggota = anggota
        self.buku = buku

    def proses(self):
        self.anggota.pinjam(self.buku)


class Pengembalian(Transaksi):
    def __init__(self, anggota, buku):
        self.anggota = anggota
        self.buku = buku

    def proses(self):
        self.anggota.kembali(self.buku)


# =========================
# MAIN PROGRAM
# =========================
buku1 = Buku("AA101", "Basis Data", 5)
anggota1 = Anggota("Aziz")

print(buku1.info())

# TRANSAKSI PINJAM
t1 = Peminjaman(anggota1, buku1)
t1.proses()
t1.proses()
t1.proses()
print(buku1.info())

# TRANSAKSI KEMBALI
t2 = Pengembalian(anggota1, buku1)
t2.proses()
t2.proses()
t2.proses()

print(buku1.info())