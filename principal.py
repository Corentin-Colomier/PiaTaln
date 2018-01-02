from urllib.parse import quote
import fonction
from pyDatalog import pyDatalog

format_jdm = 'iso-8859-1'
# r_agent_un <==> r_agent-1

#prend les entres et creer les objet on fonction
mot_un = 'chat'
mot_deux = 'voler'
action = 'r_can'
fonction.mot_un = mot_un
fonction.mot_deux = mot_deux
print("recuperation de la base de donné")
id_mot_un_gene = fonction.recup_eid_avc_nom(mot_un)
id_mot_deux_gene = fonction.recup_eid_avc_nom(mot_deux)

id_mot_un= fonction.have_raffinement(id_mot_un_gene)
id_mot_deux = fonction.have_raffinement(id_mot_deux_gene)

# rela_un_positif = fonction.relation_source_positif(id_mot_un)
# rela_un_negatif = fonction.relation_source_negatif(id_mot_un)
# rela_deux_positif = fonction.relation_cible_positif(id_mot_deux)
# rela_deux_negatif = fonction.relation_cible_negatif(id_mot_un)

rela_source = fonction.relation_source(id_mot_un)
rela_cible = fonction.relation_cible(id_mot_deux)

#new_list = fonction.fusion_list(rela_un_negatif,rela_un_positif)

print("fin de recup des donné")
print("creer le fichier prolog")
#creer la base de donne prolog
pyDatalog.create_terms('ID_R,ID_S,ID_C,NUM,NOM_R,PAR,RELATION_UN,RELATION_DEUX,ID_RELATION_UN,ID_RELATION_DEUX,A,B,N,C,D,E'
                       ',F,W,Y,X,POID,POID_UN,POID_DEUX,r_isa,cat_generique,cat_action,cat_caracteristique,'
                       'cat_associe,cat_inhibition,cat_preparation,r_syn,r_holo,r_lemma,r_agent-1,r_has_part,'
                       'r_carac,r_color,r_associated,r_inhib,r_potential_confusion,c_c,a_a,b_b,'
                       'r_but,r_sentiment,r_pos,r_agent_un,test,stop')
#---
cat_preparation(NUM,ID_S,ID_C,ID_R,'r_pos',POID) <= r_pos(NUM,ID_S,ID_C,ID_R,POID)
#---
cat_generique(NUM,ID_S,ID_C,ID_R,'r_isa',POID) <= r_isa(NUM,ID_S,ID_C,ID_R,POID)
cat_generique(NUM,ID_S,ID_C,ID_R,'r_syn',POID) <= r_syn(NUM,ID_S,ID_C,ID_R,POID)
cat_generique(NUM,ID_S,ID_C,ID_R,'r_holo',POID) <= r_holo(NUM,ID_S,ID_C,ID_R,POID)
cat_generique(NUM,ID_S,ID_C,ID_R,'r_lemma',POID) <= r_lemma(NUM,ID_S,ID_C,ID_R,POID)
#---
cat_action(NUM,ID_S,ID_C,ID_R,'r_agent-1',POID) <= r_agent_un(NUM,ID_S,ID_C,ID_R,POID)
#---
cat_caracteristique(NUM,ID_S,ID_C,ID_R,'r_hase_part',POID) <= r_has_part(NUM,ID_S,ID_C,ID_R,POID)
cat_caracteristique(NUM,ID_S,ID_C,ID_R,'r_carac',POID) <= r_carac(NUM,ID_S,ID_C,ID_R,POID)
cat_caracteristique(NUM,ID_S,ID_C,ID_R,'r_color',POID) <= r_color(NUM,ID_S,ID_C,ID_R,POID)
cat_caracteristique(NUM,ID_S,ID_C,ID_R,'r_but',POID) <= r_but(NUM,ID_S,ID_C,ID_R,POID)
cat_caracteristique(NUM,ID_S,ID_C,ID_R,'r_sentiment',POID) <= r_sentiment(NUM,ID_S,ID_C,ID_R,POID)
#---
cat_associe(NUM,ID_S,ID_C,ID_R,'r_associated',POID) <= r_associated(NUM,ID_S,ID_C,ID_R,POID)
#---
cat_inhibition(NUM,ID_S,ID_C,ID_R,'r_inihib',POID) <= r_inhib(NUM,ID_S,ID_C,ID_R,POID)
#---
a_a(N,A,B,PAR,POID_UN,POID_DEUX) <= cat_generique(N,A,PAR,ID_RELATION_UN,RELATION_UN,POID_UN)&cat_action(PAR,B,ID_RELATION_DEUX,RELATION_DEUX,POID_DEUX)
#evite les exeption
+ r_isa(0,"a","b","c","d")
+ r_pos(0,"a","b","c","d")
+ r_syn(0,"a","b","c","d")
+ r_holo(0,"a","b","c","d")
+ r_lemma(0,"a","b","c","d")
+ r_agent_un(0,"a","b","c","d")
+ r_has_part(0,"a","b","c","d")
+ r_carac(0,"a","b","c","d")
+ r_color(0,"a","b","c","d")
+ r_but(0,"a","b","c","d")
+ r_sentiment(0,"a","b","c","d")
+ r_associated(0,"a","b","c","d")
+ r_inhib(0,"a","b","c","d")
#creer les fait de la base
i = rela_source.count()
for c in rela_source :
    if c['t'] == 6 :
        + r_isa(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 4 :
        + r_pos(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 5 :
        + r_syn(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 10 :
        + r_holo(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 19 :
        + r_lemma(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] ==24 :
        + r_agent_un(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 9 :
        + r_has_part(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 17 :
        + r_carac(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 87 :
        + r_color(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 100:
        + r_but(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 32 :
        + r_sentiment(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 0:
        + r_associated(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 130:
        + r_inhib(i,c['source'],c['cible'],c['rid'],c['poid'])
    else:
        pass
    i = i -1
print("fin de la creation des regles pour source")
i = rela_cible.count()
for c in rela_cible:
    if c['t'] == 6 :
        + r_isa(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 4 :
        + r_pos(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 5 :
        + r_syn(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 10 :
        + r_holo(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 19 :
        + r_lemma(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] ==24 :
        + r_agent_un(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 9 :
        + r_has_part(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 17 :
        + r_carac(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 87 :
        + r_color(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 100:
        + r_but(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 32 :
        + r_sentiment(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 0:
        + r_associated(i,c['source'],c['cible'],c['rid'],c['poid'])
    elif c['t'] == 130:
        + r_inhib(i,c['source'],c['cible'],c['rid'],c['poid'])
    else:
        pass
    i = i - 1
print("fin de la creation des regles pour la cible")
# #selection les inference a faire
print("debut du calcul")
if action == "r_can":
    x = cat_generique(NUM,id_mot_un,ID_C,ID_R,NOM_R,POID).sort()&cat_action(N,ID_C,id_mot_deux,A,B,POID_DEUX).sort()
    b = cat_action(NUM,id_mot_un,id_mot_deux,ID_R,NOM_R,POID)

print("fin if")
i = 0
if 1 == 1:
    for z in b.sort():
        i = i + 1
        taille_inference = fonction.taille_inf(z)
        if taille_inference == 0:
            fonction.afficher_taille_zero(z,i)
    for z in x.sort():
        i = i + 1
        taille_inference = fonction.taille_inf(z)
        if taille_inference == 1 :
            fonction.afficher_taille_un(z,i)

#todo rajoute des regle
