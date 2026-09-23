# Sistem Minimarket Untuk Penjualan Snack, Minuman, dan Makanan.

```text
NIM = 2509106117
NAMA = MUHAMMAD FAJAR
KELAS = C2'25
```

Program ini merupakan program **Sistem Minimarket** yang dibuat menggunakan bahasa pemrograman **Python** dengan menerapkan konsep **Object-Oriented Programming (OOP)**.

Program digunakan untuk menggambarkan proses sederhana pada minimarket yang menjual **snack, minuman, dan makanan**. Program memiliki tiga class utama, yaitu `Produk`, `Pelanggan`, dan `Transaksi`.

Program ini juga menerapkan beberapa konsep OOP, yaitu:

* Class dan Object
* Constructor
* Atribut kelas
* Atribut objek
* Encapsulation
* Getter dan Setter menggunakan `@property`
* Class Method menggunakan `@classmethod`
* Static Method menggunakan `@staticmethod`
* Validasi data
* Relasi antar-object

---

## 1. Tujuan Program

Program ini dibuat untuk mensimulasikan pengelolaan sederhana pada minimarket, meliputi:

1. Menyimpan data produk.
2. Menampilkan informasi produk.
3. Menambahkan stok produk.
4. Mengubah stok produk dengan setter.
5. Memvalidasi agar stok tidak bernilai negatif.
6. Memvalidasi harga produk.
7. Membuat data produk dari dictionary.
8. Menyimpan data pelanggan.
9. Menampilkan informasi pelanggan.
10. Menambahkan saldo pelanggan.
11. Mengubah saldo pelanggan.
12. Memvalidasi agar saldo tidak bernilai negatif.
13. Memvalidasi nomor telepon pelanggan.
14. Membuat transaksi berdasarkan pelanggan.
15. Menambahkan produk ke dalam transaksi.
16. Mengurangi stok ketika produk masuk ke transaksi.
17. Menghitung total transaksi.
18. Mengubah biaya layanan.
19. Menghitung jumlah produk, pelanggan, dan transaksi yang dibuat.

---

# 2. Struktur Program

Program terdiri dari tiga class utama:

```text
Sistem Minimarket
│
├── class Produk
│   ├── Atribut kelas
│   ├── Constructor
│   ├── Method menampilkan produk
│   ├── Method menambah stok
│   ├── Getter dan Setter stok
│   ├── Class Method dari_data()
│   └── Static Method validasi_harga()
│
├── class Pelanggan
│   ├── Atribut kelas
│   ├── Constructor
│   ├── Method menampilkan pelanggan
│   ├── Method menambah saldo
│   ├── Getter dan Setter saldo
│   ├── Class Method ubah_status_member()
│   └── Static Method validasi_no_telepon()
│
└── class Transaksi
    ├── Atribut kelas
    ├── Constructor
    ├── Method menambah produk
    ├── Method menampilkan transaksi
    ├── Getter dan Setter total
    ├── Class Method ubah_biaya_layanan()
    └── Static Method hitung_total()
```

---

# 3. Penjelasan Class `Produk`

Class `Produk` digunakan untuk menyimpan dan mengelola data barang yang dijual di minimarket.

## 3.1 Atribut Kelas

```python
class Produk:

    nama_minimarket = "Minimarket Muhammad Fajar"
    jumlah_produk = 0
```

### `nama_minimarket`

```python
nama_minimarket = "Minimarket Muhammad Fajar"
```

Digunakan untuk menyimpan nama minimarket.

Atribut ini merupakan **atribut kelas**, sehingga dapat diakses langsung melalui class:

```python
Produk.nama_minimarket
```

### `jumlah_produk`

```python
jumlah_produk = 0
```

Digunakan untuk menghitung jumlah object produk yang telah dibuat.

Nilainya akan bertambah setiap kali constructor `Produk` dijalankan.

---

## 3.2 Constructor `__init__`

```python
def __init__(self, kode_produk, nama_produk, kategori, harga, stok):
```

Constructor digunakan untuk memberikan data awal ketika object `Produk` dibuat.

Parameter yang digunakan:

* `kode_produk` → kode produk.
* `nama_produk` → nama produk.
* `kategori` → kategori produk.
* `harga` → harga produk.
* `stok` → jumlah stok produk.

Contoh:

