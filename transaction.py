import datetime
import sqlite3

class Transaction:
    """
    Class representing a transaction.

    Atribut:
        user_id (str): ID pengguna yang terkait dengan transaksi.
        items (list): Daftar item dalam transaksi.
        transaction_history (list): Riwayat transaksi.
        final_transaction (dict): Dict yang mewakili transaksi terakhir.
        conn (sqlite3.Connection): Koneksi ke database SQLite.
        cursor (sqlite3.Cursor): Objek cursor untuk mengeksekusi kueri database.e queries.
    """

    def __init__(self, user_id):
        """
        Inisialisasi objek transaksi baru

        Args:
            user_id (str): ID pengguna yang terkait dengan transaksi.
        """
        self.user_id = user_id
        self.items = []
        self.transaction_history = []
        self.final_transaction = None
        self.conn = sqlite3.connect('transaction.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Membuat tabel 'transactions' jika belum ada di database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                user_id TEXT,
                items TEXT
            )
        ''')
        self.conn.commit()

    def add_item(self, item):
        """
        Menambahkan item ke transaksi

        Args:
            item (list): List yang mewakili item dalam format [nama_item, jumlah_item, harga_item].
        """
        self.items.append(item)

    def update_item(self, item_name):
        """
        Perbarui item pada transaksi

        Args:
            item_name (str): Nama item yang ingin diperbarui.
        """
        item_found = False
        for item in self.items:
            if item[0] == item_name:
                updated_name = input("Masukkan nama item yang baru (kosongkan jika tidak ingin mengubah): ")
                updated_qty = input("Masukkan jumlah item yang baru (kosongkan jika tidak ingin mengubah): ")
                updated_price = input("Masukkan harga per item yang baru (kosongkan jika tidak ingin mengubah): ")
                
                # Cek apakah ada input untuk mengubah jumlah item
                if updated_qty != "":
                    item[1] = int(updated_qty)

                # Cek apakah ada input untuk mengubah harga item
                if updated_price != "":
                    item[2] = int(updated_price)

                # Cek apakah ada input untuk mengubah nama item
                if updated_name != "":
                    item[0] = updated_name

                item_found = True
                break

        if not item_found:
            print("Item tidak terdapat pada list belanja.")

    def delete_item(self, item_name):
        """
        Menghapus item dari transaksi.

        Args:
            item_name (str): Nama item yang ingin dihapus.
        """
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def reset_transaction(self):
        """
        Reset transaksi dengan menghapus seluruh item
        """
        self.items = []

    def check_order(self):
        """
        Tampilkan item pada transaksi
        """
        if not self.items:
            print("Tidak ada item dalam transaksi Anda.")
        else:
            print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
            print("-----------------------------------------------------------")
            total = 0
            for i, item in enumerate(self.items, start=1):
                item_name, item_qty, item_price = item
                total_price = item_qty * item_price
                print(f"| {i}  | {item_name:<9} | {item_qty:<12} | {item_price:<10} | {total_price:<11} |")
                total += total_price
            print("-----------------------------------------------------------")
            print(f"Total Belanja Anda: Rp. {total}")
            print("Apakah item pada daftar belanjaan Anda sudah benar?")

    def save_transaction_to_db(self):
        """
        Simpan transaksi saat ini ke database
        """
        timestamp = datetime.datetime.now()
        transaction_data = {'timestamp': timestamp, 'user_id': self.user_id, 'items': self.items.copy()}
        self.transaction_history.append(transaction_data)

        self.cursor.execute('''
            INSERT INTO transactions (timestamp, user_id, items) VALUES (?, ?, ?)
        ''', (timestamp, self.user_id, str(self.items)))
        self.conn.commit()

    def save_final_transaction_to_db(self):
        """
        Simpan transaksi akhir ke database
        """
        timestamp = datetime.datetime.now()
        self.final_transaction = {'timestamp': timestamp, 'user_id': self.user_id, 'items': self.items.copy()}

        self.cursor.execute('''
            INSERT INTO transactions (timestamp, user_id, items) VALUES (?, ?, ?)
        ''', (timestamp, self.user_id, str(self.items)))
        self.conn.commit()

    def total_price(self):
        """
        Hitung total transaksi dan potongan sesuai dengan ketentuan

        Returns:
            float: Total harga pada seubah transaksi
        """
        total = 0
        for item in self.items:
            total += item[1] * item[2]

        if total > 500000:
            total *= 0.9
        elif total > 300000:
            total *= 0.92
        elif total > 200000:
            total *= 0.95

        return total

    def view_transaction_history(self):
        """
        Tampilkan history transaksi.
        """
        self.cursor.execute("SELECT * FROM transactions")
        transaction_data = self.cursor.fetchall()

        for i, data in enumerate(transaction_data, start=1):
            transaction_id, timestamp, user_id, items = data
            items = eval(items)

            print(f"Transaction #{transaction_id}")
            print("User ID:", user_id)
            print("Timestamp:", timestamp)
            print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
            print("-----------------------------------------------------------")
            total = 0
            for j, item in enumerate(items, start=1):
                item_name, item_qty, item_price = item
                total_price = item_qty * item_price
                print(f"| {j}  | {item_name:<9} | {item_qty:<12} | {item_price:<10} | {total_price:<11} |")
                total += total_price
            print("-----------------------------------------------------------")
            print(f"Total Belanja: Rp. {total}")
            print()

    def save_transaction(self):
        """
        Simpan transaksi ke database
        """
        self.save_transaction_to_db()

    def close_connection(self):
        """
        Tutup koneksi ke database
        """
        self.conn.close()
