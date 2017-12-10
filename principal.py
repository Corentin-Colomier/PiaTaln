import encodings
import fonction
import unicodedata
import urllib.parse
import urllib.request
from pyDatalog import pyDatalog

# r_agent_un <==> r_agent-1

mot_un = 'félins'
mot_deux = 'cordés'
mot_un_change = fonction.change_requete(mot_un)
mot_deux_change = fonction.change_requete(mot_deux)
object_mot_un = fonction.retourner_objet_mot(mot_un_change)
object_mot_deux = fonction.retourner_objet_mot(mot_deux_change)

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

pyDatalog.create_terms('A,B,C,D,E,F,r_isa,cat_generique,cat_action,cat_caracteristique,'
                       'cat_associe,cat_inhibition,cat_preparation,r_syn,r_holo,r_lemma,r_agent-1,r_has_part,'
                       'r_carac,r_color,r_associated,r_inhib,r_potential_confusion,c_c,a_a,b_b,'
                       'r_but,r_sentiment,r_pos,r_agent_un')

+ c_c("dk","dh")
+ a_a("chat","chien")
b_b(B,A) <= a_a(A,B)
b_b(A,B) <= c_c(A,B)
#---
cat_preparation(A,B,C) <= r_pos(A,B,C)
#---
cat_generique(A,B,C) <= r_isa(A,B,C)
cat_generique(A,B,C) <= r_syn(A,B,C)
cat_generique(A,B,C) <= r_holo(A,B,C)
cat_generique(A,B,C) <= r_lemma(A,B,C)
#---
cat_action(A,B,C) <= r_agent_un(A,B,C)
#---
cat_caracteristique(A,B,C) <= r_has_part(A,B,C)
cat_caracteristique(A,B,C) <= r_carac(A,B,C)
cat_caracteristique(A,B,C) <= r_color(A,B,C)
cat_caracteristique(A,B,C) <= r_but(A,B,C)
cat_caracteristique(A,B,C) <= r_sentiment(A,B,C)
#---
cat_associe(A,B,C) <= r_associated(A,B,C)
#---
cat_inhibition(A,B,C) <= r_inhib(A,B,C)

for c in object_mot_un.relation_sortant :
    if ';6;' in c :
        ligne = str(c).split(";")
        + r_isa(ligne[2],ligne[3],ligne[1])
    elif ';4;' in c :
        ligne = str(c).split(";")
        + r_pos(ligne[2],ligne[3],ligne[1])
    elif ';5;' in c :
        ligne = str(c).split(";")
        + r_syn(ligne[2],ligne[3],ligne[1])
    elif ';10;' in c :
        ligne = str(c).split(";")
        + r_holo(ligne[2],ligne[3],ligne[1])
    elif ';19;' in c :
        ligne = str(c).split(";")
        + r_lemma(ligne[2],ligne[3],ligne[1])
    elif ';24;' in c :
        ligne = str(c).split(";")
        + r_agent_un(ligne[2],ligne[3],ligne[1])
    elif ';9;' in c :
        ligne = str(c).split(";")
        + r_has_part(ligne[2],ligne[3],ligne[1])
    elif ';17;' in c :
        ligne = str(c).split(";")
        + r_carac(ligne[2],ligne[3],ligne[1])
    elif ';87;' in c :
        ligne = str(c).split(";")
        + r_color(ligne[2],ligne[3],ligne[1])
    elif ';100;' in c :
        ligne = str(c).split(";")
        + r_but(ligne[2],ligne[3],ligne[1])
    elif ';32;' in c :
        ligne = str(c).split(";")
        + r_sentiment(ligne[2],ligne[3],ligne[1])
    elif ';0;' in c :
        ligne = str(c).split(";")
        + r_associated(ligne[2],ligne[3],ligne[1])
    elif ';130;' in c :
        ligne = str(c).split(";")
        + r_inhib(ligne[2],ligne[3],ligne[1])
    else:
        pass

for c in object_mot_deux.relation_entrant :
    if ';6;' in c :
        ligne = str(c).split(";")
        + r_isa(ligne[2],ligne[3],ligne[1])
    elif ';4;' in c :
        ligne = str(c).split(";")
        + r_pos(ligne[2],ligne[3],ligne[1])
    elif ';5;' in c :
        ligne = str(c).split(";")
        + r_syn(ligne[2],ligne[3],ligne[1])
    elif ';10;' in c :
        ligne = str(c).split(";")
        + r_holo(ligne[2],ligne[3],ligne[1])
    elif ';19;' in c :
        ligne = str(c).split(";")
        + r_lemma(ligne[2],ligne[3],ligne[1])
    elif ';24;' in c :
        ligne = str(c).split(";")
        + r_agent_un(ligne[2],ligne[3],ligne[1])
    elif ';9;' in c :
        ligne = str(c).split(";")
        + r_has_part(ligne[2],ligne[3],ligne[1])
    elif ';17;' in c :
        ligne = str(c).split(";")
        + r_carac(ligne[2],ligne[3],ligne[1])
    elif ';87;' in c :
        ligne = str(c).split(";")
        + r_color(ligne[2],ligne[3],ligne[1])
    elif ';100;' in c :
        ligne = str(c).split(";")
        + r_but(ligne[2],ligne[3],ligne[1])
    elif ';32;' in c :
        ligne = str(c).split(";")
        + r_sentiment(ligne[2],ligne[3],ligne[1])
    elif ';0;' in c :
        ligne = str(c).split(";")
        + r_associated(ligne[2],ligne[3],ligne[1])
    elif ';130;' in c :
        ligne = str(c).split(";")
        + r_inhib(ligne[2],ligne[3],ligne[1])
    else:
        pass

try:
    print(cat_generique(str(id_mot_un),B,C)&cat_action(B,str(id_mot_deux),F))
except AttributeError:
    print("ops")

try:
    print(cat_caracteristique(str(id_mot_un), B, C) & cat_action(B, str(id_mot_deux), F))
except AttributeError:
    print("ops")

#print(cat_generique(str(id_mot_un),B,C)&cat_action(B,str(id_mot_deux),F))
print(b_b(A,B))