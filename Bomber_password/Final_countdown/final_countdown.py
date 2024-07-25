
from sys import argv
def final_countdown(n,message):
    mins, secs = divmod(n, 60)  # premiere etape affiche en ( minute,seconde )
  
    while mins >= 0:
       
        while secs >= 1:
            if mins == 0 :
                if secs <=10 :  #deuxième etape affiche segonde +...
                    print(f"{secs}...") #formatage : insér seonde +...
                else:
                    print(secs)
            else:
                print(f"{mins}'{secs}")  # premiere etape affiche minute+seconde
            
            secs -= 1 # les seconde commence de - ou = a 1 minute
        mins -= 1   # quon la seconde >=0
        secs = 59
    print(message.upper() + "!")
    
if len(argv) == 1:
    print("Pas de compteur") 
if len(argv) == 2:
    print("Pas de message")

if len(argv) == 3:
    if argv[1].isdigit():
        final_countdown(int(argv[1]),argv[2])
    else:
        print("Pas de compteur")









