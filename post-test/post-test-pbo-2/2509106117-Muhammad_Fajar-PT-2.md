# Sistem Minimarket Untuk Penjualan Snack, Minuman, dan Makanan

## 1. Deskripsi Program

Program ini merupakan sistem sederhana untuk mengelola kegiatan penjualan pada **Minimarket Muhammad Fajar**.

Program dibuat menggunakan konsep **Pemrograman Berorientasi Objek (PBO)** dengan bahasa Python.

Program dapat digunakan untuk:

* Mengelola data produk.
* Menampilkan data produk.
* Menambah stok produk.
* Mengubah dan memvalidasi stok.
* Memvalidasi harga.
* Mengelola data pelanggan.
* Mengelola saldo pelanggan.
* Membuat transaksi.
* Menambahkan produk ke transaksi.
* Menghitung total transaksi.
* Mengatur biaya layanan.
* Menerapkan relasi UML.
* Menerapkan inheritance.

---

## 2. Struktur Class

Program utama memiliki beberapa class, yaitu:

### Produk

`Produk` merupakan class yang digunakan untuk menyimpan data umum produk.

Atribut yang dimiliki antara lain:

* `kode_produk`
* `nama_produk`
* `kategori`
* `harga`
* `__stok`
* `_jenis_produk`

`__stok` merupakan atribut private sehingga data stok tidak digunakan secara langsung dari luar class.

`_jenis_produk` merupakan atribut protected yang dapat digunakan oleh subclass.

Method yang terdapat pada class `Produk` antara lain:

* `tampilkan_produk()`
* `tambah_stok()`
* `validasi_harga()`
* `ambil_data()`

Class `Produk` juga menggunakan property `stok` sebagai getter dan setter untuk mengakses serta mengubah stok dengan validasi.

---

### Snack

`Snack` merupakan subclass dari `Produk`.

Karena Snack merupakan salah satu jenis produk, maka hubungan:

```text
Snack adalah Produk
```

merupakan inheritance.

Atribut khusus pada `Snack` adalah:

```text
rasa
```

Class `Snack` juga melakukan overriding terhadap method:

```text
tampilkan_produk()
```

sehingga informasi rasa dapat ditampilkan.

---

### Minuman

`Minuman` merupakan subclass dari `Produk`.

Hubungannya adalah:

```text
Minuman adalah Produk
```

Atribut khusus pada `Minuman` adalah:

```text
ukuran
```

Contohnya:

```text
350 ml
600 ml
```

Class `Minuman` juga melakukan overriding terhadap method:

```text
tampilkan_produk()
```

---

### Pelanggan

Class `Pelanggan` digunakan untuk menyimpan data pelanggan.

Atribut yang digunakan antara lain:

* `nama_pelanggan`
* `no_telepon`
* `__saldo`

Class ini memiliki method untuk:

* Menampilkan data pelanggan.
* Menambah saldo.
* Mengubah saldo.
* Memvalidasi nomor telepon.
* Mengubah status member.

---

### Transaksi

Class `Transaksi` digunakan untuk mengelola transaksi pembelian.

Atribut utama:

* `nomor_transaksi`
* `pelanggan`
* `__total`

Method utama:

* `tambah_produk()`
* `tampilkan_transaksi()`
* `hitung_total()`
* `ubah_biaya_layanan()`

---

### DetailTransaksi

Class `DetailTransaksi` digunakan untuk menyimpan rincian produk yang dibeli dalam sebuah transaksi.

Atributnya:

* `produk`
* `jumlah`
* `subtotal`

Objek `DetailTransaksi` dibuat di dalam `TransaksiLengkap`.

Oleh karena itu, hubungan antara `TransaksiLengkap` dan `DetailTransaksi` merupakan **komposisi**.

---

### TransaksiLengkap

`TransaksiLengkap` merupakan subclass dari `Transaksi`.

Class ini digunakan untuk menambahkan penyimpanan detail transaksi tanpa mengubah struktur utama `Transaksi` pada Posttest 1.

