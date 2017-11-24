import ast
import os
import urllib.request
import Mot

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

# creer le tableau des relation sortant le parametre est le code source de la page
def extract_relation_sortant(page):
    index_debut = str(page).index("// les relations sortante")
    index_fin = str(page).index("// les relations entrantes")
    list_relation_sortant = str(page)[index_debut:index_fin]
    list_relation_sortant = list_relation_sortant.split("\\n")
    del list_relation_sortant[0]
    del list_relation_sortant[0]
    del list_relation_sortant[-1]
    del list_relation_sortant[-1]
    return list_relation_sortant

# creer le tableau des relation entrant le parametre est le code source de la page
def extract_relation_entrant(page):
    index_debut = str(page).index("// les relations entrantes")
    index_fin = str(page).index("// END")
    list_relation_entrant = str(page)[index_debut:index_fin]
    list_relation_entrant = list_relation_entrant.split("\\n")
    del list_relation_entrant[0]
    del list_relation_entrant[0]
    del list_relation_entrant[-1]
    del list_relation_entrant[-1]
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

    # curdir = os.path.dirname(__file__)
    # curdir += "/cache/" + motAchercher + ".txt"
    # if os.path.isfile(curdir):
    #     fichier = open(curdir,'r' , encoding ="Latin-1")
    #     contenuPage = str(fichier.readlines())
    #
    #     fichier.close()
    # else:
    #
    #     nom = "cache/"+motAchercher +".txt"
    #     fichier = open(nom,'w')
    #     fichier.write("Je croie qu j'aime marie")
    #     fichier.close()