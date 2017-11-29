import ast
import os
import urllib.request
import Mot

liste_clef_requete = ['à','â','ç','è','é','ê','î','ô','ù','û']
liste_clef_reponce = ['\\xe0','\\xe2','\\xe7','\\xe8','\\xe9','\\xea','\\xee','\\xf4','\\xf9','\\xfb']
dico_requete = {}
dico_requete['à'] = '%E0'
dico_requete['â'] = '%E2'
dico_requete['ç'] = '%E7'
dico_requete['è'] = '%E8'
dico_requete['é'] = '%E9'
dico_requete['ê'] = '%EA'
dico_requete['î'] = '%EE'
dico_requete['ô'] = '%F4'
dico_requete['ù'] = '%F9'
dico_requete['û'] = '%FB'

dico_reponce = {}
dico_reponce['\\xe0'] = 'à'
dico_reponce['\\xe2'] = 'â'
dico_reponce['\\xe7'] = 'ç'
dico_reponce['\\xe8'] = 'è'
dico_reponce['\\xe9'] = 'é'
dico_reponce['\\xea'] = 'ê'
dico_reponce['\\xee'] = 'î'
dico_reponce['\\xf4'] = 'ô'
dico_reponce['\\xf9'] = 'ù'
dico_reponce['\\xfb'] = 'û'



def creer_le_mot(mot):
    page = importerRezo(mot)
    if teste_existance_du_mot(page) :
        relation_sortant = extract_relation_sortant(page)
        relation_entrant = extract_relation_entrant(page)
        noeuds = extract_relation_noeuds(page)
        type_relation = extract_relation_type_relation(page)
        objet = Mot.Mot(mot,relation_sortant,relation_entrant,noeuds,type_relation)
        return objet
    else:
        print("le mot "+mot+" n'est pas present sur jeu de mot \n peut etre acause de accent que j'ai pas envie de gere")
        return None
# va chercher le code source de la page pour le mot
def importerRezo(mot_un):
    url = 'http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel=' + mot_un + '&rel='
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    return the_page


def change_requete(mot):
    for x in liste_clef_requete:
        if x in mot:
            mot = mot.replace(x, dico_requete[x])
    return mot

def change_reponce(mot):
    for x in liste_clef_reponce:
        if x in mot:
            mot = mot.replace(x, dico_reponce[x])
    return mot


# creer le tableau des relation sortant le parametre est le code source de la page
def extract_relation_sortant(page):
    if "// les relations entrantes" in str(page):
        index_debut = str(page).index("// les relations sortante")
        index_fin = str(page).index("// les relations entrantes")
        list_relation_sortant = str(page)[index_debut:index_fin]
        list_relation_sortant = list_relation_sortant.split("\\n")
        del list_relation_sortant[0]
        del list_relation_sortant[0]
        del list_relation_sortant[-1]
        del list_relation_sortant[-1]
    else:
        index_debut = str(page).index("// les relations sortante")
        index_fin = str(page).index("// END")
        list_relation_sortant = str(page)[index_debut:index_fin]
        list_relation_sortant = list_relation_sortant.split("\\n")
        del list_relation_sortant[0]
        del list_relation_sortant[0]
        del list_relation_sortant[-1]
        del list_relation_sortant[-1]
    return list_relation_sortant

# creer le tableau des relation entrant le parametre est le code source de la page
def extract_relation_entrant(page):
    if "// les relations entrantes" in str(page):
        index_debut = str(page).index("// les relations entrantes")
        index_fin = str(page).index("// END")
        list_relation_entrant = str(page)[index_debut:index_fin]
        list_relation_entrant = list_relation_entrant.split("\\n")
        del list_relation_entrant[0]
        del list_relation_entrant[0]
        del list_relation_entrant[-1]
        del list_relation_entrant[-1]
    else:
        list_relation_entrant = []
    return list_relation_entrant

# creer le tableau des noeud le parametre est le code source de la page
def extract_relation_noeuds(page):
    index_debut = str(page).index("// les noeuds/termes")
    index_fin = str(page).index("// les types de relations")
    list_relation_noeuds = str(page)[index_debut:index_fin]
    list_relation_noeuds = list_relation_noeuds.split("\\n")
    del list_relation_noeuds[0]
    del list_relation_noeuds[0]
    del list_relation_noeuds[-1]
    del list_relation_noeuds[-1]
    numero = 0
    for ligne in list_relation_noeuds:
        list_relation_noeuds[numero] = ligne.replace("\\'","")
        numero = numero + 1
    return list_relation_noeuds

# creer le tableau des type de relation le parametre est le code source de la page
def extract_relation_type_relation(page):
    index_debut = str(page).index("// les types de relations")
    index_fin = str(page).index("// les relations sortantes")
    list_relation_type_relation = str(page)[index_debut:index_fin]
    list_relation_type_relation = list_relation_type_relation.split("\\n")
    del list_relation_type_relation[0]
    del list_relation_type_relation[0]
    del list_relation_type_relation[-1]
    del list_relation_type_relation[-1]
    numero = 0
    for ligne in list_relation_type_relation:
        list_relation_type_relation[numero] = ligne.replace("\\'", "")
        numero = numero + 1
    return list_relation_type_relation

# teste si le mot existe le parametre est le code source de la page
def teste_existance_du_mot(page):
    if '<div class="jdm-warning"><br>Le terme' in str(page):
        return False
    else:
        return True

def creer_objet_deja_ecri(mot):
        curdir = os.path.dirname(__file__)
        curdir += "/cache/" + mot + ".txt"
        if os.path.isfile(curdir):
            fichier = open(curdir,'r')
            ligne = fichier.readline()
            relation_sortant = ast.literal_eval(ligne)
            ligne = fichier.readline()
            relation_entrant = ast.literal_eval(ligne)
            ligne = fichier.readline()
            noeud = ast.literal_eval(ligne)
            ligne = fichier.readline()
            type_relation = ast.literal_eval(ligne)
            objet = Mot.Mot(mot,relation_sortant,relation_entrant,noeud,type_relation)
            return objet
        else:
            print("le mot ne possede pas de fichier")
            return None

def retourner_objet_mot(mot):
    curdir = os.path.dirname(__file__)
    curdir += "/cache/" + mot + ".txt"
    # si je possede un mot deja le mot ecrir
    if os.path.isfile(curdir):
        resultat = creer_objet_deja_ecri(mot)
    else:
        resultat = creer_le_mot(mot)
        resultat.ecrire()
    return resultat