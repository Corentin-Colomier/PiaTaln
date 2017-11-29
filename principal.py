import encodings
import fonction
import unicodedata
import urllib.parse
import urllib.request
from pyDatalog import pyDatalog


mot_un = 'félins'
mot_deux = 'cordés'
mot_un_change = fonction.change_requete(mot_un)
mot_deux_change = fonction.change_requete(mot_deux)
object_mot_un = fonction.retourner_objet_mot(mot_un_change)
object_mot_deux = fonction.retourner_objet_mot(mot_deux_change)



print("zzz")
for x in object_mot_un.noeuds :
    if ';'+str(object_mot_un.mot)+';' in x :
        ligne = str(x).split(";")
        id_mot_un = ligne[1]

for x in object_mot_deux.noeuds :
    if ';'+str(object_mot_deux.mot)+';' in x :
        ligne = str(x).split(";")
        id_mot_deux = ligne[1]

print(object_mot_un.mot)
print(id_mot_un)
print(object_mot_deux.mot)
print(id_mot_deux)


pyDatalog.create_terms('A,B,C,D,E,F,r_isa')
for c in object_mot_un.relation_sortant :
    if ';6;' in c :
        ligne = str(c).split(";")
        + r_isa(ligne[2],ligne[3],ligne[1])

for c in object_mot_deux.relation_entrant :
    if ';6;' in c :
        ligne = str(c).split(";")
        + r_isa(ligne[2],ligne[3],ligne[1])

print(r_isa(str(id_mot_un),B,C)&r_isa(B,str(id_mot_deux),F))
print()