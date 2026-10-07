class Produk:

    nama_minimarket = "Minimarket Muhammad Fajar"
    jumlah_produk = 0

    def __init__(self, kode_produk, nama_produk, kategori, harga, stok):

        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.harga = harga
        self.__stok = stok

        self._jenis_produk = kategori

        Produk.jumlah_produk += 1

    def tampilkan_produk(self):
        print("Kode     :", self.kode_produk)
        print("Nama     :", self.nama_produk)
        print("Kategori :", self.kategori)
        print("Harga    : Rp", self.harga)
        print("Stok     :", self.__stok)

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah
            print("Stok berhasil ditambahkan.")
        else:
            print("Jumlah stok harus lebih dari 0.")

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            raise ValueError("Stok tidak boleh negatif.")
        self.__stok = stok_baru

    @classmethod
    def ambil_data(cls, data):
        return cls(data["kode_produk"], data["nama_produk"], data["kategori"], data["harga"], data["stok"])

    @staticmethod
    def validasi_harga(harga):
        return harga > 0

class Snack(Produk):

    def __init__(self, kode_produk, nama_produk, harga, stok, rasa):

        super().__init__(kode_produk, nama_produk,"Snack", harga, stok)

        self.rasa = rasa

    def tampilkan_produk(self):
        print("Kode     :", self.kode_produk)
        print("Nama     :", self.nama_produk)
        print("Kategori :", self._jenis_produk)
        print("Harga    : Rp", self.harga)
        print("Stok     :", self.stok)
        print("Rasa     :", self.rasa)


class Minuman(Produk):

    def __init__(self, kode_produk, nama_produk, harga, stok, ukuran):

        super().__init__(kode_produk, nama_produk, "Minuman", harga, stok)

        self.ukuran = ukuran

    def tampilkan_produk(self):
        print("Kode     :", self.kode_produk)
        print("Nama     :", self.nama_produk)
        print("Kategori :", self._jenis_produk)
        print("Harga    : Rp", self.harga)
        print("Stok     :", self.stok)
        print("Ukuran   :", self.ukuran)


class Pelanggan:

    nama_minimarket = "Minimarket Muhammad Fajar"
    jumlah_pelanggan = 0
    status_member = "Pelanggan Minimarket"

    def __init__(self, nama_pelanggan, no_telepon):

        self.nama_pelanggan = nama_pelanggan
        self.no_telepon = no_telepon
        self.__saldo = 0

        Pelanggan.jumlah_pelanggan += 1

    def tampilkan_pelanggan(self):
        print("Nama       :", self.nama_pelanggan)
        print("No. Telepon:", self.no_telepon)
        print("Saldo      : Rp", self.__saldo)

    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print("Saldo berhasil ditambahkan.")
        else:
            print("Jumlah saldo harus lebih dari 0.")

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo_baru):
        if saldo_baru < 0:
            raise ValueError("Saldo tidak boleh negatif.")

        self.__saldo = saldo_baru

    @classmethod
    def ubah_status_member(cls, status_baru):
        if status_baru.strip() == "":
            raise ValueError("Status tidak boleh kosong.")

        cls.status_member = status_baru
        print("Status pelanggan berhasil diubah.")

    @staticmethod
    def validasi_no_telepon(no_telepon):
        return no_telepon.isdigit() and len(no_telepon) >= 10


class Transaksi:

    nama_minimarket = "Minimarket Muhammad Fajar"
    jumlah_transaksi = 0
    biaya_layanan = 2000

    def __init__(self, nomor_transaksi, pelanggan):

        self.nomor_transaksi = nomor_transaksi
        self.pelanggan = pelanggan
        self.__total = 0

        Transaksi.jumlah_transaksi += 1

    def tambah_produk(self, produk, jumlah):
        if jumlah <= 0:
            print("Jumlah produk harus lebih dari 0.")
        elif jumlah > produk.stok:
            print("Stok produk tidak mencukupi.")
        else:
            self.__total += produk.harga * jumlah
            produk.stok = produk.stok - jumlah

            print(
                produk.nama_produk,
                "sebanyak",
                jumlah,
                "berhasil ditambahkan ke transaksi."
            )

    def tampilkan_transaksi(self):
        print("Nomor Transaksi :", self.nomor_transaksi)
        print("Pelanggan       :", self.pelanggan.nama_pelanggan)
        print("Total           : Rp", self.__total)
        print("Biaya Layanan   : Rp", Transaksi.biaya_layanan)
        print("Total Bayar     : Rp",self.__total + Transaksi.biaya_layanan)

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total_baru):
        if total_baru < 0:
            raise ValueError("Total transaksi tidak boleh negatif.")

        self.__total = total_baru

    @classmethod
    def ubah_biaya_layanan(cls, biaya_baru):
        if biaya_baru < 0:
            raise ValueError("Biaya layanan tidak boleh negatif.")

        cls.biaya_layanan = biaya_baru
        print("Biaya layanan berhasil diubah.")

    @staticmethod
    def hitung_total(harga, jumlah):
        if harga < 0 or jumlah < 0:
            return 0

        return harga * jumlah