```python
produk1 = Produk(
    "001",
    "Chitato",
    "Snack",
    12000,
    20
)
```

Artinya dibuat satu object produk dengan kode `001`, nama `Chitato`, kategori `Snack`, harga Rp12.000, dan stok 20.

---

## 3.3 Atribut Object

```python
self.kode_produk = kode_produk
self.nama_produk = nama_produk
self.kategori = kategori
self.harga = harga
self.__stok = stok
```

Baris tersebut menyimpan data yang diterima constructor ke dalam object.

Contohnya:

```python
self.nama_produk = nama_produk
```

Jika object dibuat dengan:

```python
Produk("001", "Chitato", "Snack", 12000, 20)
```

maka `self.nama_produk` akan berisi:

```text
Chitato
```

Sedangkan:

```python
self.__stok = stok
```

menyimpan stok sebagai atribut **private** karena menggunakan dua garis bawah (`__`).

---

## 3.4 Menghitung Jumlah Produk

```python
Produk.jumlah_produk += 1
```

Setiap kali object `Produk` dibuat, nilai `jumlah_produk` bertambah satu.

Contohnya:

```python
produk1 = Produk(...)
produk2 = Produk(...)
produk3 = Produk(...)
```

Maka:

```text
Produk.jumlah_produk = 3
```

---

## 3.5 Method `tampilkan_produk()`

```python
def tampilkan_produk(self):
```

Method ini digunakan untuk menampilkan informasi produk.

```python
print("Kode     :", self.kode_produk)
print("Nama     :", self.nama_produk)
print("Kategori :", self.kategori)
print("Harga    : Rp", self.harga)
print("Stok     :", self.__stok)
```

Setiap baris mengambil data dari object dan menampilkannya ke layar.

Contoh penggunaan:

```python
produk1.tampilkan_produk()
```

Hasilnya akan menampilkan kode, nama, kategori, harga, dan stok produk.

---

## 3.6 Method `tambah_stok()`

```python
def tambah_stok(self, jumlah):
```

Method ini digunakan untuk menambahkan stok produk.

```python
if jumlah > 0:
```

Program memeriksa apakah jumlah yang akan ditambahkan lebih dari 0.

Jika benar:

```python
self.__stok += jumlah
```

stok akan ditambahkan.

Jika jumlah tidak lebih dari 0:

```python
print("Jumlah stok harus lebih dari 0.")
```

Program memberikan pesan bahwa jumlah stok tidak valid.

---

## 3.7 Getter `stok`

```python
@property
def stok(self):
    return self.__stok
```

Getter digunakan untuk **membaca nilai stok** yang disimpan pada atribut private `__stok`.

Karena menggunakan `@property`, pemanggilannya tidak menggunakan tanda kurung.

Contoh:

```python
print(produk1.stok)
```

Bukan:

```python
print(produk1.stok())
```

Getter ini memungkinkan program membaca atribut private dengan cara yang terkontrol.

---

## 3.8 Setter `stok`

```python
@stok.setter
def stok(self, stok_baru):
```

Setter digunakan untuk mengubah nilai stok.

```python
if stok_baru < 0:
    raise ValueError("Stok tidak boleh negatif.")
```

Program memeriksa apakah stok baru kurang dari 0.

Jika kurang dari 0, program menghasilkan `ValueError`.

Jika nilainya valid:

```python
self.__stok = stok_baru
```

stok akan diubah.

Contoh:

```python
produk1.stok = 30
```

akan mengubah stok menjadi 30.

Sedangkan:

```python
produk1.stok = -10
```

akan ditolak karena stok tidak boleh negatif.

---

## 3.9 Class Method `ambil_data()`

```python
@classmethod
def ambil_data(cls, data):
```

Method ini digunakan untuk membuat object `Produk` berdasarkan data yang disimpan dalam dictionary.

Contoh dictionary:

```python
data_produk = {
    "kode_produk": "003",
    "nama_produk": "Roti Coklat",
    "kategori": "Makanan",
    "harga": 8000,
    "stok": 15
}
```

Kemudian:

```python
produk3 = Produk.dari_data(data_produk)
```

Method mengambil setiap data dari dictionary:

```python
data["kode_produk"]
data["nama_produk"]
data["kategori"]
data["harga"]
data["stok"]
```

Kemudian digunakan untuk membuat object `Produk`.

