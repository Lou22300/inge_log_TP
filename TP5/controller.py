"""Le controller fait le lien entre la vue et le modèle. Donc on importe les classes de
ces deux scripts."""

from vue import Application
from model import Model

class Controller() :
    def __init__(self):
        """On donne au controller le modèle et la vue (model et application)"""
        self.model = Model("a.txt")
        self.model.read_file() # création d'un dico qui contiendra les animaux présents dans le fichier txt
        self.view = Application(self)
        self.view.view_window() # affichage de la fenêtre de la vue*

    def display(self, value):
        """Pour changer un label selon l'animal que l'on cherche"""
        self.view.display_label(self.model.dico_animaux[value])

    def add_animal(self, dict_animal):
        """Pour ajouter un animal"""
        self.model.save(dict_animal)

    def get_model_entries(self):
        """Pour récupérer les attributs d'un animal.
        La fonction get_attribute vient du model"""
        return self.model.get_attributes()

    def get_names_list(self) :
        return self.model.creates_namelist()

    def quit_window(self):
        """Pour fermer la fenêtre de de lvue"""
        print("close app")
        self.model.close()
        self.view.destroy()

if __name__ == "__main__" :
    C = Controller()