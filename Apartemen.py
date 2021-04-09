from Hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, harga_hunian, fitur):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.harga_hunian = harga_hunian
        self.fitur = fitur

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_harga_hunian(self):
        return self.harga_hunian

    def get_fitur(self):
        return self.fitur