`cls` mengacu pada class `Produk`.

---

## 3.10 Static Method `validasi_harga()`

```python
@staticmethod
def validasi_harga(harga):
    return harga > 0
```

Static method digunakan untuk memeriksa apakah harga lebih dari 0.

Jika harga lebih dari 0, hasilnya:

```text
True
```

Jika harga 0 atau kurang, hasilnya:

```text
False
```

Method ini tidak membutuhkan object tertentu sehingga dapat dipanggil langsung melalui class:

```python
Produk.validasi_harga(12000)
```

---

# 4. Penjelasan Class `Pelanggan`

Class `Pelanggan` digunakan untuk menyimpan dan mengelola data pelanggan minimarket.

## 4.1 Atribut Kelas

```python
nama_minimarket = "Minimarket Muhammad Fajar"
jumlah_pelanggan = 0
status_member = "Pelanggan Minimarket"
```

`nama_minimarket` menyimpan nama minimarket.

`jumlah_pelanggan` digunakan untuk menghitung jumlah object pelanggan yang dibuat.

`status_member` menyimpan status member yang digunakan oleh pelanggan.

---

## 4.2 Constructor Pelanggan

```python
def __init__(self, nama_pelanggan, no_telepon):
```

Constructor menerima dua data:

* `nama_pelanggan`
* `no_telepon`

Kemudian disimpan:

```python
self.nama_pelanggan = nama_pelanggan
self.no_telepon = no_telepon
```

Saldo awal pelanggan ditentukan sebesar 0:

```python
self.__saldo = 0
```

Saldo dibuat private menggunakan `__saldo`.

---

## 4.3 Menghitung Jumlah Pelanggan

```python
Pelanggan.jumlah_pelanggan += 1
```

Setiap kali object pelanggan dibuat, jumlah pelanggan bertambah satu.

Pada program terdapat:

```python
pelanggan1 = Pelanggan(...)
pelanggan2 = Pelanggan(...)
```

Sehingga jumlah pelanggan menjadi:

```text
2
```

---

## 4.4 Method `tampilkan_pelanggan()`

```python
def tampilkan_pelanggan(self):
```

Digunakan untuk menampilkan data pelanggan.

```python
print("Nama       :", self.nama_pelanggan)
print("No. Telepon:", self.no_telepon)
print("Saldo      : Rp", self.__saldo)
```

Data yang ditampilkan adalah nama, nomor telepon, dan saldo.

---

## 4.5 Method `tambah_saldo()`

```python
def tambah_saldo(self, jumlah):
```

Digunakan untuk menambahkan saldo pelanggan.

```python
if jumlah > 0:
```

Program memeriksa apakah jumlah saldo lebih dari 0.

Jika benar:

```python
self.__saldo += jumlah
```

saldo akan bertambah.

Jika tidak:

```python
print("Jumlah saldo harus lebih dari 0.")
```

program memberikan pesan kesalahan.

---

## 4.6 Getter `saldo`

```python
@property
def saldo(self):
    return self.__saldo
```

Getter digunakan untuk membaca saldo yang tersimpan pada atribut private `__saldo`.

Contoh:

```python
print(pelanggan1.saldo)
```

---

## 4.7 Setter `saldo`

```python
@saldo.setter
def saldo(self, saldo_baru):
```

Setter digunakan untuk mengubah saldo.

Program terlebih dahulu melakukan validasi:

```python
if saldo_baru < 0:
    raise ValueError("Saldo tidak boleh negatif.")
```

Jika saldo baru kurang dari 0, perubahan ditolak.

Jika valid:

```python
self.__saldo = saldo_baru
```

saldo akan diubah.

---

## 4.8 Class Method `ubah_status_member()`

```python
@classmethod
def ubah_status_member(cls, status_baru):
```

Digunakan untuk mengubah status member pada class `Pelanggan`.

```python
if status_baru.strip() == "":
```

`strip()` digunakan untuk menghilangkan spasi di awal dan akhir teks.

Program memeriksa apakah status yang diberikan kosong.

Jika kosong:

```python
raise ValueError("Status tidak boleh kosong.")
```

Jika valid:

```python
cls.status_member = status_baru
```

status member diubah.

---

## 4.9 Static Method `validasi_no_telepon()`

