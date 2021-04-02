from Animal import *

class Zoo:

    def __init__(self,listeDesAnimaux=None):

        self.liste = []
        if listeDesAnimaux is not None:
            for un_animal in listeDesAnimaux:
                self.add_animal(un_animal)

    def __str__(self):
        return f"Mon zoo N°3:{self.liste}"
        

    def se_deplacer(self):
        pass
        

    def add_animal(self,un_animal):

        if isinstance(un_animal,Animal):
            return self.liste.append(un_animal)
        else:
            raise ValueError ("Ce n'est pas un animal valide!")
            
    #def add_zoo(self,secondZoo):
    #    self.liste+= secondZoo.liste       

    def __add__(self,secondZoo):
        zoo3 = self.liste + secondZoo.liste
        return Zoo(zoo3)