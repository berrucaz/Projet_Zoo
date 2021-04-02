from Serpent import *
from Oiseau import *
from Zoo import *

longSerpent = Serpent(poids=1.5,taille=1)
petitOiseau = Oiseau(0.2,0.15,500)
grandOiseau = Oiseau(poids=-2,taille=2,altitude_max=2000)
ani=Animal
zoo1= Zoo([grandOiseau])
zoo2= Zoo([longSerpent,grandOiseau])
zoo3=Zoo([])

longSerpent.se_deplacer()
petitOiseau.se_deplacer()
print("petitOiseau, alti max =" ,petitOiseau.oiseau_altitude_max,"\n")

zooStMarcellin=Zoo([longSerpent])
zooStMarcellin.add_animal(petitOiseau)
zooStMarcellin.add_animal(grandOiseau)
print(zooStMarcellin.liste, "\n")

#print(zooStMarcellin.list[0])
#zooStMarcellin.add_animal(12)
#print(zooStMarcellin)
#print(longSerpent.get_poids)

print(ani(5,1))

zoo3=zoo1.add_zoo(zoo2)
print(zoo3.liste)
