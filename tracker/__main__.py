# tracker/__main__.py (FILE BARU UNTUK BONUS 3)

import csv
import os
import sys

# Menggunakan 'rich' untuk tampilan yang lebih baik (Bonus)
try:
    from rich.console import Console
    from rich.table import Table
    from rich import print
    from rich.panel import Panel
    HAVE_RICH = True
except ImportError:
    HAVE_RICH = False
    print("Warning: 'rich' tidak terinstall. Tampilan akan standar.")
    print("Install 'rich' untuk tampilan lebih baik: pip install rich")
    class Console:
        def print(self, *args, **kwargs):
            __builtins__.print(*args)
    console = Console()
    Panel = lambda text, **kwargs: print(f"--- {kwargs.get('title', '')} ---\n{text}\n---------")

# --- PERBEDAAN UTAMA ADA DI BLOK IMPORT INI ---
try:
    # Gunakan relative import (titik) karena kita ada di dalam paket 'tracker'
    from . import RekapKelas, build_markdown_report, save_text, build_html_report
except ImportError as e:
    print(f"Error: Gagal melakukan relative import. {e}")
    sys.exit(1)
# --- AKHIR PERBEDAAN ---


# --- Definisi Global ---
rekap = RekapKelas()
console = Console() if HAVE_RICH else Console()
REPORT_PATH = "out/report.md"
DATA_PATH_GRADES = "data/grades.csv"
DATA_PATH_ATTENDANCE = "data/attendance.csv"


# --- Fungsi-Fungsi Helper CSV ---

