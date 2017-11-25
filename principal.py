import fonction
import urllib.parse
import urllib.request
from pyDatalog import pyDatalog
# print("entre le premier mot ?")
# entre_un = input()
#
# print("entre le deuxieme mot ?")
# entre_deux = input()

objet_mot_un = fonction.retourner_objet_mot('maison')
objet_mot_deux = fonction.retourner_objet_mot('habitation')

print("zzz")
for x in objet_mot_un.noeuds :
    if ';maison;' in x :
        ligne = str(x).split(";")
        id_maison = ligne[1]

for x in objet_mot_un.noeuds :
    if ';habitation;' in x :
        ligne = str(x).split(";")
        id_habitation = ligne[1]

print(id_maison)

pyDatalog.create_terms('X,Y,Z,W,r_isa')

for c in objet_mot_un.relation_sortant :
    if ';6;' in c :
        ligne = str(c).split(";")
        + r_isa(ligne[2],ligne[3],ligne[1])

print(r_isa(id_maison,id_habitation,Z))
print()