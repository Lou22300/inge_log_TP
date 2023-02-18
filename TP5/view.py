"""
The view creates a window that will be accessible to the user.
The Application class inherits of Tkinter class.
The controller is linking the view to the model.
"""

from tkinter import *
from tkinter import messagebox

class Application(Tk):
    """The class of the view."""

    def __init__(self, controller):
        """
        Creation of the window using Tkinter.
        We give the controller to the view.
        The attributes of the view are those that are used in the model.
        The name_list will be used to create the listbox.
        The create_widgets method permits to display many things in the window.
        """
        Tk.__init__(self)
        self.geometry("300x650")
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.name_list = self.controller.get_names_list()
        self.create_widgets()

    def create_widgets(self):
        """
        Creation of the widgets in the window.
        """
        # LABELS :
        self.label = Label(self, text="J'adore Python !")
        self.label1 = Label(self, text="")
        self.label_search = Label(self, text="Recherche")
        # BUTTONS :
        self.bouton_display = Button(self, text="Afficher", command=self.display_something)
        self.bouton_quit = Button(self, text="Quitter", command=self.quit_window)
        self.bouton_add_animal = Button(self, text="Add / Modify", command=self.add_modify_animal)
        self.bouton_delete_animal = Button(self, text="Delete", command=self.delete_animal)
        # ENTRIES :
        self.entries = {}
        self.entries_label = {}
        for att in self.attributes: # to put all the entry labels at the right place
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)
        # LISTBOX :
        self.liste = Listbox(self) # listbox is empty at first
        counter_name = 0 # position in the listebox
        for names in self.name_list : # for each animal we take the name
            counter_name += 1
            self.liste.insert(counter_name, names) # add the name at the new position
        # DISPLAY :
        self.label.pack()
        self.label1.pack()
        self.label_search.pack()
        self.liste.pack()
        self.bouton_display.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.bouton_add_animal.pack()
        self.bouton_delete_animal.pack()
        self.bouton_quit.pack()

    def display_something(self):
        """
        To display the attributes of a selected animal in the listbox. The attributes are
        displayed in the corresponding entries. The display_smthng method from the controller
        uses the display_entries_attr from the view and the get_animal_attr from the model.
        """
        self.controller.display_smthng(self.liste.get(ACTIVE))

    def display_entries_attr(self, value):
        """
        To display the attributes of an animal in the entries.
        This method is called when the display_something method is used. The controller gives in
        argument of this method the result of the get_animal_attr method from the model. So the
        value correspond to a dict containing the attributes of the selected animal.
        The first for loop is used to delete the previous text in the entries. Then we take the
        animal_attr_dict and we iterates through it and through the attributes list.
        When a key in the animal_attr_dict matches with one the the attribute list, the value
        corresponding to the animal attribute is displayed in the corresponding entry.
        """
        for values in self.entries.values():
            values.delete(0, END)
        animal_attr_dict = value
        for k, val in animal_attr_dict.items():
            for att in self.attributes:
                if k == att:
                    self.entries[att].insert(1,val)

    def add_modify_animal(self):
        """
        To add or modify an animal in the text file.
        Ajouter un animal au dico. Utilise le controller pour ajouter l'animal dans le fichier txt.
        """
        dict_animal = {}
        for key, value in self.entries.items():
            dict_animal[key] = value.get()
            value.delete(0,END)
        self.controller.add_modify_animal(dict_animal)

    def delete_animal(self):
        """
        To delete an animal from the text file.
        """
        name_to_delete = self.liste.get(ACTIVE)
        self.controller.delete_animal(name_to_delete)
        # update of the listbox : we go through all the indexes created for each added name.
        for i in range(self.liste.size()):
            if self.liste.get(i) == name_to_delete : # index = i for the name to delete.
                self.liste.delete(i) # we delete the name corresponding to the right index.
                break # names are unique so we can stop there.

    def save_pop_up(self) :
        messagebox.showinfo("adding new animal", "The new animal has been successfully added!")

    def modify_pop_up(self) :
        messagebox.showinfo("modifying the animal", "The animal has been successfully modified!")

    def delete_pop_up(self) :
        messagebox.showinfo("deleting an animal", "The animal has been successfully deleted!")

    def quit_pop_up(self) :
        messagebox.showinfo("quit", "Close app.")

    def view_window(self):
        """
        To display the window.
        """
        self.title("Ma Première App :-)")
        self.mainloop()

    def quit_window(self):
        """
        Ask to the controller to close the window and indirectly close the model.
        """
        self.controller.quit_window()

if __name__ == "__main__":
    app = Application()
    app.view_window()
