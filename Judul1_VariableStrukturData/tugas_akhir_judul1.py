#Membuat to do list untuk pr


todo_list = []


while True: 
   print("\n====to do list===")
   print("1. Tambahkan Tugas")
   print("2. Perlihatkan Tugas")
   print("3. Hapus Tugas")
   print("4. Keluar")

   pilihan = input("pilih menu:")

   if pilihan == "1":
    Tugas = input("Masukan Tugas Baru:")
    todo_list.append(Tugas)
    print("Tugas berhasil ditambahkan")
    
   elif pilihan == "2":
        if len(todo_list) == 0:
            print("belum ada tugas:")
        else: 
            print("\n daftar tugas:")
            for i in range(len(todo_list)):
                print(i + 1, ".", (todo_list[i]))
                
   elif pilihan == "3":
        if len(todo_list) == 0:
            print("tidak ada tugas untuk dihapus:")
        else:
            print("\n daftar tugas:" )
            for i in range(len(todo_list)):
                print(i+1, ".", (todo_list[i]))
                
        hapus = int(input("masukan nomor yang ingin dihapus:"))
        todo_list.pop(hapus-1)
        print("tugas berhasil dihapus")
        
   elif pilihan == "4":
        print("program selesai")
        break
   else:
        print("pilihan tidak valid")