```python
@staticmethod
def validasi_no_telepon(no_telepon):
```

Digunakan untuk memvalidasi nomor telepon.

```python
return no_telepon.isdigit() and len(no_telepon) >= 10
```

Terdapat dua pemeriksaan:

* `isdigit()` memastikan semua karakter berupa angka.
* `len(no_telepon) >= 10` memastikan panjang nomor minimal 10 karakter.

Kedua kondisi harus benar agar hasilnya `True`.

---

# 5. Penjelasan Class `Transaksi`

Class `Transaksi` digunakan untuk mengelola transaksi pembelian pelanggan.

## 5.1 Atribut Kelas

```python
nama_minimarket = "Minimarket Muhammad Fajar"
jumlah_transaksi = 0
biaya_layanan = 2000
```

`nama_minimarket` menyimpan nama minimarket.

`jumlah_transaksi` digunakan untuk menghitung jumlah transaksi.

`biaya_layanan` menyimpan biaya layanan setiap transaksi.

---

## 5.2 Constructor Transaksi

```python
def __init__(self, nomor_transaksi, pelanggan):
```

Constructor menerima:

* `nomor_transaksi`
* `pelanggan`

Data tersebut disimpan:

```python
self.nomor_transaksi = nomor_transaksi
self.pelanggan = pelanggan
```

Total transaksi dimulai dari 0:

```python
self.__total = 0
```

Total dibuat private menggunakan `__total`.

---

## 5.3 Menghitung Jumlah Transaksi

```python
Transaksi.jumlah_transaksi += 1
```

Setiap object transaksi dibuat, jumlah transaksi bertambah satu.

Pada program dibuat:

```python
transaksi1 = Transaksi(...)
transaksi2 = Transaksi(...)
```

Maka jumlah transaksi menjadi 2.

---

# 6. Method `tambah_produk()`

```python
def tambah_produk(self, produk, jumlah):
```

Method ini digunakan untuk memasukkan produk ke dalam transaksi.

Method menerima dua parameter:

* `produk` → object dari class `Produk`.
* `jumlah` → jumlah produk yang dibeli.

### Pemeriksaan pertama

```python
if jumlah <= 0:
```

Jika jumlah pembelian 0 atau kurang, program menolak transaksi.

### Pemeriksaan kedua

```python
elif jumlah > produk.stok:
```

Program memeriksa apakah jumlah yang dibeli lebih banyak daripada stok yang tersedia.

Jika stok tidak mencukupi:

```python
print("Stok produk tidak mencukupi.")
```

### Jika semua valid

```python
self.__total += produk.harga * jumlah
```

Total transaksi ditambah berdasarkan rumus:

```text
harga produk × jumlah pembelian
```

Kemudian stok dikurangi:

```python
produk.stok = produk.stok - jumlah
```

Karena `stok` menggunakan setter, perubahan stok tetap melewati validasi.

---

# 7. Method `tampilkan_transaksi()`

```python
def tampilkan_transaksi(self):
```

Digunakan untuk menampilkan informasi transaksi.

```python
print("Nomor Transaksi :", self.nomor_transaksi)
```

Menampilkan nomor transaksi.

```python
print("Pelanggan       :", self.pelanggan.nama_pelanggan)
```

Menampilkan nama pelanggan yang melakukan transaksi.

```python
print("Total           : Rp", self.__total)
```

Menampilkan total harga produk.

```python
print("Biaya Layanan   : Rp", Transaksi.biaya_layanan)
```

Menampilkan biaya layanan.

```python
print("Total Bayar     : Rp", self.__total + Transaksi.biaya_layanan)
```

Menampilkan jumlah yang harus dibayar.

Rumusnya:

```text
Total Bayar = Total Produk + Biaya Layanan
```

---

# 8. Getter dan Setter `total`

Getter:

```python
@property
def total(self):
    return self.__total
```

Digunakan untuk membaca total transaksi.

Contoh:

```python
print(transaksi1.total)
```

Setter:

```python
@total.setter
def total(self, total_baru):
```

Digunakan untuk mengubah total transaksi.

Program memastikan total tidak boleh negatif:

```python
if total_baru < 0:
    raise ValueError("Total transaksi tidak boleh negatif.")
```

Jika valid:

```python
self.__total = total_baru
```

total transaksi akan diubah.

---

