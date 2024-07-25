from sys import argv

def bomber_password(animal, repeat):
    if animal == "dogs" or animal == "cats" or animal == "cow":
        result = ""
        for nb in range (repeat):  # parcourir un ensemble de code un nombre de fois
            if animal == "dogs":
                result += "bark"
                if nb == repeat -1:
                    result += "!"
                else:
                    result += " " 
                    

            elif animal == "cats":
                result += "meow"
                if nb == repeat -1:
                    result += "!"
                else:
                    result += " " 

            elif animal == "cow":
                result += "mow"
                if nb == repeat -1:
                    result += "!"
                else:
                    result += " "
    
        print(result)       
    else:
        print("Je ne connais pas cette espèce")

        
#bomber_password("dogs", 3)
#bomber_password("cats", 5)
#bomber_password("chicken", 5)
    

if len(argv) == 3:  # La len()fonction renvoie le nombre d'éléments dans un objet.
    if argv[2].isdigit(): # La isdigit()méthode renvoie True si tous les caractères sont des chiffres, sinon False.
        repeat = int(argv[2])
        if repeat < 0:   
            print("Le nombre n'est pas reconnu")
        else:   
            bomber_password(argv[1],repeat)
    else:
        print("Le nombre n'est pas reconnu")
else:
    print("Pas d'argument")
    

