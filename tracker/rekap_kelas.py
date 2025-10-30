# tracker/rekap_kelas.py

from .mahasiswa import Mahasiswa
from .penilaian import Penilaian

class RekapKelas:
    """
    Manajer untuk mengelola banyak objek Mahasiswa dan Penilaian. [cite: 38]
    """

    def __init__(self):
        """
        Inisialisasi rekap, menggunakan dictionary sesuai format:
        {nim: {'mhs': obj, 'nilai': obj}} [cite: 41]
        """
        self.data_mahasiswa = {}

    def tambah_mahasiswa(self, nim, nama):
        """
        Tambah mahasiswa baru ke rekap. [cite: 43]
        Secara otomatis membuat data penilaian default.
        """
        if nim not in self.data_mahasiswa:
            self.data_mahasiswa[nim] = {
                'mhs': Mahasiswa(nim, nama),
                'nilai': Penilaian()  # Nilai default (semua 0)
            }
            print(f"-> Mahasiswa {nama} (NIM: {nim}) berhasil ditambahkan.")
        else:
            print(f"-> Info: NIM {nim} ({nama}) sudah terdaftar.")

    def set_hadir(self, nim, persen):
        """
        Atur persentase kehadiran untuk seorang mahasiswa. [cite: 44]
        """
        if nim in self.data_mahasiswa:
            self.data_mahasiswa[nim]['mhs'].hadir_persen = persen
            # Pesan error/sukses akan dicetak oleh setter Mahasiswa
        else:
            print(f"Error: NIM {nim} tidak ditemukan.")

    def set_penilaian(self, nim, quiz, tugas, uts, uas):
        """
        Atur nilai lengkap (quiz, tugas, uts, uas) untuk mahasiswa. [cite: 45]
        """
        if nim in self.data_mahasiswa:
            self.data_mahasiswa[nim]['nilai'] = Penilaian(quiz, tugas, uts, uas)
            print(f"-> Nilai untuk {self.data_mahasiswa[nim]['mhs'].nama} berhasil diatur.")
        else:
            print(f"Error: NIM {nim} tidak ditemukan.")

    def _predikat(self, nilai_akhir):
        """
        Tentukan predikat huruf (A-E) berdasarkan nilai akhir. [cite: 47]
        (Metode internal/helper)
        """
        if nilai_akhir >= 85:
            return 'A'
        elif nilai_akhir >= 75:
            return 'B'
        elif nilai_akhir >= 65:
            return 'C'
        elif nilai_akhir >= 55:
            return 'D'
        else:
            return 'E'

    def rekap(self):
        """
        Menghasilkan list of dictionaries dari data rekap. [cite: 46]
        Ini digunakan sebagai sumber data untuk laporan.
        """
        records = []
        for nim, data in self.data_mahasiswa.items():
            mhs = data['mhs']
            nilai_obj = data['nilai']
            
            nilai_akhir = nilai_obj.nilai_akhir()
            predikat = self._predikat(nilai_akhir)
            
            records.append({
                "nim": mhs.nim,
                "nama": mhs.nama,
                "hadir": mhs.hadir_persen,
                "nilai_akhir": nilai_akhir,
                "predikat": predikat
            })
        return records