# TP5 Ingénierie Logicielle et science reproductible :  
## Auteure :  
Lou Bergogne  
*M1 DLAD*   
## Objectifs du TP :  
Ce TP a pour objectif d'apprendre à jongler entre plusieurs classes avec un modèle d'architecture Modèle-Vue-Contrôleur.  
La **Vue**, crée dans le fichier *view.py*, est la partie du programme qui sera accessible par l'utilisateur. C'est l'interface graphique.
La classe présente dans ce programme, appelée *Application*, hérite de la classe *Tkinter*.  
Le **Modèle**, crée dans le fichier *model.py* correspond au fond du programme. Ici, c'est le modèle qui permet, lorsu'il est appelé, de crée, modifier ou supprimer des animaux d'un fichier texte. La classe *Model* utilise la classe *Animal* du fichier *animal.py*.  
Le **Contrôleur**, crée dans le fichier *controller.py*, permet de faire le lien entre la vue et le modèle. Lorsque l'utilisateur agît sur la Vue, le contrôleur donne les ordres au Modèle.  
  
Le Contrôleur doit connaître la Vue et le Modèle, qui ne se connaissent pas entre eux mais ont tout deux accès au Contrôleur.  
Aucune décision n'est prise par le Modèle ou la Vue.
## Objectifs du programme :
Ce programme permet de **stocker des informations concernant des animaux** dans un fichier texte.  
Les noms des animaux présents dans le fichier sont affichés dans une **listbox** dans l'interface graphique.  
Il est possible d'**ajouter, supprimer ou modifier des animaux** dans le fichier texte.  
Le **nom** d'un animal est **obligatoire** et doit être **unique**. Si le **nom n'est pas rentré**, un **message d'avertissement apparaît**. Si le nom existe déjà, l'animal portant ce nom est modifié.  
Lorsqu'on **affiche un animal** après l'avoir sélectionné dans la listbox, ces informations s'affichent **dans les champs de saisie**.
Les champs non-vides seront alors modifiés pour correspondre à la nouvelle saisie. Des champs inchangés ou laissés vides n'entraîneront pas de modifications. Si c'est le nom qui est modifié, alors un nouvel animal sera crée.  
Lorsque l'utilisateur **clique sur les boutons**, des fenêtres **pop-ups** apparaissent pour confirmer que l'action a bien été prise en compte.  Après **l'ajout ou la modification** d'un animal, les **champs de saisie sont vidés**.  
L'utilisateur a la possibilité de **sauvegarder les modifications** apportées au fichier au fur et à mesure en appuyant sur le bouton *Save*, ou bien la sauvegarde se fait automatiquement lorsque l'on appuie que le bouton *Save and Quit*.
## Lancement du programme :
Pour lancer ce programme, il faut faire tourner le script *controller.py*.