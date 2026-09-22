class Penumpang:
    instansi = "DAMRI Samarinda"
    total_penumpang = 0

    def __init__(self, id_penumpang, nama, no_hp):
        self.id_penumpang = id_penumpang
        self.nama = nama
        self.__no_hp = no_hp  
        Penumpang.total_penumpang += 1

    @property
    def no_hp(self):
        return self.__no_hp

    @no_hp.setter
    def no_hp(self, nomor_baru):
        if Penumpang.validasi_hp(nomor_baru):
            self.__no_hp = nomor_baru
            print(f"   [SUCCESS] No HP {self.nama} diperbarui -> {self.__no_hp}")
        else:
            print(f"   [REJECTED] Penolakan: Nomor '{nomor_baru}' tidak valid! Harus angka (10-13 digit).")

    def profil_ringkas(self):
        print(f"   * [{self.id_penumpang}] {self.nama:<15} | Kontak: {self.__no_hp}")

    @classmethod
    def dari_dictionary(cls, data):
        return cls(data["id"], data["nama"], data["hp"])

    @staticmethod
    def validasi_hp(nomor):
        return nomor.isdigit() and 10 <= len(nomor) <= 13


class BusDAMRI:
    slogan = "Aman, Nyaman, dan Terjangkau"
    total_bus = 0

    def __init__(self, kode_bus, rute, tarif, kursi_tersedia):
        self.kode_bus = kode_bus
        self.rute = rute
        self.__tarif = tarif               
        self.__kursi_tersedia = kursi_tersedia 
        BusDAMRI.total_bus += 1

    @property
    def tarif(self):
        return self.__tarif

    @tarif.setter
    def tarif(self, tarif_baru):
        if tarif_baru > 0:
            self.__tarif = tarif_baru
            print(f"   [SUCCESS] Tarif {self.kode_bus} diperbarui -> Rp {self.__tarif:,}")
        else:
            print(f"   [REJECTED] Penolakan: Tarif Rp {tarif_baru} tidak valid! (Harus > 0)")

    @property
    def kursi_tersedia(self):
        return self.__kursi_tersedia

    def info_armada(self):
        print(f"   * [{self.kode_bus}] Rute: {self.rute:<24} | Tarif: Rp {self.__tarif:>7,} | Sisa Kursi: {self.__kursi_tersedia}")

    @classmethod
    def ganti_slogan(cls, slogan_baru):
        cls.slogan = slogan_baru

    @staticmethod
    def hitung_diskon(harga, persen):
        return harga * (persen / 100)


class TiketBus:
    biaya_layanan = 3000
    total_tiket = 0

    def __init__(self, id_tiket, tanggal, penumpang, bus):
        self.id_tiket = id_tiket
        self.tanggal = tanggal
        self.penumpang = penumpang  
        self.bus = bus              
        self.__total_bayar = 0      
        self.hitung_total()
        TiketBus.total_tiket += 1

    @property
    def total_bayar(self):
        return self.__total_bayar

    def hitung_total(self):
        self.__total_bayar = self.bus.tarif + TiketBus.biaya_layanan

    def cetak_struk(self):
        print(f"   --------------------------------------------------")
        print(f"   STRUK TIKET : {self.id_tiket} ({self.tanggal})")
        print(f"   Penumpang   : {self.penumpang.nama} [{self.penumpang.id_penumpang}]")
        print(f"   Armada Bus  : {self.bus.kode_bus} - {self.bus.rute}")
        print(f"   Total Bayar : Rp {self.__total_bayar:,} (Termasuk Admin Rp {TiketBus.biaya_admin_layanan():,})")
        print(f"   --------------------------------------------------")

    @classmethod
    def set_biaya_admin(cls, nominal):
        if nominal >= 0:
            cls.biaya_layanan = nominal

    @staticmethod
    def biaya_admin_layanan():
        return TiketBus.biaya_layanan


if __name__ == "__main__":
    print("================================================")
    print("   SISTEM INFORMASI TIKET BUS DAMRI SAMARINDA   ")
    print("================================================")

    b1 = BusDAMRI("DMR-01", "Samarinda - Balikpapan", 60000, 20)
    b2 = BusDAMRI("DMR-02", "Samarinda - Sangatta", 85000, 15)

    p1 = Penumpang("PNP-01", "Karin Annasya", "081234567890")
    p2_data = {"id": "PNP-02", "nama": "Hamja Fadilah", "hp": "085244332211"}
    p2 = Penumpang.dari_dictionary(p2_data)

    print("\n[ 1. DAFTAR ARMADA BUS ]")
    b1.info_armada()
    b2.info_armada()

    print("\n[ 2. DAFTAR PENUMPANG ]")
    p1.profil_ringkas()
    p2.profil_ringkas()

    t1 = TiketBus("TKT-001", "23-09-2026", p1, b1)
    t2 = TiketBus("TKT-002", "23-09-2026", p2, b2)

    print("\n[ 3. TRANSAKSI PEMESANAN TIKET ]")
    t1.cetak_struk()
    t2.cetak_struk()

    print("\n[ 4. UJI VALIDASI ]")
    print("-- Uji Input Valid --")
    p1.no_hp = "081199887766"       #valid
    b1.tarif = 70000                #valid

    print("\n-- Uji Input Invalid --")
    p1.no_hp = "08123"              #ditolak: digit < 10
    p1.no_hp = "0812ABCDE123"       #ditolak: bukan angka
    b1.tarif = -20000               #ditolak: tarif < 0

    print("\n[ REKAP TOTAL DATA ]")
    print(f"   Total Bus Terdaftar       : {BusDAMRI.total_bus}")
    print(f"   Total Penumpang Terdaftar : {Penumpang.total_penumpang}")
    print(f"   Total Transaksi Tiket     : {TiketBus.total_tiket}")
    print("================================================")