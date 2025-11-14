sous_total = float(input("Quel est le montant de votre sous-total ?:\t"))
pourboire = input("Souhaitez-vous ajouter un pourboire ?(Oui/Non):\t")

if pourboire.lower() == "oui":
    x1 = input("Souhaitez-vous donner un montant précis ?(Oui/Non):\t")
    if x1.lower() == "oui":
        p = float(input("Quel est le montant précis souhaité ?:\t"))
        taxes = sous_total * 0.13
        cout_finale = sous_total + taxes + p 
        print(f"\nSous-Total: {sous_total}")
        print(f"Taxes: {round(taxes, 2)}")
        print(f"Pourboire: {round(p,1)}")
        print(f"Total finale: {round(cout_finale, 2)}")

    else:
        x2 = input("Souhaiteriez-vous donner un certain pourcentage ? (Oui/Non):\t")
        if x2.lower() == "oui":
            p = float(input("Quel est le pourcentage souhaité ?:\t"))
            p1 = (p / 100) * sous_total
            taxes = sous_total * 0.13
            cout_finale = sous_total + taxes + p1
            print(f"\nSous-Total: {sous_total}")
            print(f"Taxes: {round(taxes, 2)}")
            print(f"Pourboire: {round(p1,2)}")
            print(f"Total finale: {round(cout_finale, 2)}")

else:
    taxes = sous_total * 0.13
    cout_finale = sous_total + taxes
    print(f"\nSubtotal: {sous_total}")
    print(f"Taxes: {round(taxes, 2)}")
    print(f"Total finale: {round(cout_finale, 2)}")

