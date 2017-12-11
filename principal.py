from urllib.parse import quote
import fonction
from pyDatalog import pyDatalog

format_jdm = 'iso-8859-1'
# r_agent_un <==> r_agent-1

#prend les entres et creer les objet on fonction
mot_un = 'félin'
mot_deux = 'évoluer'
action = 'r_can'

object_mot_un = fonction.retourner_objet_mot(mot_un)
object_mot_deux = fonction.retourner_objet_mot(mot_deux)

print(object_mot_un.mot)

#recupere les id des mots tout en prend en compte le raffinement sementique
id_mot_un = fonction.select_id(object_mot_un)
id_mot_deux = fonction.select_id(object_mot_deux)

print(id_mot_un)
print(id_mot_deux)

#creer la base de donne prolog
pyDatalog.create_terms('PAR,RELATION_UN,RELATION_DEUX,ID_RELATION_UN,ID_RELATION_DEUX,A,B,C,D,E,F,W,Y,POID,POID_UN,POID_DEUX,r_isa,cat_generique,cat_action,cat_caracteristique,'
                       'cat_associe,cat_inhibition,cat_preparation,r_syn,r_holo,r_lemma,r_agent-1,r_has_part,'
                       'r_carac,r_color,r_associated,r_inhib,r_potential_confusion,c_c,a_a,b_b,'
                       'r_but,r_sentiment,r_pos,r_agent_un')
#---
cat_preparation(A,B,C,'r_po',POID) <= r_pos(A,B,C,POID)
#---
cat_generique(A,B,C,'is_a',POID) <= r_isa(A,B,C,POID)
cat_generique(A,B,C,'syn',POID) <= r_syn(A,B,C,POID)
cat_generique(A,B,C,'holo',POID) <= r_holo(A,B,C,POID)
cat_generique(A,B,C,'lemma',POID) <= r_lemma(A,B,C,POID)
#---
cat_action(A,B,C,'agent - 1',POID) <= r_agent_un(A,B,C,POID)
#---
cat_caracteristique(A,B,C,'has_part',POID) <= r_has_part(A,B,C,POID)
cat_caracteristique(A,B,C,'carac',POID) <= r_carac(A,B,C,POID)
cat_caracteristique(A,B,C,'color',POID) <= r_color(A,B,C,POID)
cat_caracteristique(A,B,C,'but',POID) <= r_but(A,B,C,POID)
cat_caracteristique(A,B,C,'sentiment',POID) <= r_sentiment(A,B,C,POID)
#---
cat_associe(A,B,C,'asso',POID) <= r_associated(A,B,C,POID)
#---
cat_inhibition(A,B,C,'ini',POID) <= r_inhib(A,B,C,POID)
#evite les exeption
+ r_isa("a","b","c","d")
+ r_pos("a","b","c","d")
+ r_syn("a","b","c","d")
+ r_holo("a","b","c","d")
+ r_lemma("a","b","c","d")
+ r_agent_un("a","b","c","d")
+ r_has_part("a","b","c","d")
+ r_carac("a","b","c","d")
+ r_color("a","b","c","d")
+ r_but("a","b","c","d")
+ r_sentiment("a","b","c","d")
+ r_associated("a","b","c","d")
+ r_inhib("a","b","c","d")
#creer les fait de la base
for c in object_mot_un.relation_sortant :
    if ';6;' in c :
        ligne = str(c).split(";")
        + r_isa(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';4;' in c :
        ligne = str(c).split(";")
        + r_pos(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';5;' in c :
        ligne = str(c).split(";")
        + r_syn(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';10;' in c :
        ligne = str(c).split(";")
        + r_holo(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';19;' in c :
        ligne = str(c).split(";")
        + r_lemma(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';24;' in c :
        ligne = str(c).split(";")
        + r_agent_un(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';9;' in c :
        ligne = str(c).split(";")
        + r_has_part(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';17;' in c :
        ligne = str(c).split(";")
        + r_carac(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';87;' in c :
        ligne = str(c).split(";")
        + r_color(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';100;' in c :
        ligne = str(c).split(";")
        + r_but(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';32;' in c :
        ligne = str(c).split(";")
        + r_sentiment(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';0;' in c :
        ligne = str(c).split(";")
        + r_associated(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';130;' in c :
        ligne = str(c).split(";")
        + r_inhib(ligne[2],ligne[3],ligne[1],ligne[5])
    else:
        pass

for c in object_mot_deux.relation_entrant :
    if ';6;' in c :
        ligne = str(c).split(";")
        + r_isa(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';4;' in c :
        ligne = str(c).split(";")
        + r_pos(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';5;' in c :
        ligne = str(c).split(";")
        + r_syn(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';10;' in c :
        ligne = str(c).split(";")
        + r_holo(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';19;' in c :
        ligne = str(c).split(";")
        + r_lemma(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';24;' in c :
        ligne = str(c).split(";")
        + r_agent_un(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';9;' in c :
        ligne = str(c).split(";")
        + r_has_part(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';17;' in c :
        ligne = str(c).split(";")
        + r_carac(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';87;' in c :
        ligne = str(c).split(";")
        + r_color(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';100;' in c :
        ligne = str(c).split(";")
        + r_but(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';32;' in c :
        ligne = str(c).split(";")
        + r_sentiment(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';0;' in c :
        ligne = str(c).split(";")
        + r_associated(ligne[2],ligne[3],ligne[1],ligne[5])
    elif ';130;' in c :
        ligne = str(c).split(";")
        + r_inhib(ligne[2],ligne[3],ligne[1],ligne[5])
    else:
        pass

#selection les inference a faire
if action == "r_can":
    print(cat_generique(str(id_mot_un),PAR,ID_RELATION_UN,RELATION_UN,POID_UN)&cat_action(PAR,str(id_mot_deux),ID_RELATION_DEUX,RELATION_DEUX,POID_DEUX))

print(cat_generique(str(id_mot_un),PAR,C,W,POID)&cat_generique(PAR,str(id_mot_deux),F,Y,POID))
print(cat_caracteristique(str(id_mot_un), PAR, C,W,POID) & cat_action(PAR, str(id_mot_deux),F,Y,POID))

#todo utiliser mongodb
#todo rajoute des regle