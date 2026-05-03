from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("budget.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def accueil():
    conn = get_db()
    cursor = conn.cursor()
    
    # Récupérer toutes les transactions
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    
    # Calculer les totaux
    cursor.execute("SELECT SUM(montant) FROM transactions WHERE type='revenu'")
    total_revenus = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT SUM(montant) FROM transactions WHERE type='dépense'")
    total_depenses = cursor.fetchone()[0] or 0
    
    solde = total_revenus - total_depenses
    
    # Dépenses par catégorie
    cursor.execute("""
        SELECT categorie, SUM(montant) 
        FROM transactions 
        WHERE type='dépense' 
        GROUP BY categorie
    """)
    categories = cursor.fetchall()
    cat_labels = [c[0] for c in categories]
    cat_valeurs = [c[1] for c in categories]
    
    conn.close()
    
    return render_template("index.html",
        transactions=transactions,
        total_revenus=total_revenus,
        total_depenses=total_depenses,
        solde=solde,
        cat_labels=cat_labels,
        cat_valeurs=cat_valeurs
    )

@app.route("/ajouter", methods=["POST"])
def ajouter():
    nom = request.form["nom"]
    montant = int(request.form["montant"])
    type_tx = request.form["type"]
    categorie = request.form["categorie"]
    
    conn = get_db()
    conn.execute("""
        INSERT INTO transactions (nom, montant, type, categorie)
        VALUES (?, ?, ?, ?)
    """, (nom, montant, type_tx, categorie))
    conn.commit()
    conn.close()
    
    return redirect("/")

@app.route("/supprimer/<int:id>", methods=["POST"])
def supprimer(id):
    conn = get_db()
    conn.execute("DELETE FROM transactions WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)