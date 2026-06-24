import csv
import os
from datetime import datetime

FILE = "data_pasien.csv"


# ==============================
# QUEUE
# ==============================

antrian = []


# ==============================
# HASH MAP
# ==============================

data_pasien = {}



# ==============================

def buat_file():

    if not os.path.exists(FILE):

        with open(FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "ID Pasien",
                    "Nama",
                    "Umur",
                    "Keluhan",
                    "Poli",
                    "Nomor Antrian",
                    "Tanggal"
                ]
            )



# ==============================
# LOAD DATA CSV
# ==============================

def load_data():

    data_pasien.clear()
    antrian.clear()


    with open(FILE, "r") as file:

        reader = csv.DictReader(file)


        for row in reader:

            data_pasien[row["ID Pasien"]] = row

            antrian.append(row)



# ==============================
# SIMPAN DATA CSV
# ==============================

def simpan_data():


    with open(FILE,"w",newline="") as file:


        writer = csv.DictWriter(
            file,
            fieldnames=[
                "ID Pasien",
                "Nama",
                "Umur",
                "Keluhan",
                "Poli",
                "Nomor Antrian",
                "Tanggal"
            ]
        )


        writer.writeheader()


        for pasien in antrian:

            writer.writerow(pasien)



# ==============================
# CREATE
# ==============================

def tambah_pasien():


    print("\n=== Tambah Pasien ===")


    id_pasien = input("ID Pasien : ")


    if id_pasien in data_pasien:

        print("ID sudah digunakan!")

        return



    nama = input("Nama Pasien : ")

    umur = input("Umur : ")

    keluhan = input("Keluhan : ")

    poli = input("Poli Tujuan : ")



    nomor = len(antrian)+1



    pasien = {

        "ID Pasien":id_pasien,

        "Nama":nama,

        "Umur":umur,

        "Keluhan":keluhan,

        "Poli":poli,

        "Nomor Antrian":nomor,

        "Tanggal":datetime.now().strftime("%d-%m-%Y")

    }



    antrian.append(pasien)


    data_pasien[id_pasien]=pasien


    simpan_data()



    print("Pasien berhasil ditambahkan!")



# ==============================
# READ
# ==============================

def tampilkan_data():


    print("\n=== DATA ANTRIAN PASIEN ===")


    if len(antrian)==0:

        print("Belum ada pasien")

        return



    # Sorting nomor antrian

    urut = sorted(
        antrian,
        key=lambda x:int(x["Nomor Antrian"])
    )



    for p in urut:


        print("---------------------")

        print("Nomor Antrian :",p["Nomor Antrian"])

        print("ID Pasien :",p["ID Pasien"])

        print("Nama :",p["Nama"])

        print("Umur :",p["Umur"])

        print("Keluhan :",p["Keluhan"])

        print("Poli :",p["Poli"])

        print("Tanggal :",p["Tanggal"])





# ==============================
# SEARCHING HASH MAP
# ==============================

def cari_pasien():


    print("\n=== Cari Pasien ===")


    id_cari=input("Masukkan ID Pasien : ")



    if id_cari in data_pasien:


        p=data_pasien[id_cari]


        print("\nData ditemukan")

        print("Nama :",p["Nama"])

        print("Keluhan :",p["Keluhan"])

        print("Poli :",p["Poli"])

        print("Nomor Antrian :",p["Nomor Antrian"])



    else:

        print("Data tidak ditemukan")





# ==============================
# UPDATE
# ==============================

def update_pasien():


    print("\n=== Update Data Pasien ===")


    id_update=input("ID Pasien : ")



    if id_update not in data_pasien:


        print("Data tidak ditemukan")

        return



    nama=input("Nama baru : ")

    keluhan=input("Keluhan baru : ")

    poli=input("Poli baru : ")



    pasien=data_pasien[id_update]


    pasien["Nama"]=nama

    pasien["Keluhan"]=keluhan

    pasien["Poli"]=poli



    simpan_data()



    print("Data berhasil diperbarui")





# ==============================
# DELETE
# ==============================

def hapus_pasien():


    print("\n=== Hapus Pasien ===")


    id_hapus=input("ID Pasien : ")



    if id_hapus not in data_pasien:


        print("Data tidak ditemukan")

        return



    pasien=data_pasien[id_hapus]



    antrian.remove(pasien)


    del data_pasien[id_hapus]


    simpan_data()



    print("Pasien berhasil dihapus")





# ==============================
# PANGGIL PASIEN (QUEUE)
# ==============================

def panggil_pasien():


    print("\n=== Pemanggilan Pasien ===")



    if len(antrian)==0:


        print("Tidak ada pasien")

        return



    pasien=antrian.pop(0)



    del data_pasien[pasien["ID Pasien"]]


    simpan_data()



    print(
        "Pasien dipanggil:",
        pasien["Nama"],
        "Nomor",
        pasien["Nomor Antrian"]
    )





# ==============================
# MENU UTAMA
# ==============================


def menu():


    buat_file()

    load_data()



    while True:


        print("\n==============================")

        print(" SISTEM ANTRIAN RUMAH SAKIT ")

        print("==============================")


        print("1. Tambah Pasien")

        print("2. Lihat Antrian")

        print("3. Cari Pasien")

        print("4. Update Pasien")

        print("5. Hapus Pasien")

        print("6. Panggil Pasien")

        print("7. Keluar")



        pilih=input("Pilih menu : ")



        if pilih=="1":

            tambah_pasien()


        elif pilih=="2":

            tampilkan_data()


        elif pilih=="3":

            cari_pasien()


        elif pilih=="4":

            update_pasien()


        elif pilih=="5":

            hapus_pasien()


        elif pilih=="6":

            panggil_pasien()


        elif pilih=="7":

            print("Program selesai")

            break


        else:

            print("Pilihan tidak tersedia")





menu()

