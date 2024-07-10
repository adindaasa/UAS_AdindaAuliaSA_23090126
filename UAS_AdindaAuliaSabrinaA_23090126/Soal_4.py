class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        return f"{super().information()}, Vitamin: {self.vitamin}"
    
mangga_gedong = Mangga("Mangga Gedong", "Kuning", "Manis", "Vitamin C")

print(f"Nama: {mangga_gedong.nama}")
print(f"Warna: {mangga_gedong.warna}")
print(f"Rasa: {mangga_gedong.rasa}")
print(f"Vitamin: {mangga_gedong.vitamin}")

print(mangga_gedong.information())

mangga_gedong.setNama("Mangga Harum Manis")
mangga_gedong.setWarna("Hijau")
mangga_gedong.setRasa("Manis Asam")
mangga_gedong.setVitamin("Vitamin A")
print(mangga_gedong.information())
