# encoding: utf8

"""In this program we use classes. We can create animals. Each class can have
some common attributes but can also have specific attributes. Each animal can have
children and eeach child can have a mother. We can find all the descendant of an
animal and find the parents of a child."""

class Animal() :
    """This is the class on which depend the other classes."""
    
    def __init__(self, name, species, foot, diet, age, mother) -> None :
        """This function creates an animal with those attributes."""
        self.name = name
        self.species = species
        self.foot = foot
        self.age = age
        self.diet = diet
        self.children = []
        self.mother = mother
        
    def add_child(self, name, age) : # Ajoute bien les enfants de la classe Animal() -- pas testé pour les autres classes
        """This function permits to add a child to an animal."""
        new_child = self.__class__(name, self.species, self.foot, self.diet, age, self.name) # type(self) = self.__class__
        self.children.append(new_child.name)
        return new_child
        
    def show_parents(self, mother) : # pas encore testée
        """This function permits to show all the parents/ascendants of an animal."""
        if mother == "LUCA" :
            return str(self.mother)
        else :
            return mother + super().show_parents(self.mother)
    
    def show_children(self, children) : # 
        """This function permits to show all the children/descendants of an animal."""
        if self.children == [] :
            return "No child"
        else :
            total_descendant = []
            child_list = []
            for child in self.children :
                total_descendant.append(child)
                child_list.append(Animal.show_children(child))
                total_descendant.append(child_list)
            return total_descendant
    
    def __str__(self) -> str :
        count_children = len(self.children)
        """This function permits to show the attributes of an animal."""
        return (self.name + ", "
                + self.species + ", "
                + str(self.foot) + " feet, "
                + str(self.age) + " year(s), mother is "
                + self.mother + ", "
                + self.diet + ", and have "
                + str(count_children) + " children")
    
    def __eq__(self, __o: object) -> bool:
        """This function permits to verify if two objects corresponds to the same animal."""
        return (self.species == __o.species and
                self.foot == __o.foot and
                self.age == __o.age and
                self.diet == __o.diet and
                self.children == __o.children and
                self.mother == __o.mother and
                self.name == __o.name)
  
   
class Human(Animal) :
    """This class inherits of some attributes of Animal() and have one spécific attributes."""
    
    def __init__(self, name, age, mother) -> None :
        """This function creates a human with those attributes."""
        super().__init__(name, "Human", 2, "Omnivore", age, mother)
        self.name = name

    def add_child(self, name, age) :
        """This function permits to add a child to a human."""
        new_child = self.__class__(name, age, self.name)
        self.children.append(new_child.name)
        return new_child
        
    def show_parents(self, mother) :
        """This function permits to show all the parents/ascendants of an animal."""
        super().show_parents
        
    def show_children(self, children) :
        """This function permits to show all the children/descendants of an animal."""
        super().show_children

    def __str__(self) -> str:
        """This function permits to show the attributes of a human."""
        return super().__str__() + "."
    
    def __eq__(self, __o: object) -> bool:
        """This function permits to verify if two objects corresponds to the same human."""
        return super().__eq__(__o)

   
class Snake(Animal) :
    """This class inherits of some attributes of Animal() and have one spécific attributes."""
    
    def __init__(self, name, age, mother, length) -> None : 
        """This function create a snake with those attributes."""
        super().__init__(name, "Snake", 0, "Carnivore", age, mother)
        self.length = length

    def add_child(self, name, age, length) :
        """This function permits to add a child to a snake."""
        new_child = self.__class__(name, age, self.name, length)
        self.children.append(new_child.name)
        return new_child
        
    def show_parents(self, mother) :
        """This function permits to show all the parents/ascendants of an animal."""
        super().show_parents

    def show_children(self, children) :
        """This function permits to show all the children/descendants of an animal."""
        super().show_children

    def __str__(self) -> str :
        """This function permits to show the attributes of a snake."""
        return super().__str__() + ", " + str(self.length) + "cm."
    
    def __eq__(self, __o: object) -> bool :
        """This function permits to verify if two objects corresponds to the same snake."""
        return super().__eq__(__o) and self.length == __o.length 


