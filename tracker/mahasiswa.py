# tracker/mahasiswa.py

class Mahasiswa:
    """
    Mewakili data seorang mahasiswa. [cite: 25]
    Menggunakan enkapsulasi untuk atribut _hadir_persen. [cite: 19]
    """

    def __init__(self, nim, nama):
        """
        Inisialisasi objek Mahasiswa.
        
        Args:
            nim (str): Nomor Induk Mahasiswa.
            nama (str): Nama lengkap mahasiswa.
        """
        self.nim = nim
        self.nama = nama
        self._hadir_persen = 0.0  # Atribut privat [cite: 26]

    @property
    def hadir_persen(self):
        """
        Property untuk mengambil nilai _hadir_persen. [cite: 27]
        """
        return self._hadir_persen

    @hadir_persen.setter
    def hadir_persen(self, nilai):
        """
        Setter untuk validasi nilai hadir_persen (0-100). [cite: 27]
        """
        try:
            nilai = float(nilai)
            if 0 <= nilai <= 100:
                self._hadir_persen = nilai
            else:
                print(f"Error (NIM: {self.nim}): Persentase kehadiran ({nilai}) harus antara 0 dan 100.")
        except ValueError:
             print(f"Error (NIM: {self.nim}): Masukan kehadiran '{nilai}' tidak valid.")

    def info(self):
        """
        Menampilkan profil singkat mahasiswa. [cite: 28]
        """
        return f"NIM: {self.nim}, Nama: {self.nama}, Kehadiran: {self.hadir_persen}%"