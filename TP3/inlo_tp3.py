# encoding: utf8

"""In this program we use classes. We can create animals. Each class can have some common
attributes but can also have specific attributes. Each animal can have children and each
child can have a mother. We can find all the descendant of an animal and find the parents
of a child."""

class Animal() :
    """This is the class on which depend the other classes."""

    def __init__(self, name, species, foot, diet, age, mother) -> None :
        """This function creates an animal with those attributes. Names must be given so that
        we can find the children and the parents of an animal. The mother of an animal of an
        animal create as first of its family must be specified."""
        self.name: str = name
        self.species: str = species
        self.foot: int = foot
        self.age: int = age
        self.diet: str = diet
        self.child_id: list = [] # contains not understandable id
        self.children: list = [] # contains names
        self.mother: str = mother # mother's name only
        self.parents: list = [mother] # all the parents names starting with LUCA

    def add_child(self, name, age) :
        """This function permits to add a child to an animal.
        The child is part of the same class than the mother.
        Only a few attributes are changed."""
        # creates a new specimen :
        new_child = self.__class__(name, self.species, self.foot, self.diet, age, self.name)
        # take the parents/anceestors of the parent/mother :
        new_parents = self.parents
        # And add them to the child's ancestors list :
        for element in new_parents :
            new_child.parents.append(element)
        # For the mother, two lists are modified by adding
        # id and name of the child at the same indexes
        self.children.append(new_child.name)
        self.child_id.append(new_child)
        return new_child

    def show_parents(self) :
        """This function permits to show all the parents/ancestors of an animal.
        Parents are added in a list in the function add_child.
        Return a sentence of the ancestors."""
        ancestors = ""
        # If there is only one parent : Only show this one
        if len(self.parents) == 1 :
            ancestors = self.parents[0] + " is the only parent of " + self.name + "."
        # If there is more than one parent :
        else :
            self.parents.reverse() # to take the oldest parent first
            # creates a sentence returning the names of the ancestors :
            for i in range(len(self.parents)-1) :
                ancestors = ancestors + self.parents[i] + ", "
            # adding the last one after the 'and' and finish the sentence :
            ancestors = (ancestors + "and "
                         + self.parents[-1]
                         + " are the ancestors of "
                         + self.name + ".")
        return ancestors

    def search_all_children(self) :
        """This function permits to find all the children/descendants of an animal in a list.
        The list will contains other lists of the children's children's names."""
        if not self.children : # if self.children == []
            total_child_name_list = ["No child yet for " + self.name]
        else :
            total_child_name_list = [] # list that will be returned
            # for every index in the list of not understandable child id :
            for ind,items in enumerate(self.child_id):
                # take the child name in the other list (same index)
                child_name = self.children[ind]
                # put it to the returned list
                total_child_name_list.append(child_name)
                # recursivity is used to find every child's children
                total_child_name_list.append(__class__.search_all_children(items))
        return total_child_name_list

    def show_children(self) :
        """This function is used to print all the descendants of an animal.
        The function can be called in the classes that inherited of Animal.
        The function call the search_all_children_function."""
        first_step = Animal.search_all_children(self)
        return "\nThe descendants of " + self.name + " are " + str(first_step) + "\n"

    def __str__(self) -> str :
        """This function permits to show the attributes of an animal."""
        count_children = len(self.children)
        return (self.name + ", "
                + self.species + ", "
                + str(self.foot) + " feet, "
                + str(self.age) + " year(s), mother is "
                + self.mother + ", "
                + self.diet + ", and have "
                + str(count_children) + " children : "
                + str(self.children))

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
        """This function creates a human with those attributes.
        There are no specific attributes here."""
        super().__init__(name, "Human", 2, "Omnivore", age, mother)

    def add_child(self, name, age) :
        """This function permits to add a child to a human. It is the same that for
        the Animal() class, but the new specimen is part of the Human class instead
        of Animal class."""
        new_child = self.__class__(name, age, self.name)
        # take the parents of the parents :
        new_parents = self.parents
        for element in new_parents :
            new_child.parents.append(element)
        # two lists are created with id and name respectively at the same indexes
        self.children.append(new_child.name)
        self.child_id.append(new_child)
        return new_child # only the name is returned

    def __str__(self) -> str:
        """This function permits to show the attributes of a human.
        Same that for the Animal() class, with adding a point."""
        return super().__str__() + "."