# 9. Class Method `ubah_biaya_layanan()`

```python
@classmethod
def ubah_biaya_layanan(cls, biaya_baru):
```

Digunakan untuk mengubah biaya layanan pada class `Transaksi`.

Program memeriksa:

```python
if biaya_baru < 0:
```

Biaya layanan tidak boleh negatif.

Jika valid:

```python
cls.biaya_layanan = biaya_baru
```

biaya layanan akan diubah.

Pada program:

```python
Transaksi.ubah_biaya_layanan(3000)
```

berarti biaya layanan yang sebelumnya Rp2.000 diubah menjadi Rp3.000.

---

# 10. Static Method `hitung_total()`

```python
@staticmethod
def hitung_total(harga, jumlah):
```

Digunakan untuk menghitung total harga berdasarkan harga dan jumlah barang.

```python
if harga < 0 or jumlah < 0:
    return 0
```

Jika harga atau jumlah bernilai negatif, method mengembalikan nilai `0`.

Jika keduanya valid:

```python
return harga * jumlah
```

Contoh:

```python
Transaksi.hitung_total(10000, 3)
```

hasilnya:

```text
30000
```

karena:

```text
Rp10.000 × 3 = Rp30.000
```

---

# 11. Pembuatan Object Produk

Program membuat tiga object produk.

```python
produk1 = Produk(
    "001",
    "Chitato",
    "Snack",
    12000,
    20
)
```

Membuat produk Chitato dengan stok awal 20.

```python
produk2 = Produk(
    "002",
    "Teh Botol",
    "Minuman",
    5000,
    30
)
```

Membuat produk Teh Botol dengan stok awal 30.

Produk ketiga dibuat melalui class method:

```python
produk3 = Produk.dari_data(data_produk)
```

Produk tersebut memiliki data:

```text
Kode     : 003
Nama     : Roti Coklat
Kategori : Makanan
Harga    : Rp8000
Stok     : 15
```

Karena terdapat tiga object produk, maka:

```python
Produk.jumlah_produk
```

bernilai:

```text
3
```

---

# 12. Pengujian Getter dan Setter Stok

Program membaca stok menggunakan getter:

```python
print("Stok produk 1:", produk1.stok)
```

Kemudian mengubah stok menggunakan setter:

```python
produk1.stok = 30
```

Program juga menguji nilai yang tidak valid:

```python
try:
    produk1.stok = -10
except ValueError as e:
    print("Validasi:", e)
```

Ketika `-10` diberikan, setter menghasilkan `ValueError`.

Program kemudian menangkap kesalahan tersebut menggunakan:

```python
except ValueError as e:
```

dan menampilkan pesan:

```text
Validasi: Stok tidak boleh negatif.
```

---

# 13. Pengujian Static Method Produk

Program menguji:

```python
Produk.validasi_harga(12000)
```

Karena 12000 lebih besar dari 0, hasilnya:

```text
True
```

Kemudian:

```python
Produk.validasi_harga(0)
```

Karena 0 tidak lebih besar dari 0, hasilnya:

```text
False
```

---

# 14. Pengujian Data Pelanggan

Program membuat dua pelanggan:

```python
pelanggan1 = Pelanggan(
    "Andi",
    "081234567890"
)
```

dan:

```python
pelanggan2 = Pelanggan(
    "Budi",
    "082345678901"
)
```

Setiap pelanggan memiliki saldo awal:

```text
Rp0
```

Karena terdapat dua object pelanggan:

```python
Pelanggan.jumlah_pelanggan
```

bernilai:

```text
2
```

---

# 15. Pengujian Saldo Pelanggan

Program menambahkan saldo Andi:

```python
pelanggan1.tambah_saldo(100000)
```

Saldo menjadi:

```text
Rp100000
```

Kemudian saldo diubah menggunakan setter:

```python
pelanggan1.saldo = 150000
```

Saldo menjadi:

```text
Rp150000
```

Program juga menguji saldo negatif:

```python
try:
    pelanggan1.saldo = -50000
except ValueError as e:
    print("Validasi:", e)
```

Hasilnya adalah pesan:

```text
Validasi: Saldo tidak boleh negatif.
```

---

# 16. Pengujian Nomor Telepon

Program menguji nomor:

```python
Pelanggan.validasi_no_telepon("081234567890")
```

