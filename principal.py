import fonction
import urllib.parse
import urllib.request

print("entre le premier mot ?")
entre_un = input()
# print("entre le deuxieme mot ?")
# mot_deux = input()

# rezo_deux = model.fonction.importerRezo(mot_deux)
objet_mot = fonction.retourner_objet_mot(entre_un)
objet_mot.toString()