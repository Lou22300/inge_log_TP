"""Création d'un animal un peu comme on faisait dans le TP pour l'arbre."""

class Animal():
    def __init__(self, species, age, diet, foot, name):
        self.species = species
        self.age = age
        self.diet = diet
        self.foot = foot
        self.name = name

    def __str__(self):
        return self.species +"/"+str(self.age) +"/"+self.diet +"/"+str(self.foot) +"/"+self.name


if __name__ == "__main__" :
    a = Animal("Test", "21", "diet", "foot", "name")
    # print(dir(a)) # retourne des nom de fonctions que l'on peut utiliser dessus et à la fin ses attributs.
    print(a.__getattribute__) # et ça, ça doit être pour récupérer les attributs