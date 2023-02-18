"""Creation of an animal with specified attributes."""

class Animal():
    """The class of an Animal object."""

    def __init__(self, species, age, diet, foot, name):
        """Creation of the animal using specified attributes."""
        self.species = species
        self.age = age
        self.diet = diet
        self.foot = foot
        self.name = name

    def __str__(self):
        """To print all the attributes of an animal."""
        return ("Name : " + self.name + "\n" +
                "Specie : " + self.species + "\n" +
                "Age : " + str(self.age) + "\n" +
                "Diet : " + self.diet + "\n" +
                "Foot : " + str(self.foot))

if __name__ == "__main__" :
    a = Animal("Test", "21", "diet", "foot", "name")
    # print(dir(a)) # retourne noms de fonctions que l'on peut utiliser sur a + ses attributs.
    print(a.__getattribute__) # et ça, ça doit être pour récupérer les attributs
