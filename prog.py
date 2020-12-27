# Saisie controlée des notes de controle et de synthése
while True:
    nc= float(input("donner la nc  : "))
    ns= float(input("donner la ns  : "))
    if (0.00<=nc<=20.00 ) and (0.00<=ns<=20.00 ):
        break;
    

# Calcul de la moyenne
    
moy=(nc+2*ns)/3


# Affichage de la moyenne

print("la moyenne = ",moy)