from pymongo import MongoClient
import pymongo

mot_un = ""
mot_deux = ""

client = MongoClient("localhost",27017)
db = client['taln']
collection_eid = db['eid']
collection_rid = db['rid']

#on envoi le eid on reçoit le nom
def recup_nom_avc_eid(eid):
    dd = collection_eid.find_one({"eid":eid})
    return dd['nom']

#on fusion les valeurs en fonctions de la
#valeur absolut
def fusion_list(list_un,list_deux):
    iterator_un = int(0)
    iterator_deux = int(0)
    list_resultat = []
    while iterator_un != list_un.count() and iterator_deux != list_deux.count():
        # print(iterator_un)
        # print(iterator_deux)
        # print(list_deux.count())
        if iterator_un == list_un.count() and iterator_deux != list_deux.count():
            list_resultat.append(list_deux[iterator_deux])
            iterator_deux = iterator_deux + 1
        elif iterator_deux == list_deux.count() and iterator_un != list_un.count():
            list_resultat.append(list_un[iterator_un])
            iterator_un = iterator_un + 1
        elif abs(list_deux[iterator_deux]['poid']) < abs(list_un[iterator_un]['poid']):
            list_resultat.append(list_un[iterator_un])
            iterator_deux = iterator_deux + 1
        elif abs(list_un[iterator_un]['poid'])< abs(list_deux[iterator_deux]['poid']):
            list_resultat.append(list_deux[iterator_deux])
            iterator_deux = iterator_deux + 1
        else:
            print("je doit pas passer par la ité 1 : " + str(iterator_un))
            print("et iterator 2 : " + str(iterator_deux))
    return list_resultat

#on envoie le nom on reçoi l'eif
def recup_eid_avc_nom(nom):
    dd = collection_eid.find_one({"nom":nom})
    return dd['eid']

def relation_source_positif(eid):
    cursor = collection_rid.find({"source":eid,"poid":{"$gt":0}}).sort("poid",pymongo.DESCENDING)
    return cursor

def relation_source(eid):
    cursor = collection_rid.find({"source":eid}).sort("poidAbs",pymongo.ASCENDING)
    return cursor
#0 direct 1 pas par 1
def taille_inf(z):
    if len(z)==4:
        return 0
    elif len(z) == 9:
        return 1
def afficher_taille_un(z,i):
    id_mot_passerel = z[1]
    type_r_un = z[3]
    type_r_deux = z[7]
    poid_r_un = z[4]
    poid_r_deux = z[8]
    mot_passerel = recup_nom_avc_eid(id_mot_passerel)
    print("iteration n " + str(i) + " : \n\t"+
          str(mot_un) + " -- "+ str(type_r_un)+"/"+str(poid_r_un)+ " --> " + str(mot_passerel) +
          " -- "+ str(type_r_deux)+"/"+str(poid_r_deux) + " --> " + str(mot_deux))
def afficher_taille_zero(z,i):
    type_r = z[2]
    poid_r = z[3]
    print("iteration n " + str(i) + " : \n\t"+
          str(mot_un) + " -- "+ str(type_r)+"/"+str(poid_r) + " --> " + str(mot_deux))

def relation_cible(eid):
    cursor = collection_rid.find({"cible":eid}).sort("poidAbs",pymongo.ASCENDING)
    return cursor


def relation_source_negatif(eid):
    cursor = collection_rid.find({"source":eid,"poid":{"$lt":0}}).sort("poid",pymongo.ASCENDING)
    return cursor

def relation_cible_positif(eid):
    cursor = collection_rid.find({"cible":eid,"poid":{"$gt":0}}).sort("poid",pymongo.DESCENDING)
    return cursor

def relation_cible_negatif(eid):
    cursor = collection_rid.find({"cible":eid,"poid":{"$lt":0}}).sort("poid",pymongo.ASCENDING)
    return cursor

def have_raffinement(eid):
    id = 0
    cursor = collection_rid.find({"source":eid,"t":1})
    if cursor.count() == 0 or cursor.count() == 1:
        id = eid
    else:
        id = liste_raf(cursor)
        if id == -1:
            id = eid
    return id

def liste_raf(cursor):
    i = 0
    liste_tuple = []
    print("les raffinement possible sont :")
    for ligne in cursor:
        id_ligne = ligne['cible']
        nom = get_domaine(id_ligne)
        tuple = (id_ligne,nom)
        print(str(tuple)+" "+str(i))
        i = 1 + i
        liste_tuple.append(tuple)
    select = input("quelle raffinement voulez vous -1 pour aucune")
    select = int(select)
    if select == -1:
        return -1
    else:
        return liste_tuple[select][0]

def get_domaine(eid):
    cursor = collection_eid.find_one({'eid':eid})
    nom = cursor['nom']
    nom = nom.split('>')[1]
    nom = int(nom)
    cursor = collection_eid.find_one({'eid': nom})
    return cursor['nom']
#recupere la liste des rafinement sementique
def extract_raffinement(object_mot):
    liste_raffinement = []
    for x in object_mot.noeuds:
        if str(object_mot.mot) + ">" in x:
            liste_raffinement.append(x)
    return liste_raffinement

#fonction qui demand quelle rafinement prendre
def propose_choix(list_raf):
    i = 0
    list_tuple = []
    print('liste des raffinement possible')
    for x in list_raf:
        y = x.split(";")
        tuple = (y[1],y[5],i)
        list_tuple.append(tuple)
        i=i+1
        print(tuple)
    raf = len(list_raf)
    raf = input("entre le numero (3iem valeur) du raffinement que vous voulez"
          " ou entre -1 peut import : ")
    raf = int(raf)
    if raf != -1 and raf >= len(list_raf):
        print("serieux ???")
    if raf == -1:
        return -1
    else:
        return list_tuple[raf][0]

def recup_id_sans_choix(object_mot):
    id_mot = -1
    for x in object_mot.noeuds:
        if ";'" + str(object_mot.mot) + "';" in x:
            ligne = str(x).split(";")
            id_mot = ligne[1]
    return id_mot

def select_id(object_mot):
    liste_raffinement = extract_raffinement(object_mot)
    if liste_raffinement:
        id_mot = propose_choix(liste_raffinement)
        if id_mot == -1:
            id_mot = recup_id_sans_choix(object_mot)
    else:
        id_mot = recup_id_sans_choix(object_mot)
    return id_mot