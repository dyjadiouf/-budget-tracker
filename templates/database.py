import sqlite3

def init_db():
    conn = sqlite3.connect("budget.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            montant INTEGER NOT NULL,
            type TEXT NOT NULL,
            categorie TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Base de données créée !")

init_db()