import sqlite3

def view_database():
    conn = sqlite3.connect('transaction.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    transaction_data = cursor.fetchall()

    for data in transaction_data:
        transaction_id, timestamp, user_id, items = data
        items = eval(items)

        print(f"Transaction ID: {transaction_id}")
        print("User ID:", user_id)
        print("Timestamp:", timestamp)
        print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
        print("-----------------------------------------------------------")
        total = 0
        for i, item in enumerate(items, start=1):
            item_name, item_qty, item_price = item
            total_price = item_qty * item_price
            print(f"| {i}  | {item_name:<9} | {item_qty:<12} | {item_price:<10} | {total_price:<11} |")
            total += total_price
        print("-----------------------------------------------------------")
        print(f"Total Belanja: Rp. {total}")
        print()

    conn.close()

if __name__ == "__main__":
    view_database()
