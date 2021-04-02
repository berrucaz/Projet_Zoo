class Animal:

    def __init__(self,poids,taille):
        self.set_poids(poids)
        self.set_taille(taille)
    
    def __str__(self):
        return f"Mon poids est:{self.__poids}, Ma taille est: {self.__taille}"
        

    def se_deplacer(self):
        pass

#Ajoutez une validation de données dans le setter, vous pouvez par exemple
#traiter le cas de l’instanciation d’un animal avec un poids négatif : cette tentative doit
#par exemple renvoyer une erreur (ValueError).

    def set_poids(self,poids):
        if poids < 0:
            try:
                raise ValueError 
            except:
                print(ValueError,"\n","Le poids doit être > 0","\n")
        else:
            self.__poids=poids

    def set_taille(self,taille):
        self.__taille=taille

    def get_poids(self):
        return self.__poids
    
    def get_taille(self):
        return self.__taille

    