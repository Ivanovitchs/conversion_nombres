
def funct_convert(unite1,unite2,facteur):
        cm= input("conversion de " + str(unite1) + " vers " + str(unite2) + ". Donnez la valeur en " + str(unite1 ) + ". appuyer sur la touche q pour terminer " )
        if cm=="q":
            return True
        cms=float(cm)
        converte=float(round(cms*facteur,2))
        print("le resultats de la conversion est : " + str(converte))
        return False

print("convertion des nombres")
print("taper 1 pour la convertion des pouces vers cm")
print("taper 2 pour la convertion des cm vers pouces")
choix=input("entrer votre choix " )

if choix=="1":
    while True:
        if funct_convert("inch","cm",5.64):
            break
elif choix=="2":
    while True:
        if funct_convert("cm","inch",0.36):
            break
        