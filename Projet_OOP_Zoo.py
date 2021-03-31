class Animal:

    def __init__(self,poids,taille):
        self.animal_poids=poids
        self.animal_taille=taille

    #def getTaille(self):
    #    print("ma taille:", self.animal_taille)

    #def getPoids(self)
    #    print("Poids:", self.animal_poids)

    def se_deplacer(self):
        pass

class Serpent(Animal):
    
    def __init__(self,poids,taille):
        Animal.__init__(self,poids,taille)
    
    def se_deplacer(self):
            print("Je rampe")
    

class Oiseau(Animal):
    
    def __init__(self,poids,taille):
        Animal.__init__(self,poids,taille)
    
    def se_deplacer(self):
            print("Mes chers parents,je vole")
    

longSerpent = Serpent(1.5,1)
petitOiseau = Oiseau(0.2,0.15)

longSerpent.se_deplacer()
petitOiseau.se_deplacer()