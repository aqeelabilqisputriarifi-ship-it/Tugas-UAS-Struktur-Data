# Sistem Antrian Rumah Sakit

## Deskripsi
Program ini merupakan aplikasi sederhana berbasis Python untuk mengelola sistem antrian pasien di rumah sakit. Data pasien disimpan dalam file CSV sehingga tetap tersimpan meskipun program ditutup.

## Fitur
- Menambah data pasien
- Menampilkan daftar antrian pasien
- Mencari pasien berdasarkan ID (Hash Map)
- Mengubah data pasien
- Menghapus data pasien
- Memanggil pasien sesuai urutan antrian (Queue)
- Menyimpan data secara otomatis ke file CSV

## Struktur Data yang Digunakan
- Queue (List)
  - Digunakan untuk menyimpan urutan antrian pasien.
  - Pasien dipanggil menggunakan metode FIFO (First In First Out).

- Hash Map (Dictionary)
  - Digunakan untuk mempercepat proses pencarian pasien berdasarkan ID.

## File Program

```
project/
│
├── main.py
├── data_pasien.csv
└── README.md
```

## Cara Menjalankan Program

1. Pastikan Python sudah terinstall.
2. Simpan semua file dalam satu folder.
3. Jalankan program dengan perintah:

```bash
python main.py
```

atau

```bash
python3 main.py
```

## Menu Program

1. Tambah Pasien
2. Lihat Antrian
3. Cari Pasien
4. Update Pasien
5. Hapus Pasien
6. Panggil Pasien
7. Keluar

## Penyimpanan Data

Semua data pasien akan disimpan pada file:

```
data_pasien.csv
```

Program akan membuat file tersebut secara otomatis apabila belum tersedia.

## Bahasa Pemrograman

- Python 3

## Library yang Digunakan

- csv
- os
- datetime

Seluruh library di atas merupakan library bawaan Python sehingga tidak perlu melakukan instalasi tambahan.

## Penulis

Nama : Aqeela Bilqis

Mata Kuliah : Struktur Data

Proyek : Sistem Antrian Rumah Sakit Menggunakan Queue dan Hash Map