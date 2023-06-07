from transaction import Transaction

if __name__ == "__main__":
    user_id = input("Masukkan User ID Anda: ")
    transaksi = Transaction(user_id)

    while True:
        print("=== Super Cashier ===")
        print("1. Tambah Item")
        print("2. Update Item")
        print("3. Hapus Item")
        print("4. Cek Pesanan")
        print("5. Total Harga")
        print("6. Batalkan/Reset Transaksi")
        print("0. Keluar")

        opsi = input("Pilih menu (0-6): ")

        if opsi == "1":
            item_name = input("Masukkan nama item: ")
            item_qty = int(input("Masukkan jumlah item: "))
            item_price = int(input("Masukkan harga per item: "))
            transaksi.add_item([item_name, item_qty, item_price])
            print("Item berhasil ditambahkan ke transaksi.")
        elif opsi == "2":
            item_name = input("Masukkan nama item yang ingin diupdate: ")
            transaksi.update_item(item_name)
            print("Item berhasil diupdate.")
        elif opsi == "3":
            item_name = input("Masukkan nama item yang ingin dihapus: ")
            transaksi.delete_item(item_name)
            print("Item berhasil dihapus dari transaksi.")
        elif opsi == "4":
            transaksi.check_order()
        elif opsi == "5":
            total_belanja = transaksi.total_price()
            print(f"Total Harga: Rp. {total_belanja}")
        elif opsi == "6":
            transaksi.reset_transaction()
            print("Transaksi telah direset.")
        elif opsi == "0":
            transaksi.save_final_transaction_to_db()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        transaksi.save_transaction()

    transaksi.close_connection()
