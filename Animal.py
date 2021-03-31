class Animal:

    def __init__(self,poids,taille):
        self.animal_poids=poids
        self.animal_taille=taille
    
    def se_deplacer(self):
        pass



unAnimal = Animal(1.5,1)

unAnimal.se_deplacer()
