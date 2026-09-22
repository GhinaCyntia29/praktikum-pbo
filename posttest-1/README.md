1. DESKRIPSI PROGRAM
    Program ini adalah sistem pemesanan tiket bus DAMRI Samarinda berbasis Python OOP. Program digunakan untuk mengelola data armada bus, data penumpang, serta memproses transaksi pemesanan tiket.
Fitur utama dalam program:
- Penumpang: Mengelola ID, nama, dan kontak penumpang beserta validasi nomor HP.
- BusDAMRI: Mengelola kode bus, rute, tarif, sisa kursi, dan validasi tarif.
- TiketBus: Menghubungkan data penumpang dengan bus untuk menghitung total biaya dan mencetak struk transaksi.

2. PENJELASAN STRUKTUR CLASS
    2.1 Penumpang
        Class ini digunakan untuk mencatat data calon penumpang bus.
    Class Attribute:
- instansi: Menyimpan nama instansi ("DAMRI Samarinda").
- total_penumpang: Menghitung total objek Penumpang yang dibuat.
    Instance Attribute:
- id_penumpang dan nama: Atribut publik untuk identitas penumpang.
- __no_hp: Atribut private untuk nomor kontak penumpang.
    Method:
- profil_ringkas(): Instance method untuk menampilkan data singkat penumpang.
- no_hp (Getter & Setter @property): Memvalidasi input nomor HP baru agar hanya menerima karakter angka dengan panjang 10 sampai 13 digit.
- dari_dictionary(): Class method untuk membuat objek Penumpang secara otomatis dari data bertipe dictionary.
- validasi_hp(): Static method sebagai fungsi pembantu untuk pengecekan format nomor HP.

    2.2 BusDAMRI
        Class ini digunakan untuk mengelola data armada bus DAMRI, rute, dan tarif.
    Class Attribute:
- slogan: Slogan operasional bus.
- total_bus: Menghitung total objek BusDAMRI yang dibuat.
    Instance Attribute:
- kode_bus dan rute: Atribut publik untuk armada dan tujuan.
- __tarif: Atribut private untuk harga dasar tiket bus.
- __kursi_tersedia: Atribut private untuk sisa kapasitas kursi.
    Method:
- info_armada(): Instance method untuk menampilkan rincian rute, tarif, dan ketersediaan kursi.
- tarif (Getter & Setter @property): Memvalidasi perubahan tarif agar nilainya harus lebih besar dari 0.
- ganti_slogan(): Class method untuk mengubah variabel slogan pada kelas.
- hitung_diskon(): Static method untuk mengkalkulasi besaran potongan harga tiket.

    2.3 TiketBus
        Class ini berfungsi sebagai objek transaksi yang menghubungkan objek Penumpang dengan objek BusDAMRI.
    Class Attribute:
- biaya_layanan: Biaya administrasi tambahan per transaksi (default: Rp 3.000).
- total_tiket: Menghitung total transaksi tiket yang berhasil dibuat.
    Instance Attribute:
- id_tiket dan tanggal: Data transaksi pemesanan.
- penumpang: Relasi objek dari class Penumpang.
- bus: Relasi objek dari class BusDAMRI.
- __total_bayar: Atribut private penampung total biaya (tarif bus + biaya layanan).
    Method:
- hitung_total(): Instance method untuk menghitung harga total tiket.
- cetak_struk(): Instance method untuk menampilkan struk transaksi pemesanan tiket.
- set_biaya_admin(): Class method untuk mengubah nominal biaya admin layanan.
- biaya_admin_layanan(): Static method untuk mengambil data biaya admin saat ini.

### Pengujian Program (Main Code)
1. Membuat & menampilkan data armada bus
   - b1 dan b2 dibuat langsung lewat __init__.
   - Keduanya ditampilkan menggunakan info_armada().

2. Membuat & menampilkan data penumpang
   - p1 (Karin Annasya) dibuat lewat __init__.
   - p2 (Hamja Fadilah) dibuat lewat dari_dictionary() (class method).
   - Keduanya ditampilkan menggunakan profil_ringkas().

3. Membuat & mencetak transaksi tiket
   - t1 = Pemesanan tiket Karin Annasya untuk bus DMR-01.
   - t2 = Pemesanan tiket Hamja Fadilah untuk bus DMR-02.
   - Struk pembayaran dicetak menggunakan cetak_struk().

4. Menguji setter dengan data valid
   - p1.no_hp = "081199887766" -> Berhasil diubah karena berupa angka (10-13 digit).
   - b1.tarif = 70000 -> Berhasil diubah karena nilai bernilai positif (> 0).

5. Menguji setter dengan data invalid
   - p1.no_hp = "08123" -> Ditolak karena kurang dari 10 digit.
   - p1.no_hp = "0812ABCDE123" -> Ditolak karena mengandung huruf.
   - b1.tarif = -20000 -> Ditolak karena nilai bernilai negatif (<= 0).
   Input yang tidak sesuai akan ditolak dan nilai lama tetap dipertahankan.

6. Menampilkan rekapitulasi atribut class
   - BusDAMRI.total_bus (2)
   - Penumpang.total_penumpang (2)
   - TiketBus.total_tiket (2)