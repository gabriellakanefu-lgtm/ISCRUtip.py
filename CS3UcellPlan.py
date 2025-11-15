journnee = float(input("Quelle est durée de vos appelles en minutes durant la journnée en un mois?:\t"))
soiree = float(input("Quelle est durée de vos appelles en minutes durant la soirée en un mois?:\t"))
weekend = float(input("Quelle est durée de vos appelles en minutes durant le weekend dans un mois:\t"))
go = float(input("Quelle est le montant de Go/gB utiliser en un mois?:\t"))

if journnee > 100:
  (journnee - 100) * 0.25
elif journne < 100:
  journnee = 0 
elif (weekend * 0.20) => 15:
  weekend = 15
elif (weekend * 0.20) < 15:
  weekend = weekend * 0.20
soiree * 0.15
elif go > 4:
  (go - 4) * 1.50 + 30
cout_total = weekend + journee + soiree + go

print(f"Le coût total du forfait est de {cout_total}")
  


