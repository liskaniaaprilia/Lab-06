# Lab 6

print("=======================================")
print("Nama : Liskania Aprilia")
print("NIM  : 312210383")
print("=======================================")

data = {}
# Untuk Menambahkan Data
def tambah():
    print()
    print("Tambah Data")
    nama  = input    ("Nama        : ")
    nim   = input    ("NIM         : ")
    tugas = int(input("Nilai Tugas : "))
    uts   = int(input("Nilai UTS   : "))
    uas   = int(input("Nilai UAS   : "))
    nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
    data[nama] = [nim, tugas, uts, uas, nilaiakhir]
    return

# Untuk Menampilkan Data
def tampilkan():
    if data.items():
        print()
        print("Daftar Nilai")
        print()
        print("=======================================================================================");
        print("|     NAMA    |      NIM      |    TUGAS    |     UTS     |     UAS     | Nilai Akhir |");
        print("=======================================================================================");
        i = 0
        for x in data.items():
            i+=i
            print("|  {0:9}  |   {1:9}   |  {2:9}  |  {3:9}  |  {4:9}  |  {5:9}  |"
                  .format(x[0][: 14], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("=======================================================================================");

    else :
        print()
        print("Daftar Nilai")
        print()
        print("======================================================================================");
        print("|    NAMA    |      NIM      |    TUGAS    |     UTS     |     UAS     | Nilai Akhir |");
        print("======================================================================================");
        print("|                                  TIDAK ADA DATA                                    |");
        print("======================================================================================");
    return

# Untuk Menghapus data  Berdasarkan Nama
def hapus():
    print()
    print("Hapus Data Mahasiswa")
    nama  = input    ("Nama       : ")
    if nama in data.keys():
        del data[nama]
    else:
        print("Data {0} tidak ada".format(nama))
    return

# Untuk Mengubah data Berdasarkan Nama
def ubah():
    print()
    print("Ubah Data Mahasiswa")
    nama = input("Nama        : ")
    if nama in data.keys():
        nim   = input    ("NIM         : ")
        tugas = int(input("Nilai Tugas : "))
        uts   = int(input("Nilai UTS   : "))
        uas   = int(input("Nilai UAS   : "))
        nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
        data[nama] = [nim, tugas, uts, uas, nilaiakhir]
    else:
        print("Data nilai{0} tidak ada".format(nama))

while True:
    print()
    print("|1| Lihat Data")
    print("|2| Tambah Data")
    print("|3| Ubah Data")
    print("|4| Hapus Data")
    print("|5| Keluar")

    x = input(">> PILIH MENU : ")

    if x == '1':
        tampilkan()
    elif x == '2':
        tambah()
    elif x == '3':
        ubah()
    elif x == '4':
        hapus()

    else:

        exit()








