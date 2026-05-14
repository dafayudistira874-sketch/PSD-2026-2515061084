aktivitas = []

def tambah_aktivitas():
    data = input("Masukkan aktivitas: ")
    aktivitas.append(data)
    print("Aktivitas berhasil ditambahkan")

def hapus_aktivitas():
    if len(aktivitas) == 0:
        print("Tidak ada aktivitas yang bisa dihapus")
    else:
        data = aktivitas.pop()
        print("Aktivitas terakhir dihapus:", data)

def tampilkan():
    if len(aktivitas) == 0:
        print("Belum ada aktivitas")
    else:
        print("Riwayat aktivitas:")
        for i in range(len(aktivitas)-1, -1, -1):
            print(aktivitas[i])

def main():
    while True:
        print("\n=== MENU RIWAYAT AKTIVITAS ===")
        print("1. Tambah Aktivitas")
        print("2. Hapus Aktivitas Terakhir")
        print("3. Tampilkan Riwayat Aktivitas")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_aktivitas()
        elif pilih == "2":
            hapus_aktivitas()
        elif pilih == "3":
            tampilkan()
        elif pilih == "4":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid")

main()
