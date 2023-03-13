import random;

nbr_min=5
nbr_max=10
solution=0
nbr_question=4
nbr_point=0


def calcule_nombre():
    nbr_aleatoire1=random.randint(nbr_min,nbr_max)
    nbr_aleatoire2=random.randint(nbr_min,nbr_max)
    o=random.randint(0,1)
    calcul="*"
    solution=nbr_aleatoire1*nbr_aleatoire2
    if o==1:
        calcul="+"
    result=input(f"calculez : {nbr_aleatoire1} {calcul} {nbr_aleatoire2} = " )
    if o==1:
        solution=nbr_aleatoire1+nbr_aleatoire2
    results = int(result)
    if results==solution:
        print("reponse correcte")
        return True
    else :
        print("reponse incorrect")
        
for i in range(1,nbr_question+1):    
    b=calcule_nombre()
    c=nbr_question-i
    if b==True:
        nbr_point+=1
    print("il vous restes :" + str(c))

nbr_reponse=str(nbr_point)+"/"+str(nbr_question)

print("vous avez " + nbr_reponse)
moyenne=int(nbr_question/2)
if nbr_point==nbr_question :
    print("Excellent vous maitrisez vos maths")
elif nbr_point==0:
    print("revisez vos maths")
elif nbr_point<moyenne:
    print("vous pouvez mieux faire")
else :
    print("pas mal")




