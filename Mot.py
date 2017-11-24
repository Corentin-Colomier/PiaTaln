# relation_sortant = extract_relation_sortant()
# relation_entrant = extract_relation_entrant()
# noeuds = extract_relation_noeuds()
# type_relation = extract_relation_type_relation()
import os
import ast


class Mot:
    def __init__(self,word,out,iin,node,kind):
        self.mot = word
        self.relation_sortant = out
        self.relation_entrant = iin
        self.noeuds = node
        self.type_relation = kind

    def toString(self):
        print("Je suis le mot :\n" + str(self.mot) + "\nmes relation sortant sont :\n" + str(self.relation_sortant) + "\nmes relation "
              + "entrant sont :\n" + str(self.relation_entrant) + "\nles noeuds sont :\n" + str(self.noeuds) + "\nles type de relation :\n"
              + str(self.type_relation))

    def ecrire(self):
        curdir = os.path.dirname(__file__)
        curdir += "/cache/" + self.mot + ".txt"
        if os.path.isfile(curdir):
            print("le mot possede deja un fichier")
        else:
            fichier = open(curdir,'w')
            fichier.write(str(self.relation_sortant))
            fichier.write("\n")
            fichier.write(str(self.relation_entrant))
            fichier.write("\n")
            fichier.write(str(self.noeuds))
            fichier.write("\n")
            fichier.write(str(self.type_relation))

