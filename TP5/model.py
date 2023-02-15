"""Model auquel le controller a accès et qui utilise la classe animal"""

from Animal import Animal

class Model():
    def __init__(self, filename):
        """Création du modèle"""
        self.filename = filename
        self.file=open(self.filename, "r+")
        self.dico_animaux = {}

    def read_file(self):
        """Lecture du fichier et récupération des animaux dedans.
        Pour ça on utilise la classe Animal du fichier Animal.py"""
        for line in self.file:
            line = line.strip() # enlever le \n à la fin des lignes
            tab = line.split(",") # couper la ligne en fonction des attributs donnés dans le fichier txt
            a = Animal(tab[0],tab[1],tab[2],tab[3],tab[4])
            self.dico_animaux[a.name] = a # clé = nom de l'animal, valeur = liste d'attribut de l'animal

    def save(self, dict_animal):
        """Ecrire les modification dans le fichier text (nouvel animal ajouter avec les entries)"""
        self.file.write("\n"+dict_animal["species"]+","+dict_animal["age"]+","+dict_animal["diet"]+","+dict_animal["foot"]+","+dict_animal["name"])

    def close(self):
        """Fermer le fichier txt"""
        self.file.close()

    def get_attributes(self):
        """Cette fonction était pas finie quand on a fini le cours, il y avait encore des erreurs.
        Mais le but est de récupérer tous les attributs d'un animal en faisant une recherche avec son nom. Returning a list."""
        attr = []
        # get first key of the dict no mater what is it
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr

    def creates_namelist(self):
        """Cette fonction est utilisée pour la listebox."""
        # on récupère les noms des animaux en clés du dico_animaux :
        name_list = []
        for names in self.dico_animaux :
            name_list.append(names)
        name_list.sort()
        return name_list

if __name__ == "__main__" :
    model = Model("a.txt")
    model.read_file()
    model.close()
    