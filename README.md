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
**Flowchart program utama** \
![flow_chart_transaction-Page-1](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/4f10d196-cf90-4201-af31-598db0ca7aa5) 

**Flowchart Create_Item** \
![flow_chart_transaction-Page-3](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/b35ce5d5-38ab-4dff-987b-a1f9e4c4d0ad) 

**Flowchart Add_item** \
![flow_chart_transaction-Page-2](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/3e1644be-71af-464e-a1c3-8f172c3e8552) 

**Flowchart update_item** \
![flow_chart_transaction-Page-4 (1)](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/f7f248bb-4f65-4ade-a392-a8d189d90039)

**Flowchart delete_item** \
![flow_chart_transaction-Page-5](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/cd079d01-cb57-4df5-9208-5f6e9e5b7f52)

**flowchart batalkan transaksi** \
![flow_chart_transaction-Page-6](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/ac150495-ecd5-4ced-8cd4-b992641e6491)

**flowchart cek order** \
![flow_chart_transaction-Page-7](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/90869005-df14-4e61-bd6a-1e3f75251ecb)

**flowchart total harga** \
![flow_chart_transaction-Page-8](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/a36d0fd3-540a-4375-a8a3-c8211cd81700)

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

- Selanjutnya masukkan no ID (pada contoh ini dimasukkan angka 33), kemudian tekan *enter* (tampilan)
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/6d7c0bb9-b0ec-4b6f-9ee8-96d86420bd80)\
pengguna dapat melakukan transaksi suai dengan pilihan yang sudah tertera

- **Test 1** 
1. customer dapat menambahkan item barang yang akan dibeli dengan cara masukkan angka **1** kemudian *enter* 
2. Masukkan **nama item** yang akan dibeli kemudian tekan *enter*
3. Masukkan **jumlah item** yang dibeli kemudian tekan *enter*
4. Masukkan **harga per item** kemudian tekan *enter*\
**expected output :** \
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/b29187d3-9f41-4418-82b5-4b0001c37736)

  Jika ingin memasukka item lain yang akan dibeli, ulangi langkah 1 - 4 \
**expected output :** \
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/6f4be6df-cc5c-40c4-9275-ebd8ace8e347) \

**Test 2** \
Jika customer ingin memeriksa item apa saja yang sudah dimasukkan, maka dapat memasukkan angka **4** pada pilihan menu. \
**expected output :** \
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/77082b57-d139-438d-a6fe-98976c3ff738)

**Test 3** \
Jika setelah memeriksa item yang sudah dimasukkan, customer merasa ada kesalahan input sehingga harus mengahapus item dari daftar yang telah dimasukkan. Maka customer dapat memasukkan pilihan **3** untuk menghapus item yang diinginkan dari daftar belanja, selanjutnya customer memasukkan nama barang yang akan dihapus dari daftar. \
**expected output :** \
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/a33c54d8-732d-4364-83cf-7bddf1c666c8) \
kemudian jika diperiksa pada daftar belanja, item yang dihapus telah hilang dari daftar \
**expected output :** \
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/74f811f0-aaf0-4051-84a0-c66000746d5a)

**Test 4** \
Setelah customer memeriksa daftar belanja nya kembali, cusotmer menyadari ada kesalahan nama barang, jumlah dan harga yang dimasukkan. Maka customer dapat memasukkan pilihan **2** pada menu utama. Kemudian customer dapat memasukkan nama item yang ingin diupdate. Selanjutnya customer dapat memasukkan nama item yang baru (jika tidak ada perubahan cukup tekan *enter* saja), jumlah item yang baru (Jika tidak ada yang berubah tekan *enter* saja), harga per item yang baru (jika tidak ada yang berubah tekan *enter* saja). \
**expected output :** \
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/610282a8-de50-4730-990f-a6fac7eb2865) \
Jika customer periksa daftar belanja lagi, maka daftar belanja sudah diupdate sesuai dengan keinginan \
**expected output :** \
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/c817568b-d634-4c36-a4b4-97708e626dfb) \
Dapat dilihat dari gambar di atas, nama item dan jumlah item telah diubah melalui menu pilihan no **2**  sedangkan harga/item tetap karena customer tidak melakukan perubahan harga/item

**Test 5** \
Setelah customer memasukkan kembali item barang belanja melalui menu pilihan no **1**, customer melakukan periksa barang kembali \
**expected output :** \
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/e66ad4de-b2b3-43cf-9a9a-21e1d8fe3d37) \
Setelah melihat daftar belanja tersebut, customer ingin menghapus semua daftar belanja yang telah dimasukkan karena suatu alasan tertentu. Maka customer dapat memilih menu pilihan **6** untuk membatalkan daftar belanja (reset transaksi). Setelah itu daftar belanja akan kosong \
**expected output :** \
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/a88b4645-74ca-4758-bd8c-6986d1a13b3b)

**Test 6** \
Customer kembali memasukkan item belanjaan yang baru. kemudian kembali memeriksa barang yang telah dimasukkan ke daftar belanja \
**expected output :** \
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/5b517849-85dc-4bbe-b9b0-08a8902ab996) \
Setelah memeriksa daftar belanja yang telah dimasukkan, customer melakukan pembayaran. Untuk melakukan pembayaran, customer memasukkan pilihan **5** untuk mengetahui harga yang harus di bayar. Pada aplikasi ini terdapat ketentuan besaran diskon sesuai dengan total harga pembelian. \
Jika total harga > Rp. 200.000 maka akan mendapat diskon 5% \
Jika total harga > Rp. 300.000 maka akan mendapat diskon 5% \
Jika total harga > Rp. 500.000 maka akan mendapat diskon 10% \
**expected output :** \
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/183cdfde-c0b6-45a3-a138-d6def27e3b16) 
\
Selanjutnya customer dapat keluar dari aplikasi dengan memasukkan pilihan **0**, kemudian aplikasi angka tertutup  \
**expected output :**\
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/5af4aace-844d-475e-bbcd-3e72c9451df8)

**Test 7**\
Pemilik usaha dapat melihat seluruh aktivitas transaksi yang telah dilakukan oleh customer karena seluruh aktifitas transaksi disimpan ke dalam database. Pemilik usaha dapat menjalankan program **view_database.py** melalui command prompt
**expected output :**\
![image](https://github.com/rianrahmanda/super_cashier_pacmann/assets/51916650/ececab1a-4555-4985-8a43-00e4a6f19957) \
Data transaksi dapat digunakan untuk menggali informasi perilaku customer dengan menggunakan pendekatan statistika ataupun machine learning.

**Kesimpulan**
Program di atas adalah sebuah program Python yang mengimplementasikan kelas Transaction untuk melakukan operasi pada transaksi. Program ini memungkinkan pengguna untuk menambah, mengupdate, menghapus, dan memeriksa item dalam transaksi, menghitung total harga belanja dengan diskon, serta melihat riwayat transaksi. Dengan program ini, pengguna dapat dengan mudah mengelola transaksi, termasuk menambah, mengupdate, menghapus, dan melihat riwayat transaksi dengan total harga belanja yang dihitung secara otomatis.
