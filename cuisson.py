
import time

print("1: Oeufs à la coque : 3 minutes")
print("2: Oeufs mollets : 6 minutes")
print("3: Oeufs durs : 9 minutes")

choix=input("choissisez une option ")
duree=0
if choix=="1":
    duree=3*60
if choix=="2":
    duree=6*60
if choix=="3":
    duree==9*60

while duree>0:
     for i in range(10):
            time.sleep(1)
            duree-=1
            print(".", end="", flush=True )

     min = duree//60
     sec= duree-min*60
     terminer=input("appuyer q pour terminer")
     print(f"Temps restant : {min:02d}:{sec:02d} " , end="", flush=True )
        

     
print("cuisson terminée")