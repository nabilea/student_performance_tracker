# tracker/penilaian.py

class Penilaian:
    """
    Mewakili data penilaian seorang mahasiswa (quiz, tugas, uts, uas). [cite: 33]
    """

    def __init__(self, quiz=0, tugas=0, uts=0, uas=0):
        """
        Inisialisasi objek Penilaian dengan validasi nilai 0-100. [cite: 36]
        
        Args:
            quiz (float): Nilai quiz (0-100)
            tugas (float): Nilai tugas (0-100)
            uts (float): Nilai UTS (0-100)
            uas (float): Nilai UAS (0-100)
        """
        self.quiz = self._validasi_nilai(quiz, "Quiz")
        self.tugas = self._validasi_nilai(tugas, "Tugas")
        self.uts = self._validasi_nilai(uts, "UTS")
        self.uas = self._validasi_nilai(uas, "UAS") # [cite: 34]

    def _validasi_nilai(self, nilai, nama_nilai):
        """Helper internal untuk validasi semua nilai agar 0-100."""
        try:
            nilai = float(nilai)
            if 0 <= nilai <= 100:
                return nilai
            else:
                print(f"Error: Nilai {nama_nilai} ({nilai}) harus 0-100. Diatur ke 0.")
                return 0.0
        except ValueError:
            print(f"Error: Nilai {nama_nilai} ('{nilai}') tidak valid. Diatur ke 0.")
            return 0.0

    def nilai_akhir(self):
        """
        Hitung nilai akhir berdasarkan bobot:
        15% Quiz, 25% Tugas, 25% UTS, 35% UAS. [cite: 35]
        """
        return (self.quiz * 0.15) + \
               (self.tugas * 0.25) + \
               (self.uts * 0.25) + \
               (self.uas * 0.35)