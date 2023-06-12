Atrribute pada **transcation.py**:
-- **user_id (str):** ID pengguna yang terkait dengan transaksi.
-- **items (list):** Daftar item dalam transaksi.
transaction_history (list): Riwayat transaksi.
final_transaction (dict): Dict yang mewakili transaksi terakhir.
conn (sqlite3.Connection): Koneksi ke database SQLite.
cursor (sqlite3.Cursor): Objek cursor untuk mengeksekusi kueri database.
