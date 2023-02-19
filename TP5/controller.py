"""
The controller is used to make the link between the view and the model.
The classes from the view (Application) and the model (Model) are imported here.
"""

from view import Application
from model import Model

class Controller() :
    """Class of the controller"""

    def __init__(self):
        """
        We give to the controller the model and the view.
        The read_file method returns a dict containing all the animals
        present in the text file.
        The view_window method permits to display the window.
        """
        self.model = Model("a.txt")
        self.model.read_file()
        self.view = Application(self)
        self.view.view_window()

    def get_names_list(self) :
        """
        To create a listbox containing all the animal names present in the text file.
        The creates_namelist method from the model takes the name and sort them.
        """
        return self.model.creates_namelist()

    def get_model_entries(self):
        """
        Permits to get all the attributes of an animal such as "name" or "diet"
        using the get_attributes method from the model. They are used to put
        a label upon the corresponding entries.
        """
        return self.model.get_attributes()

    def display_smthng(self, value):
        """
        To change some things in the view taking informations from the model.
        The get_animal_attr method of the model returns a dictionnary
        of the attributes that corresponds to a chosen animal.
        The display_entries_attr method of the view display the
        attributes of the given animal in the corresponding entries.
        """
        self.view.display_entries_attr(self.model.get_animal_attr(value))

    def add_modify_animal(self, dict_animal):
        """
        To add a new animal in the text file.
        The save_new_animal method from the model takes the attributes
        from the entries and add an animal to the text file.
        If the name of the animal already is in the text file, it just
        modify the attributes if they are changed.
        It will display different opo-ups on the view depending on the case.
        For that, it uses the display_pop_up method of the view.
        """
        if dict_animal["name"] != "" :
            choice = self.model.save_modify_animal(dict_animal)
            if choice == 0 :
                self.view.display_pop_up(1)
                self.view.add_animal_to_listbox(dict_animal["name"])
            if choice == 1 :
                self.view.display_pop_up(2)
        else :
            self.view.display_pop_up(3)

    def delete_animal(self, name_to_delete):
        """
        Permits do delete a selected animal from the text file.
        """
        self.model.delete_an_animal(name_to_delete)

    def save_the_file(self) :
        """
        To save all the modifications. It uses the dico_animaux from the model.
        The file is errased and rewrited with all the animal that are in the dictionnary.
        """
        self.model.rewrite_file()

    def quit_window(self):
        """To close de window displayed by the view and the text file opened by the model."""
        self.save_the_file()
        self.view.quit_pop_up()
        self.model.close()
        self.view.destroy()

if __name__ == "__main__" :
    C = Controller()
