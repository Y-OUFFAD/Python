
#import json
# import json,urllib
# import urllib.request
# import re
# from sys import argv



import json
import requests
from sys import argv


def get_secret_ingredients(path):
    try:
        url = requests.get(path)
        text = url.text
        data = json.loads(text)
        #json_data = f.read()
        #data = json.loads(json_data)
        print(data) 
    except:
        print("Erreur lors de la requete")



if len(argv) == 2:
    get_secret_ingredients(argv[1])

    

elif len(argv) == 1:
     
     #get_secret_ingredients(argv[0])

    print("Pas d'argument")


# url = requests.get("https://pastebin.com/raw/tHgDw2YB")
# text = url.text

# data = json.loads(text)

# # user = data[0]
# print(data)

