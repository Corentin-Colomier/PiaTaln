import fonction
import urllib.parse
import urllib.request
from pyDatalog import pyDatalog
# print("entre le premier mot ?")
# entre_un = input()
#
# print("entre le deuxieme mot ?")
# entre_deux = input()

objet_mot_un = fonction.retourner_objet_mot('plante')
objet_mot_deux = fonction.retourner_objet_mot('place')

print("zzz")
for x in objet_mot_un.noeuds :
    if ';'+str(objet_mot_un.mot)+';' in x :
        ligne = str(x).split(";")
        id_mot_un = ligne[1]

for x in objet_mot_deux.noeuds :
    if ';'+str(objet_mot_deux.mot)+';' in x :
        ligne = str(x).split(";")
        id_mot_deux = ligne[1]

print(id_mot_un)
print(id_mot_deux)


pyDatalog.create_terms('X,Y,Z,W,r_isa')
for c in objet_mot_un.relation_sortant :
    if ';6;' in c :
        ligne = str(c).split(";")
        + r_isa(ligne[2],ligne[3],ligne[1])

for c in objet_mot_deux.relation_sortant :
    if ';6;' in c :
        ligne = str(c).split(";")
        + r_isa(ligne[2],ligne[3],ligne[1])

print(r_isa(str(id_mot_un),Y,Z)&r_isa(str(id_mot_deux),Y,W))
print()