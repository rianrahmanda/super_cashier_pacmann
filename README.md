# super_cashier_pacmann

**Latar Belakang Masalah**\
Aplikasi ini dibuat untuk melakukan pembelian secara mandiri dengan memasukkan item yang dibeli, jumlah item yang dibeli dan harga item yang dibeli oleh pelanggan. Selain itu aplikasi ini memiliki fitur penyimpanan transaksi pelanggan agar pemilik usaha dapat memiliki  data pelanggan yang nantinya dapat digunakan sebagai data untuk menganalisa prilaku pelanggan dengan menggunakan teknik - teknik machine learning. Program ini terdiri dari 3 file yaitu :
1. "transaction.py" yang menyimpan fungsi utama dari program super_Cashier
2. "main_cashier.py" untuk menjalankan aplikasi main cashier
3. "view_database.py" untuk melihat isi database yang berisi histori transaksi pelanggan. fitur ini dijalankan oleh pemilik usaha

**Requirements/Objectives**\
Objective program **transaction.py**:
- Membuat objek transaksi dengan inisialisasi ID pengguna.
- Menambahkan, memperbarui, menghapus, dan menampilkan item dalam transaksi.
- Menghitung total harga transaksi dengan menerapkan potongan harga sesuai dengan ketentuan.
- Menyimpan transaksi saat ini dan transaksi akhir ke database.
- Menampilkan riwayat transaksi dari database.
- Menutup koneksi ke database.

**Requirements** program **transaction.py**:
- Koneksi ke database SQLite.
- Tabel "transactions" dalam database untuk menyimpan data transaksi.
- Kelas **Transaction** yang mewakili transaksi.
- Metode **__init__** untuk inisialisasi objek transaksi.
- Metode **create_table** untuk membuat tabel 'transactions' jika belum ada di database.
- Metode **add_item** untuk menambahkan item ke transaksi.
- Metode **update_item** untuk memperbarui item dalam transaksi.
- Metode **delete_item** untuk menghapus item dari transaksi.
- Metode **reset_transaction** untuk menghapus seluruh item dalam transaksi.
- Metode **check_order** untuk menampilkan item dalam transaksi.
- Metode **save_transaction_to_db** untuk menyimpan transaksi saat ini ke database.
- Metode **save_final_transaction_to_db** untuk menyimpan transaksi akhir ke database.
- Metode **total_price** untuk menghitung total harga transaksi.
- Metode **view_transaction_history** untuk menampilkan riwayat transaksi dari database.
- Metode **save_transaction** untuk menyimpan transaksi ke database.
- Metode **close_connection** untuk menutup koneksi ke database.
