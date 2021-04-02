from Animal import *

class Oiseau(Animal):
    
    def __init__(self,poids,taille,altitude_max):
        
        super(Oiseau,self).__init__(poids,taille)
        self.oiseau_altitude_max=altitude_max

    def se_deplacer(self):
        print("Mes chers parents,je vole")   

