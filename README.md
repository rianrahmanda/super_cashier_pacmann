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
- **user_id (str):** ID pengguna yang terkait dengan transaksi.
- **items (list):** Daftar item dalam transaksi.
- **transaction_history (list):** Riwayat transaksi.
- **final_transaction (dict):** Dict yang mewakili transaksi terakhir.
- **conn (sqlite3.Connection):** Koneksi ke database SQLite.
- **cursor (sqlite3.Cursor):** Objek cursor untuk mengeksekusi kueri database.\

**Method** pada **transaction.py**:
- **init(self, user_id):** Inisialisasi objek transaksi baru.
- **create_table(self):** Membuat tabel 'transactions' jika belum ada di database.
- **add_item(self, item):** Menambahkan item ke transaksi.
- **update_item(self, item_name):** Perbarui item pada transaksi.
- **delete_item(self, item_name):** Menghapus item dari transaksi.
- **reset_transaction(self):** Reset transaksi dengan menghapus seluruh item.
- **check_order(self):** Tampilkan item pada transaksi.
- **save_transaction_to_db(self):** Simpan transaksi saat ini ke database.
- **save_final_transaction_to_db(self):** Simpan transaksi akhir ke database.
- **total_price(self):** Hitung total transaksi dan potongan sesuai dengan ketentuan.
- **view_transaction_history(self):** Tampilkan history transaksi.
- **save_transaction(self):** Simpan transaksi ke database.
- **close_connection(self):** Tutup koneksi ke database.

# Flowchart
# Demonstrasi Program
Setelah program diunduh, harus disimpan kedalam direktori yang sama:\
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/ed281a66-194f-427b-b2a4-4aa938812f29)

Buka **command prompt** dengan cara mengklik simbol **windows** dan ketikkan cmd kemudian tekan *enter*
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/af2a2453-6bf4-473d-bb0b-1d4d3d06b1b0)

Akses direktori tempat ketiga file **super_cashier** disimpan. Karena file yang disimpan (dalam kasus saya) pada direktori D (dapat dilihat pada gambar pertama), maka pada **command prompt** nya ketikkan perintah di bawah ini secara berurutan:
- **D:**, kemudian tekan *enter*, maka tampilannya akan seperti gambar di bawah ini
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/f479f9b4-ac4e-4d39-a5c2-a6b548e7413d)

- **cd "pacmann academy"**, kemudian tekan *enter* (tampilan)
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/b99f0ea1-7d81-4d23-abe1-c3d724671929)

- **cd "final project python I"**, kemudian tekan *enter* (tampilan)
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/0b9b63b3-2869-4ef5-88b3-13d17bf58ef1)

- **python main_cashier.py**, kemudian tekan *enter* (tampilan)
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/f92cfd43-f75b-4466-be66-a6c38fd48195)



# Kesimpulan