Nomor tersebut terdiri dari angka dan memiliki panjang minimal 10 karakter sehingga hasilnya:

```text
True
```

Kemudian diuji:

```python
Pelanggan.validasi_no_telepon("123")
```

Nomor tersebut kurang dari 10 karakter sehingga hasilnya:

```text
False
```

---

# 17. Pembuatan Transaksi

Program membuat dua transaksi:

```python
transaksi1 = Transaksi(
    "TRX001",
    pelanggan1
)
```

Transaksi `TRX001` dimiliki oleh pelanggan Andi.

Kemudian:

```python
transaksi2 = Transaksi(
    "TRX002",
    pelanggan2
)
```

Transaksi `TRX002` dimiliki oleh pelanggan Budi.

---

# 18. Pengujian Transaksi 1

Pada transaksi pertama terdapat:

```python
transaksi1.tambah_produk(produk1, 2)
```

Artinya Andi membeli 2 Chitato.

Harga Chitato:

```text
Rp12.000
```

Maka:

```text
Rp12.000 × 2 = Rp24.000
```

Kemudian:

```python
transaksi1.tambah_produk(produk2, 3)
```

Andi membeli 3 Teh Botol.

Perhitungannya:

```text
Rp5.000 × 3 = Rp15.000
```

Total produk:

```text
Rp24.000 + Rp15.000 = Rp39.000
```

Biaya layanan awal:

```text
Rp2.000
```

Sehingga total pembayaran:

```text
Rp39.000 + Rp2.000 = Rp41.000
```

---

# 19. Pengujian Transaksi 2

Transaksi kedua:

```python
transaksi2.tambah_produk(produk3, 2)
```

Pelanggan Budi membeli 2 Roti Coklat.

Harga Roti Coklat:

```text
Rp8.000
```

Perhitungannya:

```text
Rp8.000 × 2 = Rp16.000
```

Dengan biaya layanan Rp2.000, total pembayaran:

```text
Rp16.000 + Rp2.000 = Rp18.000
```

---

# 20. Pengujian Getter dan Setter Total

Program mengambil total menggunakan getter:

```python
print("Total transaksi 1:", transaksi1.total)
```

Kemudian total transaksi diubah:

```python
transaksi1.total = 50000
```

Total transaksi 1 menjadi:

```text
Rp50.000
```

Program juga menguji nilai negatif:

```python
try:
    transaksi1.total = -10000
except ValueError as e:
    print("Validasi:", e)
```

Program akan menampilkan:

```text
Validasi: Total transaksi tidak boleh negatif.
```

---

# 21. Pengujian Class Method Transaksi

Program menjalankan:

```python
Transaksi.ubah_biaya_layanan(3000)
```

Perintah tersebut mengubah biaya layanan dari:

```text
Rp2.000
```

menjadi:

```text
Rp3.000
```

Setelah itu:

```python
transaksi1.tampilkan_transaksi()
```

akan menampilkan biaya layanan baru sebesar Rp3.000.

---

# 22. Pengujian Atribut Kelas

Pada bagian akhir program terdapat:

```python
print("Nama Minimarket :", Produk.nama_minimarket)
print("Jumlah Produk   :", Produk.jumlah_produk)
```

Bagian tersebut digunakan untuk melihat atribut kelas `Produk`.

Kemudian:

```python
print("Jumlah Pelanggan:", Pelanggan.jumlah_pelanggan)
print("Status Member   :", Pelanggan.status_member)
```

digunakan untuk melihat atribut kelas `Pelanggan`.

Sedangkan:

```python
print("Jumlah Transaksi:", Transaksi.jumlah_transaksi)
print("Biaya Layanan   :", Transaksi.biaya_layanan)
```

digunakan untuk melihat atribut kelas `Transaksi`.

---

# 23. Konsep OOP yang Digunakan

## 23.1 Class

Program memiliki tiga class:

```python
Produk
Pelanggan
Transaksi
```

Class digunakan sebagai rancangan untuk membuat object.

---

## 23.2 Object

Contoh object:

```python
produk1
produk2
produk3
pelanggan1
pelanggan2
transaksi1
transaksi2
```

Object merupakan hasil pembuatan dari sebuah class.

Contohnya:

```python
produk1 = Produk(...)
```

berarti `produk1` merupakan object dari class `Produk`.

---