Class ini memiliki atribut:

```text
_detail
```

dan method:

```text
tambah_produk()
tampilkan_detail()
```

---

### Minimarket

Class `Minimarket` digunakan untuk mengelola daftar produk yang tersedia.

Produk dibuat terlebih dahulu di luar class `Minimarket`, kemudian diberikan menggunakan method:

```text
tambah_produk()
```

Hubungan ini merupakan **agregasi**.

---

## 3. Relasi UML

Program menerapkan tiga relasi UML yang diminta pada Posttest 2.

### 3.1 Asosiasi

Asosiasi diterapkan antara:

```text
Transaksi → Produk
```

Contohnya:

```python
transaksi3.tambah_produk(produk3, 1)
```

Objek `Produk` diberikan sebagai parameter kepada method transaksi.

Produk tidak dibuat oleh transaksi dan tidak menjadi bagian yang dibuat secara khusus oleh transaksi.

---

### 3.2 Agregasi

Agregasi diterapkan antara:

```text
Minimarket ◇── Produk
```

Objek produk dibuat secara mandiri terlebih dahulu.

Contohnya:

```python
produk1 = Produk(...)
produk2 = Produk(...)
```

Kemudian objek tersebut dimasukkan ke minimarket:

```python
minimarket1.tambah_produk(produk1)
minimarket1.tambah_produk(produk2)
```

Dengan demikian, `Minimarket` hanya menampung referensi objek produk yang sudah dibuat di luar class.

---

### 3.3 Komposisi

Komposisi diterapkan antara:

```text
TransaksiLengkap ◆── DetailTransaksi
```

Objek `DetailTransaksi` dibuat langsung di dalam method `tambah_produk()` pada `TransaksiLengkap`.

Contohnya:

```python
detail = DetailTransaksi(
    produk,
    jumlah,
    produk.harga * jumlah
)
```

Dengan demikian, detail transaksi merupakan bagian dari transaksi.

---

## 4. Inheritance

Program menerapkan inheritance dengan struktur:

```text
              Produk
             /      \
            /        \
         Snack      Minuman
```

`Produk` berperan sebagai **superclass**.

`Snack` dan `Minuman` berperan sebagai **subclass**.

### Superclass

```text
Produk
```

Menyediakan atribut dan method umum yang dapat digunakan oleh subclass.

### Subclass

```text
Snack
Minuman
```

Kedua subclass mewarisi atribut dan method dari `Produk`.

---

## 5. Penggunaan super()

Subclass `Snack` menggunakan:

```python
super().__init__(
    kode_produk,
    nama_produk,
    "Snack",
    harga,
    stok
)
```

Sedangkan `Minuman` menggunakan:

```python
super().__init__(
    kode_produk,
    nama_produk,
    "Minuman",
    harga,
    stok
)
```

`super().__init__()` digunakan untuk memanggil constructor milik superclass `Produk`.

Dengan demikian, atribut umum produk tidak perlu ditulis ulang pada subclass.

---

## 6. Atribut Khusus Subclass

Setiap subclass memiliki atribut khusus.

### Snack

Memiliki atribut:

```text
rasa
```

Contoh:

```text
Keju
Balado
Barbeque
```

### Minuman

Memiliki atribut:

```text
ukuran
```

Contoh:

```text
350 ml
600 ml
```

Atribut tersebut membedakan masing-masing subclass.

---

## 7. Method Overriding

Method:

```text
tampilkan_produk()
```

yang terdapat pada class `Produk` dibuat kembali pada class:

```text
Snack
Minuman
```

Tujuannya adalah memberikan perilaku tambahan sesuai jenis produk.

Pada `Snack`, method menampilkan:

```text
Rasa
```

Sedangkan pada `Minuman`, method menampilkan:

```text
Ukuran
```

---

## 8. Protected dan Private

Program menggunakan dua tingkat akses yang diminta pada Posttest 2.

### Protected

```python
self._jenis_produk = kategori
```

Atribut `_jenis_produk` merupakan atribut protected.

