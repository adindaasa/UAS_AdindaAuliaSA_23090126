class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' telah ditambahkan ke antrian.")

    def dequeue(self):
        if len(self.antrian) > 0:
            pesanan = self.antrian.pop(0)
            print(f"Pesanan '{pesanan}' telah dihapus dari antrian.")
            return pesanan
        else:
            print("Antrian kosong. Tidak ada pesanan yang dapat dihapus.")
            return None

    def tampilkan_antrian(self):
        if len(self.antrian) > 0:
            print("Pesanan saat ini dalam antrian:")
            for idx, pesanan in enumerate(self.antrian, start=1):
                print(f"{idx}. {pesanan}")
        else:
            print("Antrian kosong.")

if __name__ == "__main__":
    # Contoh penggunaan
    antrian_restoran = AntrianRestoran()

    # Menambahkan pesanan ke antrian
    antrian_restoran.enqueue("Burger")
    antrian_restoran.enqueue("Pizza")
    antrian_restoran.enqueue("Pasta")

    # Menampilkan antrian saat ini
    antrian_restoran.tampilkan_antrian()

    # Menghapus pesanan dari antrian
    antrian_restoran.dequeue()

    # Menampilkan antrian saat ini lagi
    antrian_restoran.tampilkan_antrian()
