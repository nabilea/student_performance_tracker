# Proyek 2: Student Performance Tracker

Proyek ini merupakan implementasi Tugas Proyek 2 untuk Mata Kuliah Pemrograman Python (MK44). Aplikasi ini dirancang untuk mengelola data kinerja mahasiswa, mengintegrasikan konsep Object-Oriented Programming (OOP) dan Modularisasi Paket.

Aplikasi ini berfungsi sebagai alat untuk mengelola data mahasiswa, kehadiran, penilaian, dan menghasilkan laporan kinerja.

## 🎯 Fitur Utama

* **Manajemen Data Mahasiswa**: Mengelola `nim`, `nama`, dan `_hadir_persen` melalui kelas `Mahasiswa`. Menerapkan enkapsulasi dan validasi `@property` untuk kehadiran (0-100).
* **Manajemen Penilaian**: Mengelola nilai `quiz`, `tugas`, `uts`, `uas` melalui kelas `Penilaian`. Menerapkan validasi nilai (0-100).
* **Kalkulasi Nilai Akhir**: Menyediakan method `nilai_akhir()` dengan bobot (Quiz 15%, Tugas 25%, UTS 25%, UAS 35%).
* **Manajer Rekap**: Menggunakan kelas `RekapKelas` untuk mengelola kumpulan objek mahasiswa dan penilaian dalam struktur data dictionary.
* **Interaksi CLI**: Menyediakan antarmuka baris perintah (CLI) interaktif untuk:
    * Memuat data dari file `.csv`.
    * Menambah mahasiswa baru.
    * Mengubah data presensi.
    * Mengubah data nilai.
* **Penyimpanan Data**: Perubahan yang dilakukan (tambah mahasiswa, ubah nilai, ubah presensi) akan disimpan kembali secara permanen ke file `.csv` yang sesuai.
* **Ekspor Laporan**:
    * Menghasilkan laporan rekap dalam format **Markdown** (`out/report.md`).
    * (Bonus) Menghasilkan laporan rekap dalam format **HTML** (`out/report.html`) dengan pewarnaan baris berdasarkan predikat.
* **Fitur Filter**:
    * (Bonus) Menyediakan menu untuk menampilkan rekap mahasiswa di terminal yang memiliki nilai akhir di bawah 70.

## 📁 Struktur Proyek

Struktur folder proyek ini dirancang sesuai dengan panduan modularisasi Minggu 10.

student_performance_tracker/ ├── app.py # Titik masuk aplikasi utama (CLI) ├── README.md # Dokumentasi ini ├── requirements.txt # Daftar dependensi (misal: rich) ├── .venv/ # Direktori virtual environment ├── data/ # Berisi data input CSV │ ├── attendance.csv │ └── grades.csv ├── out/ # Berisi laporan yang dihasilkan │ ├── report.md │ └── report.html └── tracker/ # Paket (package) Python ├── init.py # Penanda paket, mengekspor simbol ├── main.py # (Bonus) Entry point untuk python -m tracker ├── mahasiswa.py # Modul Class Mahasiswa ├── penilaian.py # Modul Class Penilaian ├── rekap_kelas.py # Modul Class RekapKelas (Manajer) └── report.py # Modul fungsi laporan


## 🚀 Cara Menjalankan

1.  **Buka Terminal**
    Pastikan Anda berada di direktori utama proyek ini (`student_performance_tracker/`).

2.  **Buat Virtual Environment** (Hanya perlu dilakukan satu kali)
    ```bash
    python -m venv .venv
    ```

3.  **Aktifkan Virtual Environment**
    * Di Windows (PowerShell):
        ```powershell
        .\.venv\Scripts\Activate.ps1
        ```
        *(Jika terjadi error, jalankan `Set-ExecutionPolicy RemoteSigned -Scope Process` terlebih dahulu, lalu ulangi perintah aktivasi)*

4.  **Install Dependensi**
    Pastikan virtual environment (`.venv`) telah aktif, lalu jalankan:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Jalankan Aplikasi**
    Aplikasi dapat dijalankan melalui dua cara:

    * **Cara Standar:**
        ```bash
        python app.py
        ```
    * **Cara Modul (Bonus):**
        ```bash
        python -m tracker
        ```

6.  **Gunakan Aplikasi**
    Aplikasi akan menampilkan menu interaktif. Coba Opsi 1 untuk memuat data dari CSV, lalu Opsi 5 untuk melihat rekap, dan Opsi 6 atau 8 untuk menghasilkan file laporan di direktori `out/`.