## 23.3 Encapsulation

Encapsulation diterapkan pada data yang bersifat private, yaitu:

```python
self.__stok
self.__saldo
self.__total
```

Data tersebut tidak digunakan secara langsung dari luar class.

Akses dan perubahan dilakukan melalui getter dan setter.

Contohnya:

```python
produk1.stok
```

untuk membaca stok, dan:

```python
produk1.stok = 30
```

untuk mengubah stok.

---

## 23.4 Getter

Getter digunakan untuk mengambil nilai atribut private.

Contohnya:

```python
@property
def stok(self):
    return self.__stok
```

Getter juga terdapat pada:

* `Produk.stok`
* `Pelanggan.saldo`
* `Transaksi.total`

---

## 23.5 Setter

Setter digunakan untuk mengubah nilai atribut private sekaligus melakukan validasi.

Contohnya:

```python
@stok.setter
def stok(self, stok_baru):
```

Setter terdapat pada:

* `Produk.stok`
* `Pelanggan.saldo`
* `Transaksi.total`

---

## 23.6 Class Method

Class method ditandai dengan:

```python
@classmethod
```

Class method digunakan untuk mengakses atau mengubah data yang berkaitan dengan class.

Dalam program terdapat:

```python
Produk.dari_data()
Pelanggan.ubah_status_member()
Transaksi.ubah_biaya_layanan()
```

---

## 23.7 Static Method

Static method ditandai dengan:

```python
@staticmethod
```

Static method digunakan untuk fungsi yang tidak membutuhkan data object maupun class tertentu.

Dalam program terdapat:

```python
Produk.validasi_harga()
Pelanggan.validasi_no_telepon()
Transaksi.hitung_total()
```

---

# 24. Alur Kerja Program

Secara umum, alur program adalah:

```text
Program dimulai
       ↓
Membuat object Produk
       ↓
Menampilkan data produk
       ↓
Menambah dan mengubah stok
       ↓
Melakukan validasi stok
       ↓
Menguji static method Produk
       ↓
Membuat Produk dari dictionary
       ↓
Membuat object Pelanggan
       ↓
Menampilkan data pelanggan
       ↓
Menambah dan mengubah saldo
       ↓
Melakukan validasi saldo
       ↓
Memvalidasi nomor telepon
       ↓
Mengubah status member
       ↓
Membuat object Transaksi
       ↓
Menambahkan produk ke transaksi
       ↓
Mengurangi stok produk
       ↓
Menghitung total transaksi
       ↓
Menguji getter dan setter total
       ↓
Mengubah biaya layanan
       ↓
Menampilkan atribut kelas
       ↓
Program selesai
```

---

# 26. Panduan Pengujian

Pengujian dilakukan untuk memastikan setiap bagian program dapat berjalan sesuai dengan fungsi yang dibuat.

## Pengujian 1 — Data Produk

Bagian yang diuji:

```python
produk1.tampilkan_produk()
produk2.tampilkan_produk()
```

**Tujuan:** memastikan data produk dapat ditampilkan.

**Hasil yang diharapkan:** kode, nama, kategori, harga, dan stok produk ditampilkan dengan benar.

---

## Pengujian 2 — Menambah Stok

Perintah:

```python
produk1.tambah_stok(5)
```

Stok awal Chitato adalah 20.

Setelah ditambah 5:

```text
20 + 5 = 25
```

**Hasil yang diharapkan:** stok Chitato menjadi 25.

---

## Pengujian 3 — Setter Stok Valid

Perintah:

```python
produk1.stok = 30
```

**Hasil yang diharapkan:** stok berubah menjadi 30.

---

## Pengujian 4 — Setter Stok Tidak Valid

Perintah:

```python
produk1.stok = -10
```

**Hasil yang diharapkan:**

```text
Validasi: Stok tidak boleh negatif.
```

---

## Pengujian 5 — Validasi Harga

Perintah:

```python
Produk.validasi_harga(12000)
Produk.validasi_harga(0)
```

**Hasil yang diharapkan:**

```text
True
False
```

---

## Pengujian 6 — Data Pelanggan

Perintah:

```python
pelanggan1.tampilkan_pelanggan()
pelanggan2.tampilkan_pelanggan()
```

**Tujuan:** memastikan data pelanggan dapat ditampilkan.

---