class Dog(Animal) :
    """This class inherits of some attributes of Animal() and have one spécific attributes."""
    
    def __init__(self, name, age, mother, race) -> None :
        """This function creates a dog with those attributes."""
        super().__init__(name, "Dog", 4, "Carnivore", age, mother)
        self.race = race
        
    def add_child(self, name, age) :
        """This function permits to add a child to a dog."""
        new_child = self.__class__(name, age, self.name, self.race)
        self.children.append(new_child.name)
        return new_child
        
    def show_parents(self, mother) :
        """This function permits to show all the parents/ascendants of an animal."""
        super().show_parents
        
    def show_children(self, children) :
        """This function permits to show all the children/descendants of an animal."""
        super().show_children

    def __str__(self) -> str :
        """This function permits to show the attributes of a dog."""
        return super().__str__() + ", " + self.race
    
    def __eq__(self, __o: object) -> bool :
        """This function permits to verify if two objects corresponds to the same dog."""
        return super().__eq__(__o) and self.race == __o.race

if __name__ == "__main__" :

    animal1 = Animal("Bobby", "Rat", 4, "Omnivore", 7, "LUCA")
    animal2 = animal1.add_child("Bob", 5)
    animal3 = animal1.add_child("Benny", 4)
    animal4 = animal2.add_child("Brenda", 4)
    animal5 = animal2.add_child("Branny", 3)
    animal6 = animal2.add_child("Boo", 2)
    animal7 = animal3.add_child("Baxter", 3)
    animal8 = animal3.add_child("Betty", 2)
    animal9 = animal3.add_child("Bibbi", 1)
    print("\n", animal1)
    print(animal1.children)
    print("\n", animal2)
    print(animal2.children)
    print("\n", animal3)
    print(animal3.children)

    # human1 = Human("Jeanne", 70, "LUCA")
    # human2 = human1.add_child("Jeannette", 50)
    # human3 = human1.add_child("Jean", 45)
    # human4 = human2.add_child("Jeanne-Marie", 30)
    # human5 = human2.add_child("Jeannie", 25)
    # print("\n", human1)
    # print(human2)
    # print(human3)
    # print(human4)
    # print(human5)
    
    # snake1 = Snake("Sulivan", 40, "LUCA", 500)
    # snake2 = snake1.add_child("Sully", 35, 400)
    # snake3 = snake1.add_child("Snow", 33, 389)
    # snake4 = snake1.add_child("Sam", 31, 366)
    # snake5 = snake2.add_child("Sammy", 25, 400)
    # snake6 = snake2.add_child("Samantha", 24, 400)
    # snake7 = snake2.add_child("Siri", 23, 400)
    # snake8 = snake3.add_child("Shella", 25, 400)
    # snake9 = snake8.add_child("Shell", 20, 400)
    # snake10 = snake8.add_child("Shanny", 18, 400)
    # print("\n", snake1)
    # print(snake1.children)
    # print("\n", snake2)
    # print(snake2.children)
    # print("\n", snake8)
    # print(snake8.children)

    # dog1 = Dog("Damian", 20, "LUCA", "Husky")
    # dog2 = Dog("Ronnie", 19, "LUCA", "Doberman")
    # dog3 = dog1.add_child("Dobby", 14)
    # dog4 = dog1.add_child("Darren", 8)
    # dog5 = dog1.add_child("Dixie", 4)
    # dog6 = dog2.add_child("Ron", 16)
    # dog7 = dog2.add_child("Roxie", 9)
    # dog8 = dog2.add_child("Rex", 5)
    # print("\n ", dog1)
    # print(dog1.children)
    # print("\n ", dog2)
    # print(dog2.children)

    print(animal1.show_children)