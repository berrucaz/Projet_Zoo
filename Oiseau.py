from Animal import *

class Oiseau(Animal):
    
    def __init__(self,poids,taille):
        Animal.__init__(self,poids,taille)
    
    def se_deplacer(self):
        print("Mes chers parents,je vole")
    
