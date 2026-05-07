def sequential_search(produk, cari):
    for i in range(len(produk)):
        if produk[i].lower() == cari.lower():
            return i + 1   # agar indeks dimulai dari 1
    return -1


def main():
    produk = ["Buku", "Pulpen", "Penghapus", "Penggaris", "Spidol"]

    print("Daftar Produk Toko:")
    for i in range(len(produk)):
        print(i+1, ".", produk[i])

    cari = input("\nMasukkan nama produk yang ingin dicari: ")

    hasil = sequential_search(produk, cari)

    if hasil != -1:
        print("Produk ditemukan pada Rak ke-", hasil)
    else:
        print("Produk tidak tersedia di toko")


main()