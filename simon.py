import random;
import time;
import os;

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


nbr_generes=""
score=0
for i in range(4):
        nbr_genere= random.randint(0,9)
        nbr_generes+=str(nbr_genere)
    

print("Memoriser la sequence : ")
print(nbr_generes)
time.sleep(3)
clear_screen()
nbr_repondu=input("Entrer la sequence " )
if nbr_repondu==nbr_generes:
    while True:
            score+=1
            nbr_regenere=random.randint(0,9)
            nbr_regeneres=str(nbr_regenere)
            nbr_generes+=nbr_regeneres
            print("Memoriser la sequence : ")
            print(nbr_generes)
            time.sleep(3)
            clear_screen()
            rereponse=input("Entrer la sequence ")
            if not rereponse==nbr_generes:
                print("mauvaise reponse la sequence était : " + nbr_generes)
                break;
                
    print("votre score finale est " +str(score))
else:
    print("mauvaise reponse la sequence étatit : " +nbr_generes)
    score+=score
