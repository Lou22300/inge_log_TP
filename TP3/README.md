# TP3 Ingénierie Logicielle et science reproductible :  
## Auteure :  
Lou Bergogne  
*M1 DLAD*   
## Objectifs :  
Ce TP a pour objectifs d'**apprendre à utiliser les classes** en python.  
Pour cela, on crée une première classe qui permet des créer des animaux.  
On crée ensuite d'autres classes (*Human*, *Snake* et *Dog*) qui **héritent** des méthodes de la classe Animal.  
Certaines de ces classes ont aussi des attributs spécifiques, comme c'est le cas de la classe *Snake* (à laquelle on ajoute la taille), ou de la classe *Dog* (à laquelle on ajoute la race).  
  
Chaque animal a une mère et peut **retrouver tous ses parents** (la mère de sa mère de sa mère...) grâce à la fonction *show_parents()*.  
Chaque animal peut **retrouver tous ses descendants** (ses enfants, leurs enfants, et leurs enfants...) grâce à la fonction *show_parents()*.  
Pour le premier animal crée dans chaque espèce, la mère est "LUCA" (*Last Comon Ancestor*)