Atribut ini digunakan oleh subclass `Snack` dan `Minuman`.

Contohnya:

```python
print("Kategori :", self._jenis_produk)
```

### Private

```python
self.__stok = stok
```

Atribut `__stok` merupakan atribut private pada class `Produk`.

Stok tidak digunakan secara langsung dari subclass. Pengaksesannya dilakukan melalui property:

```text
stok
```

Dengan demikian, data stok tetap memiliki perlindungan dan validasi.

---

## 9. Panduan Pengujian

Jalankan program Python dari awal sampai akhir.

### Pengujian Produk

Program akan menampilkan data:

* Chitato
* Teh Botol
* Roti Coklat

Kemudian program menguji:

* Penambahan stok.
* Getter stok.
* Setter stok.
* Validasi stok.
* Static method.
* Class method.

### Pengujian Pelanggan

Program membuat:

* Andi
* Budi

Kemudian menguji:

* Data pelanggan.
* Penambahan saldo.
* Getter dan setter saldo.
* Validasi saldo.
* Validasi nomor telepon.
* Perubahan status member.

### Pengujian Transaksi

Program membuat beberapa transaksi dan menguji:

* Penambahan produk.
* Pemeriksaan stok.
* Perhitungan total.
* Getter total.
* Setter total.
* Validasi total.
* Biaya layanan.

### Pengujian Inheritance

Program membuat:

```python
snack1 = Snack(...)
minuman1 = Minuman(...)
```

Kemudian menjalankan:

```python
snack1.tampilkan_produk()
minuman1.tampilkan_produk()
```

Pengujian ini menunjukkan bahwa kedua subclass memiliki atribut dan method dari superclass serta memiliki atribut khusus masing-masing.

### Pengujian Protected

Program menjalankan:

```python
print(snack1._jenis_produk)
print(minuman1._jenis_produk)
```

Hasilnya menunjukkan bahwa subclass dapat menggunakan atribut protected dari superclass.

### Pengujian Agregasi

Program membuat objek `Minimarket`, kemudian memasukkan produk yang sudah dibuat sebelumnya:

```python
minimarket1.tambah_produk(produk1)
minimarket1.tambah_produk(produk2)
minimarket1.tambah_produk(produk3)
```

Hal ini menunjukkan bahwa objek produk dibuat secara mandiri kemudian ditampung oleh minimarket.

### Pengujian Komposisi

Program membuat:

```python
transaksi3 = TransaksiLengkap(
    "TRX003",
    pelanggan1
)
```

Kemudian menambahkan produk:

```python
transaksi3.tambah_produk(snack1, 2)
transaksi3.tambah_produk(minuman1, 3)
```

Setiap produk yang berhasil ditambahkan akan membuat objek `DetailTransaksi` di dalam transaksi.

### Pengujian Asosiasi

Program menggunakan:

```python
transaksi3.tambah_produk(produk3, 1)
```

Objek produk diberikan sebagai parameter kepada transaksi.

Hal tersebut menunjukkan bahwa transaksi menggunakan produk melalui parameter method.

---

## 10. Kesimpulan

Posttest 2 mengembangkan program Posttest 1 dengan menambahkan konsep hubungan antar class dan inheritance.

Konsep yang diterapkan adalah:

1. **Asosiasi** antara `Transaksi` dan `Produk`.
2. **Agregasi** antara `Minimarket` dan `Produk`.
3. **Komposisi** antara `TransaksiLengkap` dan `DetailTransaksi`.
4. **Inheritance** dengan `Produk` sebagai superclass serta `Snack` dan `Minuman` sebagai subclass.
5. **super().**init**()** pada subclass.
6. **Atribut khusus** pada setiap subclass.
7. **Method overriding** pada `tampilkan_produk()`.
8. **Protected attribute** `_jenis_produk`.
9. **Private attribute** `__stok`.

Dengan penerapan tersebut, program tetap mempertahankan fungsi utama Posttest 1 sekaligus memenuhi konsep yang diminta pada Posttest 2.
