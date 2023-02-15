"""Vue à laquelle le controller a accès"""

from tkinter import *

class Application(Tk):
    """Cette classe hérite de tkinter"""
    def __init__(self, controller):
        """Création de la vue = de la fenêtre. On récupère des informations du model depuis le controller."""
        Tk.__init__(self)
        self.controller = controller
        self.attributes = self.controller.get_model_entries() # la vue est reliée au model grâce à ça
        self.name_list = self.controller.get_names_list() # Noms de tous les animaux
        self.creer_widgets() # création des widgets présents dans la fenêtre

    def creer_widgets(self):
        """Création des widgets présents dans la fenêtre"""
        # LABELS :
        self.label = Label(self, text="J'adore Python !")
        self.label1 = Label(self, text="")
        self.label_search = Label(self, text="Recherche")
        # BUTTONS :
        self.bouton_display = Button(self, text="Afficher", command=self.display_something)
        self.bouton = Button(self, text="Quitter", command=self.quit_window)
        self.bouton_add_animal = Button(self, text="Add", command=self.add_animal)
        # ENTRIES :
        self.entries = {}
        self.entries_label = {}
        # LISTBOX :
        self.liste = Listbox(self) # listbox vide au départ
        counter_name = 0 # position dans la listebox
        for names in self.name_list : # pour chaque animal on récupère le nom
            counter_name += 1
            self.liste.insert(counter_name, names) # on ajoute à la nouvelle position le nouveau nom
        # AFFICHAGE :
        for att in self.attributes:
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)
        self.label.pack()
        self.label1.pack()
        self.label_search.pack()
        self.liste.pack()
        self.bouton_display.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.bouton.pack()
        self.bouton_add_animal.pack()

    def quit_window(self):
        """La vue demande au controller de fermer la fenêtre"""
        self.controller.quit_window()

    def display_something(self):
        """Pour changer ce qui est affiché dans un des labels de la fenêtre de la vue
        La fonction display vient du controller. On affiche ce qui est actuellement sélectionné dans la listbox"""
        self.controller.display(self.liste.get(ACTIVE))

    def display_label(self, value):
        """Utilisée dana le controller"""
        self.label1['text'] = value
        

    def add_animal(self):
        """Ajouter un animal au dico. Utilise le controller pour ajouter l'animal dans le fichier txt."""
        dict_animal = {}
        for key in self.entries:
            dict_animal[key] = self.entries[key].get()
            self.entries[key].delete(0,END)
        self.controller.add_animal(dict_animal)
        

    def view_window(self):
        """Pour que la fenêtre reste affichée"""
        self.title("Ma Première App :-)")
        self.mainloop()

if __name__ == "__main__":
    app = Application()
    app.view_window()