class DetailTransaksi:

    def __init__(self, produk, jumlah, subtotal):

        self.produk = produk
        self.jumlah = jumlah
        self.subtotal = subtotal

    def tampilkan_detail(self):

        print(self.produk.nama_produk, "x", self.jumlah, "= Rp", self.subtotal)


class TransaksiLengkap(Transaksi):

    def __init__(self, nomor_transaksi, pelanggan):

        super().__init__(nomor_transaksi, pelanggan)

        self._detail = []

    def tambah_produk(self, produk, jumlah):

        stok_awal = produk.stok

        super().tambah_produk(produk, jumlah)

        if jumlah > 0 and jumlah <= stok_awal:

            detail = DetailTransaksi(produk, jumlah, produk.harga * jumlah)

            self._detail.append(detail)

    def tampilkan_detail(self):

        print("\nDETAIL TRANSAKSI")

        for detail in self._detail:
            detail.tampilkan_detail()

class Minimarket:

    def __init__(self, nama_minimarket):

        self.nama_minimarket = nama_minimarket
        self._produk = []

    def tambah_produk(self, produk):

        self._produk.append(produk)

        print(produk.nama_produk, "berhasil ditambahkan ke", self.nama_minimarket)

    def tampilkan_produk(self):

        print("\nDAFTAR PRODUK MINIMARKET")

        for produk in self._produk:

            produk.tampilkan_produk()
            print()

print("=" * 60)
print("SISTEM MINIMARKET")
print("Penjualan Snack, Minuman, dan Makanan")
print("=" * 60)

produk1 = Produk("001", "Chitato", "Snack", 12000, 20)

produk2 = Produk("002", "Teh Botol", "Minuman", 5000, 30)

print("\nDATA PRODUK")

produk1.tampilkan_produk()
print()

produk2.tampilkan_produk()

print("\nTAMBAH STOK")

produk1.tambah_stok(5)

print("Stok Chitato sekarang:", produk1.stok)

print("\nGETTER STOK")

print("Stok produk 1:", produk1.stok)
print("Stok produk 2:", produk2.stok)

print("\nMENGUBAH STOK")

produk1.stok = 30

print("Stok produk 1 setelah diubah:", produk1.stok)

print("\nMEMVALIDASI STOK")

try:
    produk1.stok = -10
except ValueError as e:
    print("Validasi:", e)

print("\nSTATIC METHOD PRODUK")

print("Apakah harga Rp12.000 TRUE ATAU FALSE?", Produk.validasi_harga(12000))

print("Apakah harga Rp0 TRUE ATAU FALSE?", Produk.validasi_harga(0))

print("\nCLASS METHOD PRODUK")

data_produk = {"kode_produk": "003", "nama_produk": "Roti Coklat", "kategori": "Makanan", "harga": 8000, "stok": 15}

produk3 = Produk.ambil_data(data_produk)

produk3.tampilkan_produk()

pelanggan1 = Pelanggan("Andi", "081234567890")

pelanggan2 = Pelanggan("Budi", "082345678901")

print("\nDATA PELANGGAN")

pelanggan1.tampilkan_pelanggan()
print()

pelanggan2.tampilkan_pelanggan()

print("\nTAMBAH SALDO")

pelanggan1.tambah_saldo(100000)

print("Saldo Andi:", pelanggan1.saldo)

print("\nMENGUBAH SALDO")

pelanggan1.saldo = 150000

print("Saldo Andi setelah diubah:", pelanggan1.saldo)

print("\nMEMVALIDASI SALDO")