## Pengujian 7 — Menambah Saldo

Perintah:

```python
pelanggan1.tambah_saldo(100000)
```

**Hasil yang diharapkan:** saldo Andi menjadi Rp100.000.

---

## Pengujian 8 — Setter Saldo

Perintah:

```python
pelanggan1.saldo = 150000
```

**Hasil yang diharapkan:** saldo Andi berubah menjadi Rp150.000.

Kemudian diuji dengan:

```python
pelanggan1.saldo = -50000
```

**Hasil yang diharapkan:** program menolak nilai tersebut dan menampilkan pesan validasi.

---

## Pengujian 9 — Validasi Nomor Telepon

Perintah:

```python
Pelanggan.validasi_no_telepon("081234567890")
```

**Hasil yang diharapkan:**

```text
True
```

Kemudian:

```python
Pelanggan.validasi_no_telepon("123")
```

**Hasil yang diharapkan:**

```text
False
```

---

## Pengujian 10 — Transaksi

Pada transaksi pertama:

```python
transaksi1.tambah_produk(produk1, 2)
transaksi1.tambah_produk(produk2, 3)
```

**Hasil yang diharapkan:**

* 2 Chitato berhasil ditambahkan.
* 3 Teh Botol berhasil ditambahkan.
* Total produk menjadi Rp39.000.
* Stok Chitato berkurang 2.
* Stok Teh Botol berkurang 3.

---

## Pengujian 11 — Transaksi Produk Kedua

Perintah:

```python
transaksi2.tambah_produk(produk3, 2)
```

**Hasil yang diharapkan:**

* 2 Roti Coklat berhasil ditambahkan.
* Total produk menjadi Rp16.000.
* Stok Roti Coklat berkurang dari 15 menjadi 13.

---

## Pengujian 12 — Setter Total Transaksi

Perintah:

```python
transaksi1.total = 50000
```

**Hasil yang diharapkan:** total transaksi 1 menjadi Rp50.000.

Kemudian diuji:

```python
transaksi1.total = -10000
```

**Hasil yang diharapkan:**

```text
Validasi: Total transaksi tidak boleh negatif.
```

---

## Pengujian 13 — Static Method Transaksi

Perintah:

```python
hasil = Transaksi.hitung_total(10000, 3)
```

**Hasil yang diharapkan:**

```text
30000
```

karena:

```text
Rp10.000 × 3 = Rp30.000
```

---

## Pengujian 14 — Mengubah Biaya Layanan

Perintah:

```python
Transaksi.ubah_biaya_layanan(3000)
```

**Hasil yang diharapkan:** biaya layanan berubah dari Rp2.000 menjadi Rp3.000.

---

# 27. Ringkasan Hasil Pengujian

| No. | Pengujian              | Kondisi                 | Hasil yang Diharapkan   |
| --- | ---------------------- | ----------------------- | ----------------------- |
| 1   | Menampilkan produk     | Data produk tersedia    | Data produk tampil      |
| 2   | Menambah stok          | `+5`                    | Stok bertambah          |
| 3   | Setter stok            | `30`                    | Stok berubah menjadi 30 |
| 4   | Validasi stok          | `-10`                   | Ditolak                 |
| 5   | Validasi harga         | `12000` dan `0`         | `True` dan `False`      |
| 6   | Menampilkan pelanggan  | Data tersedia           | Data pelanggan tampil   |
| 7   | Menambah saldo         | `100000`                | Saldo bertambah         |
| 8   | Setter saldo           | `150000`                | Saldo berubah           |
| 9   | Validasi saldo         | `-50000`                | Ditolak                 |
| 10  | Validasi nomor telepon | Nomor valid             | `True`                  |
| 11  | Validasi nomor telepon | `"123"`                 | `False`                 |
| 12  | Menambah produk        | Stok mencukupi          | Produk masuk transaksi  |
| 13  | Mengurangi stok        | Produk dibeli           | Stok berkurang          |
| 14  | Getter total           | Data transaksi tersedia | Total dapat dibaca      |
| 15  | Setter total           | `50000`                 | Total berubah           |
| 16  | Validasi total         | `-10000`                | Ditolak                 |
| 17  | Hitung total           | `10000 × 3`             | `30000`                 |
| 18  | Ubah biaya layanan     | `3000`                  | Biaya berubah           |

---