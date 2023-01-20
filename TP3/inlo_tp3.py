# encoding: utf8

"""In this program we use classes. We can create animals. Each class can have
some common attributes but can also have specific attributes. Each animal can have
children and eeach child can have a mother. We can find all the descendant of an
animal and find the parents of a child."""

class Animal() :
    """This is the class on which depend the other classes."""
    
    def __init__(self, species, foot, diet, age, mother) -> None :
        """This function creates an animal with those attributes."""
        self.species = species
        self.foot = foot
        self.age = age
        self.diet = diet
        self.children = []
        self.mother = mother
        
    def add_child(self, age) :
        """This function permits to add a child to an animal."""
        self.children.append(child=super().__init__(self.species, self.foot, self.diet, age, [], self))
        
    def show_parents(self, mother) :
        """This function permits to show all the parents/ascendants of an animal."""
        if mother == "LUCA" :
            return str(self.mother)
        else :
            return mother + super().show_parents(self.mother)
    
    def show_children(self, children) :
        """This function permits to show all the children/descendants of an animal."""
        if children == [] :
            return "No child"
        else :
            for child in children :
                return child + super().show_children(child)
    
    def __str__(self) -> str :
        """This function permits to show the attributes of an animal."""
        return (self.species + ", "
                + str(self.foot) + ", "
                + str(self.age) + ", "
                + self.diet + ", "
                + str(self.children))
    
    def __eq__(self, __o: object) -> bool:
        """This function permits to verify if two objects corresponds to the same animal."""
        return (self.species == __o.species and
                self.foot == __o.foot and
                self.age == __o.age and
                self.diet == __o.diet and
                self.children == __o.children and
                self.mother == __o.mother)
  
        
class Human(Animal) :
    """This class inherits of some attributes of Animal() and have one spécific attributes."""
    
    def __init__(self, age, mother, name) -> None :
        """This function creates a human with those attributes."""
        super().__init__("Human", 2, "Omnivore", age, mother)
        self.name = name

    def add_child(self, age, name) :
        """This function permits to add a child to a human."""
        self.children.append(child=super().__init__(self.species, self.foot, self.diet, age, [], self, name))
        
    def show_parents(self, mother) :
        """This function permits to show all the parents/ascendants of an animal."""
        super().show_parents
        
    def show_children(self, children) :
        """This function permits to show all the children/descendants of an animal."""
        super().show_children

    def __str__(self) -> str:
        """This function permits to show the attributes of a human."""
        return super().__str__() + ", " + self.name 
    
    def __eq__(self, __o: object) -> bool:
        """This function permits to verify if two objects corresponds to the same human."""
        return super().__eq__(__o) and self.name == __o.name 

   
class Snake(Animal) :
    """This class inherits of some attributes of Animal() and have one spécific attributes."""
    
    def __init__(self, age, mother, length) -> None : 
        """This function create a snake with those attributes."""
        super().__init__("Snake", 0, "Carnivore", age, mother)
        self.length = length

    def add_child(self, age, length) :
        """This function permits to add a child to a snake."""
        self.children.append(child=super().__init__(self.species, self.foot, self.diet, age, [], self, length))
        
    def show_parents(self, mother) :
        """This function permits to show all the parents/ascendants of an animal."""
        super().show_parents

    def show_children(self, children) :
        """This function permits to show all the children/descendants of an animal."""
        super().show_children

    def __str__(self) -> str :
        """This function permits to show the attributes of a snake."""
        return super().__str__() + ", " + self.length
    
    def __eq__(self, __o: object) -> bool :
        """This function permits to verify if two objects corresponds to the same snake."""
        return super().__eq__(__o) and self.length == __o.length 


class Dog(Animal) :
    """This class inherits of some attributes of Animal() and have one spécific attributes."""
    
    def __init__(self, age, mother, race) -> None :
        """This function creates a dog with those attributes."""
        super().__init__("Dog", 4, "Carnivore", age, mother)
        self.race = race
        
    def add_child(self, age) :
        """This function permits to add a child to a dog."""
        self.children.append(child=super().__init__(self.species, self.foot, self.diet, age, [], self, self.race))
        
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
    human1 = Human(70, "LUCA", "Jeanne")
    print(human1)
    human2 = Human(human1.add_child(50, "Jeannette"))
    print(human2)
    # human3 = human1.add_child(45, "Jean")
    # human4 = human2.add_child(30, "Jeanne-Marie")
    # human4 = human2.add_child(25, "Jeannie")
    

