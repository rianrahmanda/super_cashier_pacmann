# super_cashier_pacmann

**Latar Belakang Masalah**\
Aplikasi ini dibuat untuk melakukan pembelian secara mandiri dengan memasukkan item yang dibeli, jumlah item yang dibeli dan harga item yang dibeli oleh pelanggan. Selain itu aplikasi ini memiliki fitur penyimpanan transaksi pelanggan agar pemilik usaha dapat memiliki  data pelanggan yang nantinya dapat digunakan sebagai data untuk menganalisa prilaku pelanggan dengan menggunakan teknik - teknik machine learning. Program ini terdiri dari 3 file yaitu :
1. "transaction.py" yang menyimpan fungsi utama dari program super_Cashier
2. "main_cashier.py" untuk menjalankan aplikasi main cashier
3. "view_database.py" untuk melihat isi database yang berisi histori transaksi pelanggan. fitur ini dijalankan oleh pemilik usaha

# Requirements/Objectives
**Objective** program **transaction.py**:
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

**Objective** program **main_cashier.py**:
- Membuat objek transaksi dengan menggunakan ID pengguna yang dimasukkan.
- Menampilkan menu pilihan kepada pengguna.
- Mengizinkan pengguna untuk menambahkan, memperbarui, menghapus, dan menampilkan item dalam transaksi.
- Menghitung total harga transaksi.
- Mereset transaksi jika pengguna memilih opsi tersebut.
- Menyimpan transaksi akhir ke database saat pengguna memilih keluar.
- Menutup koneksi ke database setelah selesai.
- Dengan memenuhi semua requirements dan mencapai tujuan yang dijelaskan di atas, kedua file ini bekerja bersama untuk memungkinkan pengguna melakukan transaksi, melacak riwayat transaksi, dan menyimpan data transaksi ke database.

**Requirements** program **main_cashier.py**:
- Import modul Transaction dari file "transaction.py".
- Meminta input User ID dari pengguna.
- Menampilkan menu pilihan untuk kasir.
- Menambahkan item ke transaksi.
- Memperbarui item dalam transaksi.
- Menghapus item dari transaksi.
- Menampilkan item dalam transaksi.
- Menghitung total harga transaksi.
- Mereset transaksi dengan menghapus seluruh item.
- Menyimpan transaksi akhir ke database.
- Mengulang menu pilihan hingga pengguna memilih keluar.

**Objective** program **view_database.py**:
- Membuka koneksi ke database SQLite dengan menggunakan modul sqlite3.
- Mengeksekusi kueri SELECT untuk mengambil semua data transaksi dari tabel "transactions".
- Menggunakan perulangan untuk mengiterasi setiap data transaksi yang diperoleh.
- Mengekstrak informasi penting seperti ID transaksi, ID pengguna, timestamp, dan daftar item dari setiap data transaksi.
- Menghitung total harga untuk setiap transaksi dengan mengalikan jumlah item dengan harga per item.
- Menampilkan informasi transaksi dengan menggunakan format yang sesuai.
- Menutup koneksi ke database setelah selesai.
- Dengan memenuhi semua requirements dan mencapai tujuan yang dijelaskan di atas, kode tersebut berfungsi untuk membuka koneksi ke database, mengambil data transaksi dari tabel "transactions", dan menampilkan informasi transaksi beserta total harga dari setiap transaksi yang ada dalam tabel.

**Requirements** program **view_database.py**:
- Koneksi ke database SQLite.
- Tabel **transactions** dalam database yang menyimpan data transaksi.
- Fungsi **view_database** untuk menampilkan isi tabel "transactions" dari database.
- Mengambil data transaksi dari tabel "transactions" menggunakan kueri SELECT.
- Menampilkan informasi transaksi, termasuk *ID transaksi*, *ID pengguna*, *timestamp*, *daftar item*, *jumlah item*, *harga per item*, *total harga*, dan *total belanja*.

# Ringkasan Function dan Attribute
**Attributes** pada **transaction.py**:
**user_id (str):** ID pengguna yang terkait dengan transaksi.
**items (list):** Daftar item dalam transaksi.
**transaction_history (list):** Riwayat transaksi.
**final_transaction (dict):** Dict yang mewakili transaksi terakhir.
**conn (sqlite3.Connection):** Koneksi ke database SQLite.
**cursor (sqlite3.Cursor):** Objek cursor untuk mengeksekusi kueri database.
