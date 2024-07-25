import json
from sys import argv


def find_monkey(prison):
    # ouverture d'un fichier en mode lécture         
    try:
        #with ouverture, fermeture securiser 
        # open fonction de python ouvrire des  fichiers.
        with open(prison, 'r') as fils:                  
            json_data = fils.read()
            ile = json.loads(json_data)
            #print(f'iciiii monsieur {data}')

            for prison in ile:
                # print('////////////////////')
                # print(prison)
                # le prisoners est a l'interieur de la prison 
                prisoners = prison["prisoners"]
                # print('*********************')
                # print(prisoners)
                # print('////////////////////')
                for prisoner in prisoners:
                    # print(prisoner['species'])
                    # dans species en a forgotten one,Deku Baba, Monkey

                    if prisoner ['species'] == 'Monkey':
                        print('The monkey is in the cell number 3')

                # for prisonner in number:
                #     print(prisonner)

                    # for Monkey in prisonner:
                    #     print(Monkey)

                    # if Monkey == number 1 :
                    # print("The monkey is in the cell number 3")
                    # elif Monkey == 'number': 2
                    # print("The monkey is in the cell number 3")
                    # elif Monkey == number 3:
                    #       print("The monkey is in the cell number 3")
    


    # si la classe est executé c'est ok.
    # sinon en sotte ver excepté pour l'executer afin d'éviter un crache
    except FileNotFoundError:
        print("le fichier n'existe pas")                

    #prison=json.load(fils)
    #json.dump() ingecter dans le dictionnaire


if len(argv) == 1:
    print("Pas d'argument.")
if len(argv) == 2:
    find_monkey(argv[1])

 
if len(argv) == 0:
    print("le fichier n'existe pas")



    


