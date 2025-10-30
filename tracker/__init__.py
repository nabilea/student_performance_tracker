# tracker/__init__.py (VERSI LENGKAP DENGAN BONUS)

"""
Paket student_performance_tracker.

Mengekspor kelas dan fungsi utama untuk digunakan oleh app.py
sesuai konsep modularisasi Minggu 10.
"""

from .mahasiswa import Mahasiswa
from .penilaian import Penilaian
from .rekap_kelas import RekapKelas
# 1. TAMBAHKAN build_html_report DI SINI
from .report import build_markdown_report, save_text, build_html_report

# Mendefinisikan apa yang diekspor saat 'from tracker import *'
__all__ = [
    'Mahasiswa', 
    'Penilaian', 
    'RekapKelas', 
    'build_markdown_report', 
    'save_text',
    'build_html_report' # 2. TAMBAHKAN JUGA DI SINI
]