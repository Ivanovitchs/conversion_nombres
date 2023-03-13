convertisseur=input("vous souhaitez convertir pouces vers cm ou cm vers pouces ? " )
sortir=0
if convertisseur=="pouces vers cm":
    while sortir==0:
        try:
            cm=int(input("entrer la valeur à convertir (inch) " ))
            converte=float(round(cm*2.54,2))
            print(str(converte)+ " cm")
            print("Appuyer sur Enter pour sortir")
        except ValueError:
            break;
       
elif convertisseur=="cm vers pouces":
    while sortir==0:
        try:
            cm=int(input("entrer la valeur à convertir (cm) "))
            converte=float(round(cm*0.394,2))
            print(str(converte)+ " inch")
            print("Appuyer sur Enter pour sortir")
        except ValueError:
            break;
    