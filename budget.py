transactions = []

def afficher_menu():
    print("==============================")
    print("   💰 MON BUDGET TRACKER")
    print("==============================")
    print("1. Ajouter une dépense")
    print("2. Ajouter un revenu")
    print("3. Voir toutes les transactions")
    print("4. Voir le solde")
    print("5. Quitter")
    print("==============================")

while True:
    afficher_menu()
    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom de la dépense : ")
        montant = int(input("Montant : "))
        transactions.append({"nom": nom, "montant": montant, "type": "dépense"})
        print("✅ Dépense ajoutée !")

    elif choix == "2":
        nom = input("Nom du revenu : ")
        montant = int(input("Montant : "))
        transactions.append({"nom": nom, "montant": montant, "type": "revenu"})
        print("✅ Revenu ajouté !")

    elif choix == "3":
        if len(transactions) == 0:
            print("❌ Aucune transaction")
        else:
            print("--- Vos transactions ---")
            for t in transactions:
                print(t["type"].upper(), "→", t["nom"], ":", t["montant"], "FCFA")

    elif choix == "4":
        total_revenus = 0
        total_depenses = 0
        for t in transactions:
            if t["type"] == "revenu":
                total_revenus += t["montant"]
            else:
                total_depenses += t["montant"]
        solde = total_revenus - total_depenses
        print("💰 Revenus    :", total_revenus, "FCFA")
        print("💸 Dépenses   :", total_depenses, "FCFA")
        print("📊 Solde      :", solde, "FCFA")
        if solde < 0:
            print("⚠️ Attention, vous dépensez plus que vous gagnez !")
        elif solde <= 50000:
            print("💛 Budget serré, faites attention")
        else:
            print("✅ Bonne gestion, continuez ainsi !")

    elif choix == "5":
        print("Au revoir !")
        break

    else:
        print("❌ Choix invalide, essayez encore")