try:
    pelanggan1.saldo = -50000
except ValueError as e:
    print("Validasi:", e)

print("\nSTATIC METHOD PELANGGAN")

print("No. telepon Andi 081234567890 TRUE ATAU FALSE?", Pelanggan.validasi_no_telepon("081234567890"))

print("No. telepon valid 123 TRUE ATAU FALSE?", Pelanggan.validasi_no_telepon("123"))

print("\nCLASS METHOD PELANGGAN")

Pelanggan.ubah_status_member("Pelanggan Minimarket")

transaksi1 = Transaksi("TRX001", pelanggan1)

transaksi2 = Transaksi("TRX002", pelanggan2)

print("\nTRANSAKSI 1")

transaksi1.tambah_produk(produk1, 2)
transaksi1.tambah_produk(produk2, 3)

transaksi1.tampilkan_transaksi()

print("\nTRANSAKSI 2")

transaksi2.tambah_produk(produk3, 2)

transaksi2.tampilkan_transaksi()

print("\nGETTER TOTAL")

print("Total transaksi 1:", transaksi1.total)
print("Total transaksi 2:", transaksi2.total)

print("\nMENGUBAH TOTAL")

transaksi1.total = 50000

print("Total transaksi 1 setelah diubah:", transaksi1.total)

print("\nMEMVALIDASI TOTAL")

try:
    transaksi1.total = -10000
except ValueError as e:
    print("Validasi:", e)

print("\nSTATIC METHOD TRANSAKSI")

hasil = Transaksi.hitung_total(10000, 3)

print("Rp10.000 x 3 =", hasil)

print("\nCLASS METHOD TRANSAKSI")

Transaksi.ubah_biaya_layanan(3000)

transaksi1.tampilkan_transaksi()

print("\nATRIBUT KELAS")

print("Nama Minimarket :", Produk.nama_minimarket)
print("Jumlah Produk   :", Produk.jumlah_produk)

print()

print("Jumlah Pelanggan:", Pelanggan.jumlah_pelanggan)
print("Status Member   :", Pelanggan.status_member)

print()

print("Jumlah Transaksi:", Transaksi.jumlah_transaksi)
print("Biaya Layanan   :", Transaksi.biaya_layanan)

print("\n" + "=" * 60)
print("PENGUJIAN POSTTEST 2")
print("=" * 60)

print("\nPENGUJIAN INHERITANCE")

snack1 = Snack("004", "Doritos", 10000, 25, "Keju")

minuman1 = Minuman("005", "Aqua", 4000, 40, "600 ml")

snack1.tampilkan_produk()
print()

minuman1.tampilkan_produk()

print("\nPENGUJIAN ATRIBUT KHUSUS SUBCLASS")

print("Rasa Snack    :", snack1.rasa)
print("Ukuran Minuman:", minuman1.ukuran)

print("\nPENGUJIAN PROTECTED ATTRIBUTE")

print("Jenis produk Snack:", snack1._jenis_produk)

print("Jenis produk Minuman:", minuman1._jenis_produk)

print("\nPENGUJIAN INHERITANCE")

print("Snack adalah Produk:", isinstance(snack1, Produk))

print("Minuman adalah Produk:", isinstance(minuman1, Produk))

print("Snack adalah Minuman:", isinstance(snack1, Minuman))

print("\nPENGUJIAN AGGREGATION")

minimarket1 = Minimarket("Minimarket Muhammad Fajar")

minimarket1.tambah_produk(produk1)
minimarket1.tambah_produk(produk2)
minimarket1.tambah_produk(produk3)
minimarket1.tambah_produk(snack1)
minimarket1.tambah_produk(minuman1)

minimarket1.tampilkan_produk()

print("\nPENGUJIAN COMPOSITION")

transaksi3 = TransaksiLengkap("TRX003",pelanggan1)

transaksi3.tambah_produk(snack1, 2)

transaksi3.tambah_produk(minuman1, 3)

transaksi3.tampilkan_transaksi()
transaksi3.tampilkan_detail()

print("\nPENGUJIAN ASSOCIATION")

transaksi3.tambah_produk(produk3, 1)

transaksi3.tampilkan_transaksi()


print("\n" + "=" * 60)
print("PENGUJIAN POSTTEST 2 SELESAI")
print("=" * 60)