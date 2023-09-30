class Divisi:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.karyawan = []

class Karyawan:
    def __init__(self, nip, nama):
        self.nip = nip
        self.nama = nama
        self.gaji = 0
        self.presensi = None 

    def set_gaji(self, gaji):
        self.gaji = gaji

class Manager(Karyawan):
    def __init__(self, nip, nama):
        super().__init__(nip, nama)
        self.bonus = 0

    def set_bonus(self, bonus):
        self.bonus = bonus

class Presensi:
    def __init__(self):
        self.data_presensi = {}

    def set_presensi(self, tanggal, status):
        self.data_presensi[tanggal] = status

    def get_presensi(self):
        return self.data_presensi.items()
