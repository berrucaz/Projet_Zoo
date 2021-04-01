from Animal import *

class Oiseau(Animal):
    
    def __init__(self,poids,taille,altitude_max):
        #Animal.__init__(self,poids,taille)
        super(Oiseau,self).__init__(poids,taille)
        altitude_max=1000

    def se_deplacer(self):
        print("Mes chers parents,je vole")   