class Snake(Animal) :
    """This class inherits of some attributes of Animal() and have one
    spécific attributes."""

    def __init__(self, name, age, mother, length) -> None :
        """This function create a snake with those attributes.
        Same that for the Animal() class, with adding the length."""
        super().__init__(name, "Snake", 0, "Carnivore", age, mother)
        self.length: float = length

    def add_child(self, name, age, length) :
        """This function permits to add a child to a snake.
        Different from the Animal() class function because of length."""
        new_child = self.__class__(name, age, self.name, length)
        # take the parents of the parents :
        new_parents = self.parents
        for element in new_parents :
            new_child.parents.append(element)
        self.children.append(new_child.name)
        self.child_id.append(new_child)
        return new_child

    def __str__(self) -> str :
        """This function permits to show the attributes of a snake.
        Same that for the Animal() class with adding the length."""
        return super().__str__() + ", " + str(self.length) + "cm."

    def __eq__(self, __o: object) -> bool :
        """This function permits to verify if two objects corresponds to the same snake.
        Same that for the Animal() class with adding the length."""
        return super().__eq__(__o) and self.length == __o.length

class Dog(Animal) :
    """This class inherits of some attributes of Animal() and have
    one spécific attributes."""

    def __init__(self, name, age, mother, race) -> None :
        """This function creates a dog with those attributes."""
        super().__init__(name, "Dog", 4, "Carnivore", age, mother)
        self.race: str = race

    def add_child(self, name, age) :
        """This function permits to add a child to a dog.
        Different from the Animal() class function because of race."""
        new_child = self.__class__(name, age, self.name, self.race)
        # take the parents of the parents :
        new_parents = self.parents
        for element in new_parents :
            new_child.parents.append(element)
        self.children.append(new_child.name)
        self.child_id.append(new_child)
        return new_child

    def __str__(self) -> str :
        """This function permits to show the attributes of a dog.
        Same that for the Animal() class with adding the length."""
        return super().__str__() + ", " + self.race

    def __eq__(self, __o: object) -> bool :
        """This function permits to verify if two objects corresponds to the same dog.
        Same that for the Animal() class with adding the length."""
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

    human1 = Human("Jeanne", 70, "LUCA")
    human2 = human1.add_child("Jeannette", 50)
    human3 = human1.add_child("Jean", 45)
    human4 = human2.add_child("Jeanne-Marie", 30)
    human5 = human2.add_child("Jeannie", 25)

    snake1 = Snake("Sulivan", 40, "LUCA", 500)
    snake2 = snake1.add_child("Sully", 35, 400)
    snake3 = snake1.add_child("Snow", 33, 389.5)
    snake4 = snake1.add_child("Sam", 31, 366)
    snake5 = snake2.add_child("Sammy", 25, 400)
    snake6 = snake2.add_child("Samantha", 24, 400.5)
    snake7 = snake2.add_child("Siri", 23, 377)
    snake8 = snake3.add_child("Shella", 25, 153)
    snake9 = snake8.add_child("Shell", 20, 113)
    snake10 = snake8.add_child("Shanny", 18, 90.5)

    dog1 = Dog("Damian", 20, "LUCA", "Husky")
    dog2 = Dog("Ronnie", 19, "LUCA", "Doberman")
    dog3 = dog1.add_child("Dobby", 14)
    dog4 = dog1.add_child("Darren", 8)
    dog5 = dog1.add_child("Dixie", 4)
    dog6 = dog2.add_child("Ron", 16)
    dog7 = dog2.add_child("Roxie", 9)
    dog8 = dog2.add_child("Rex", 5)

    print("---------------------------------------------------\n\n", animal1)
    print(animal1.show_children())
    print(animal9.show_parents(), "\n")

    print("---------------------------------------------------\n\n", human1)
    print(human1.show_children())
    print(human5.show_parents(), "\n")

    print("---------------------------------------------------\n\n", snake1)
    print(snake1.show_children())
    print(snake10.show_parents(), "\n")

    print("---------------------------------------------------\n\n", dog1)
    print("\n", dog2)
    print(dog1.show_children())
    print(dog8.show_parents(), "\n")