def append_to_grades_csv(nim, nama):
    """Menambahkan data mahasiswa baru ke grades.csv dengan nilai default 0."""
    new_data = [nim, nama, 0, 0, 0, 0]
    try:
        with open(DATA_PATH_GRADES, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(new_data)
        print(f"[green]-> Data {nama} berhasil disimpan ke {DATA_PATH_GRADES}[/green]")
    except IOError as e:
        print(f"[red]Error: Gagal menyimpan ke {DATA_PATH_GRADES}. {e}[/red]")
    except Exception as e:
        print(f"[red]Error tidak terduga saat menyimpan ke grades: {e}[/red]")

def append_to_attendance_csv(nim, hadir_persen=0.0):
    """Menambahkan data mahasiswa baru ke attendance.csv dengan kehadiran default 0."""
    new_data = [nim, hadir_persen]
    try:
        with open(DATA_PATH_ATTENDANCE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(new_data)
        print(f"[green]-> Data kehadiran {nim} berhasil disimpan ke {DATA_PATH_ATTENDANCE}[/green]")
    except IOError as e:
        print(f"[red]Error: Gagal menyimpan ke {DATA_PATH_ATTENDANCE}. {e}[/red]")
    except Exception as e:
        print(f"[red]Error tidak terduga saat menyimpan ke attendance: {e}[/red]")

def save_grades_to_csv():
    """Menulis ulang (overwrite) file grades.csv dengan data terbaru."""
    header = ['nim', 'nama', 'quiz', 'tugas', 'uts', 'uas']
    try:
        with open(DATA_PATH_GRADES, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for data in rekap.data_mahasiswa.values():
                mhs = data['mhs']
                nilai = data['nilai']
                row = {
                    'nim': mhs.nim, 'nama': mhs.nama, 'quiz': nilai.quiz,
                    'tugas': nilai.tugas, 'uts': nilai.uts, 'uas': nilai.uas
                }
                writer.writerow(row)
        print(f"[green]-> Perubahan nilai berhasil disimpan ke {DATA_PATH_GRADES}[/green]")
    except IOError as e:
        print(f"[red]Error: Gagal menyimpan ke {DATA_PATH_GRADES}. {e}[/red]")

def save_attendance_to_csv():
    """Menulis ulang (overwrite) file attendance.csv dengan data terbaru."""
    header = ['nim', 'hadir_persen']
    try:
        with open(DATA_PATH_ATTENDANCE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for data in rekap.data_mahasiswa.values():
                mhs = data['mhs']
                row = {'nim': mhs.nim, 'hadir_persen': mhs.hadir_persen}
                writer.writerow(row)
        print(f"[green]-> Perubahan presensi berhasil disimpan ke {DATA_PATH_ATTENDANCE}[/green]")
    except IOError as e:
        print(f"[red]Error: Gagal menyimpan ke {DATA_PATH_ATTENDANCE}. {e}[/red]")


# --- Fungsi-Fungsi CLI ---

def tampilkan_menu():
    """Tampilkan menu utama CLI (VERSI LENGKAP DENGAN BONUS)."""
    menu_text = """
[bold]1)[/bold] Muat data dari CSV
[bold]2)[/bold] Tambah mahasiswa baru
[bold]3)[/bold] Ubah presensi mahasiswa
[bold]4)[/bold] Ubah nilai mahasiswa
[bold]5)[/bold] Lihat rekap di terminal
[bold]6)[/bold] Simpan laporan Markdown
[bold magenta]7)[/bold magenta] Lihat rekap (Nilai < 70) [bold yellow](Bonus)[/bold yellow]
[bold magenta]8)[/bold magenta] Simpan laporan HTML [bold yellow](Bonus)[/bold yellow]
[bold]9)[/bold] Keluar
"""
    print(Panel(
        menu_text, 
        title="[bold cyan]=== Student Performance Tracker ===[/bold cyan]", 
        padding=(1, 2), 
        expand=False
    ))
    print("[bold]Pilihan Anda (1-9): [/bold]", end="")

def muat_data_csv():
    """Menu 1: Muat data dari file CSV."""
    print(f"\n[cyan]Memuat data dari {DATA_PATH_GRADES} dan {DATA_PATH_ATTENDANCE}...[/cyan]")
    try:
        with open(DATA_PATH_GRADES, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rekap.tambah_mahasiswa(row['nim'], row['nama'])
                rekap.set_penilaian(row['nim'], row['quiz'], row['tugas'], row['uts'], row['uas'])
        print(f"[green]Data nilai dari {DATA_PATH_GRADES} berhasil dimuat.[/green]")
    except FileNotFoundError:
        print(f"[yellow]Warning: File {DATA_PATH_GRADES} tidak ditemukan.[/yellow]")
    except Exception as e:
        print(f"[red]Error saat memuat {DATA_PATH_GRADES}: {e}[/red]")
    try:
        with open(DATA_PATH_ATTENDANCE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rekap.set_hadir(row['nim'], row['hadir_persen'])
        print(f"[green]Data kehadiran dari {DATA_PATH_ATTENDANCE} berhasil dimuat.[/green]")
    except FileNotFoundError:
        print(f"[yellow]Warning: File {DATA_PATH_ATTENDANCE} tidak ditemukan.[/yellow]")
    except Exception as e:
        print(f"[red]Error saat memuat {DATA_PATH_ATTENDANCE}: {e}[/red]")

def tambah_mahasiswa_cli():
    """Menu 2: Handler CLI untuk menambah mahasiswa baru (DIMODIFIKASI)."""
    print("\n[cyan]-- Tambah Mahasiswa Baru --[/cyan]")
    nim = input("Masukkan NIM: ").strip()
    nama = input("Masukkan Nama: ").strip()
    if not nim or not nama:
        print("[red]Error: NIM dan Nama tidak boleh kosong.[/red]")
        return
    if nim in rekap.data_mahasiswa:
        print(f"[yellow]Info: NIM {nim} ({rekap.data_mahasiswa[nim]['mhs'].nama}) sudah terdaftar.[/yellow]")
        return
    rekap.tambah_mahasiswa(nim, nama) 
    hadir_default = rekap.data_mahasiswa[nim]['mhs'].hadir_persen 
    print("[cyan]Menyimpan data baru ke file CSV...[/cyan]")
    append_to_grades_csv(nim, nama) 
    append_to_attendance_csv(nim, hadir_default)

def ubah_presensi_cli():
    """Menu 3: Handler CLI untuk mengubah presensi (DIMODIFIKASI)."""
    print("\n[cyan]-- Ubah Presensi Mahasiswa --[/cyan]")
    nim = input("Masukkan NIM mahasiswa: ").strip()
    if nim not in rekap.data_mahasiswa:
        print(f"[red]Error: NIM {nim} tidak ditemukan.[/red]")
        return
    try:
        persen_str = input(f"Masukkan persentase kehadiran baru (0-100) untuk {rekap.data_mahasiswa[nim]['mhs'].nama}: ").strip()
        rekap.set_hadir(nim, persen_str) 
        print("[cyan]Menyimpan perubahan presensi ke CSV...[/cyan]")
        save_attendance_to_csv()
    except Exception as e:
        print(f"[red]Error: {e}[/red]")

def ubah_nilai_cli():
    """Menu 4: Handler CLI untuk mengubah nilai (DIMODIFIKASI)."""
    print("\n[cyan]-- Ubah Nilai Mahasiswa --[/cyan]")
    nim = input("Masukkan NIM mahasiswa: ").strip()
    if nim not in rekap.data_mahasiswa:
        print(f"[red]Error: NIM {nim} tidak ditemukan.[/red]")
        return
    try:
        print(f"Masukkan nilai baru untuk [bold]{rekap.data_mahasiswa[nim]['mhs'].nama}[/bold]:")
        quiz = input("Nilai Quiz (0-100): ").strip()
        tugas = input("Nilai Tugas (0-100): ").strip()
        uts = input("Nilai UTS (0-100): ").strip()
        uas = input("Nilai UAS (0-100): ").strip()
        rekap.set_penilaian(nim, quiz, tugas, uts, uas) 
        print("[cyan]Menyimpan perubahan nilai ke CSV...[/cyan]")
        save_grades_to_csv()
    except Exception as e:
        print(f"[red]Error tidak terduga saat input nilai: {e}[/red]")

def _tampilkan_tabel_rekap(records, title="Rekap Kinerja Mahasiswa"):
    """Fungsi helper internal untuk menampilkan tabel rekap (kaya atau standar)."""
    if not records:
        print(f"[yellow]Tidak ada data mahasiswa untuk ditampilkan ({title}).[/yellow]")
        return
    records.sort(key=lambda x: x['nim'])
    if HAVE_RICH:
        table = Table(title=f"[bold cyan]{title}[/bold cyan]")
        table.add_column("NIM", style="magenta")
        table.add_column("Nama", style="green")
        table.add_column("Hadir (%)", justify="right", style="cyan")
        table.add_column("Nilai Akhir", justify="right", style="yellow")
        table.add_column("Predikat", justify="center", style="bold")
        for rec in records:
            table.add_row(
                rec['nim'], rec['nama'],
                f"{rec['hadir']:.1f}", f"{rec['nilai_akhir']:.2f}", rec['predikat']
            )
        console.print(table)
    else:
        print(f"{'NIM':<12} | {'Nama':<15} | {'Hadir (%)':>10} | {'Nilai Akhir':>12} | {'Predikat':^10}")
        print("-" * 65)
        for rec in records:
            print(f"{rec['nim']:<12} | {rec['nama']:<15} | {rec['hadir']:>10.1f} | {rec['nilai_akhir']:>12.2f} | {rec['predikat']:^10}")
            
def lihat_rekap_cli():
    """Menu 5: Tampilkan rekap di terminal (tampilan terminal)."""
    print("\n[cyan]-- Rekap Nilai Mahasiswa (Terminal) --[/cyan]")
    records = rekap.rekap()
    _tampilkan_tabel_rekap(records, "Rekap Kinerja Mahasiswa")

def simpan_laporan_md():
    """Menu 6: Hasilkan dan simpan laporan Markdown."""
    print(f"\n[cyan]-- Simpan Laporan Markdown --[/cyan]")
    records = rekap.rekap()
    if not records:
        print("[yellow]Tidak ada data untuk dibuat laporan.[/yellow]")
        return
    content = build_markdown_report(records)
    save_text(REPORT_PATH, content)

def lihat_rekap_filter_cli():
    """Menu 7 (Bonus): Tampilkan rekap mahasiswa dengan nilai < 70."""
    print("\n[cyan]-- Rekap Mahasiswa (Nilai < 70) --[/cyan]")
    all_records = rekap.rekap()
    filtered_records = [rec for rec in all_records if rec['nilai_akhir'] < 70]
    _tampilkan_tabel_rekap(filtered_records, "Mahasiswa dengan Nilai < 70")

def simpan_laporan_html():
    """Menu 8 (Bonus): Hasilkan dan simpan laporan HTML."""
    print(f"\n[cyan]-- Simpan Laporan HTML --[/cyan]")
    records = rekap.rekap()
    if not records:
        print("[yellow]Tidak ada data untuk dibuat laporan.[/yellow]")
        return
    content = build_html_report(records)
    save_text("out/report.html", content)

def main():
    """Fungsi utama untuk menjalankan loop aplikasi (VERSI LENGKAP DENGAN BONUS)."""
    os.makedirs("data", exist_ok=True)
    os.makedirs("out", exist_ok=True)
    while True:
        tampilkan_menu()
        try:
            pilihan = input().strip()
            if pilihan == '1':
                muat_data_csv()
            elif pilihan == '2':
                tambah_mahasiswa_cli()
            elif pilihan == '3':
                ubah_presensi_cli()
            elif pilihan == '4':
                ubah_nilai_cli()
            elif pilihan == '5':
                lihat_rekap_cli()
            elif pilihan == '6':
                simpan_laporan_md()
            elif pilihan == '7':
                lihat_rekap_filter_cli()
            elif pilihan == '8':
                simpan_laporan_html()
            elif pilihan == '9':
                print("[bold cyan]Terima kasih telah menggunakan Student Performance Tracker![/bold cyan]")
                break
            else:
                print("[red]Pilihan tidak valid. Harap masukkan angka 1-9.[/red]")
        except (EOFError, KeyboardInterrupt):
            print("\n[bold red]Aplikasi dihentikan. Keluar...[/bold red]")
            break
        except Exception as e:
            print(f"\n[bold red]Terjadi error: {e}[/bold red]")
        if pilihan != '9':
            try:
                input("\nTekan Enter untuk kembali ke menu...")
            except (EOFError, KeyboardInterrupt):
                 print("\n[bold red]Aplikasi dihentikan. Keluar...[/bold red]")
                 break

# --- Entry Point ---
if __name__ == "__main__":
    main()