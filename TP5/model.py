"""
The model premits to create and handle many data that will not be directly
accessible to the user. The controller is linking the view to the model.
It uses the Animal class imported from animal.py.
"""

from animal import Animal

class Model():
    """Class of the model. Uses the Animal class."""

    def __init__(self, filename):
        """
        Creation of the model. We give the file containing the animals.
        The file is opened and we initialize the dict that will contain
        the animal's attributes.
        """
        self.filename = filename
        self.file=open(self.filename, "r+", encoding = "UTF-8")
        self.dico_animaux = {}

    def read_file(self):
        """
        Reading the file and getting the attributes of the animals using the Animal class.
        The strip() function is used to cut the return to line and the split() function to
        separe all the attributes on one line.
        Each name will be a key in the dict and the value will be the list of its attributes.
        """
        for line in self.file:
            if line != "\n" :
                line = line.strip()
                tab = line.split(",")
                all_animal_attr = Animal(tab[0],tab[1],tab[2],tab[3],tab[4])
                self.dico_animaux[all_animal_attr.name] = all_animal_attr

    def creates_namelist(self):
        """
        To create the listbox containing the names of all the animals in the text file.
        The names are sorted alphabetically.
        """
        # on récupère les noms des animaux en clés du dico_animaux :
        name_list = []
        for names in self.dico_animaux :
            name_list.append(names)
        name_list.sort()
        return name_list

    def get_attributes(self):
        """
        This function is used to get all the attributes of an animal while searching with the name.
        It is returning a list of the attributes that an animal can have such as "name" or "diet"...
        """
        attr = []
        # get first key of the dict no mater what it is
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr

    def get_animal_attr(self, name):
        """
        To get a dictionnary containing the attributes corresponding to the selected animal
        in the listbox. The keys will be the possible attributes (ex : "diet") and the values
        will be specific to the selected animal (ex : "Carnivore").
        We iterate with the build-in dir() method through all the attributes of the chosen object.
        Then we have to ignore the attributes which starts with '_', and we only get the attributes
        that we have created.
        """
        dict_animal = {}
        animal = self.dico_animaux.get(name) # get the object 'animal' the user wants
        # Iterate through the attributes of the class Animal
        for attribute in dir(animal):
            # Ignore attributes that start with underscore (_) and are not defined in the class
            if not attribute.startswith("_"):
                # Get the value of the attribute
                value = getattr(animal, attribute)
                # Add the attribute and its value to the dictionary
                dict_animal[attribute] = value
        return dict_animal

    def save_modify_animal(self, dict_animal):
        """
        To write the modifications in the text file.
        If the name of the animal doesn't already exist in the file, a new animal is added.
        If the name already exists in the file, the modifications are saved to the line
        corresponding to the animal with the same name. If nothing have been written in some
        entries (exept the name), the previous attribute is kept.
        """
        # CHECK IF THE ANIMAL ALREADY EXIST :
        does_name_exist = False
        line_counter = 0
        # for each name in the text file :
        for names in self.dico_animaux :
            line_counter += 1
            # if the name in the entry matches one of the name in the file :
            if dict_animal["name"] == names :
                does_name_exist = True
                break
        # IF THE ANIMAL DOESN'T ALREADY EXIST -> ADDED TO THE FILE :
        if does_name_exist is False :
            self.save_new_animal(dict_animal)
            return 0
        # IF THE ANIMAL ALREADY EXISTS -> MODIFIED IN THE FILE :
        else :
            self.modify_animal(dict_animal)
            return 1

    def save_new_animal(self, dict_animal) :
        """
        If the animal to save doesn't already exist in the text file, it is added
        in a new line with all the attributes in the entries.
        """
        self.file.write("\n" + dict_animal["species"] + "," +
                            dict_animal["age"] + "," +
                            dict_animal["diet"] + "," +
                            dict_animal["foot"] + "," +
                            dict_animal["name"])

    def modify_animal(self, dict_animal) :
        """
        If the animal to save already exists in the text file, it is modified.
        The line that already exists is deleted and a new line is added.
        If some entries are empty, the previous attribute is kept.
        """
        if dict_animal["species"] == "" :
            dict_animal["species"] = self.dico_animaux[dict_animal["name"]].species
        if dict_animal["age"] == "" :
            dict_animal["age"] = self.dico_animaux[dict_animal["name"]].age
        if dict_animal["diet"] == "" :
            dict_animal["diet"] = self.dico_animaux[dict_animal["name"]].diet
        if dict_animal["foot"] == "" :
            dict_animal["foot"] = self.dico_animaux[dict_animal["name"]].foot
        self.delete_an_animal(dict_animal["name"])
        self.file.write("\n" + dict_animal["species"] + "," +
                        dict_animal["age"] + "," +
                        dict_animal["diet"] + "," +
                        dict_animal["foot"] + "," +
                        dict_animal["name"])

    def delete_an_animal(self, name_to_delete) :
        """
        To save the modifications in the text file when an animal is deleted.
        """
        self.file.seek(0) # Cursor back to the start of the text file.
        lines = self.file.readlines()  # list of all the line of the file.
        self.file.seek(0)  # Cursor back to the start of the text file.
        self.file.truncate() # to erase the content of the all file.
        for line in lines: # take all the lines and compare the name to the name_to_delete.
            line_list = line.strip().split(',')
            if line_list[-1] != name_to_delete: # if it is not the line to delete
                self.file.write(line)  # the line is written in the file.

    def close(self):
        """
        To close the text file.
        """
        self.file.close()

if __name__ == "__main__" :
    model = Model("a.txt")
    model.read_file()
    model.close()
