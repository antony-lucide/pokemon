import Pokemon as pk
from Eau import *
from Feu import *
import random
from var import *

class Combat():
#Class combat avec les différentes méthodes pour faire un combats de pokémons
    def __init__(self,pokemon1,pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

#Si un pokemon meurt, je print un résultat
    def vérifie(self):
        if self.__vie > 0:
            print('Plus de vie !')
#Affiche le vainqueur du duel
    def renvoie(self):
        if self.__vie > 0 and self.defense >= 0:
            print(self.__nom)
    
#Retourne une valeur aléatoire pour faire combattre les pokémons
    def aléatoire(self):
        return random.choice([0,1])
        
#Pour récuperer le type du pokémon
    def récupère(self):
        return types[dict[self.pokemon1.type]][dict[self.pokemon2.type]]
    
#Malus en cas d'attaque
    def enlève(self):
        if self.pokemon1.attaque >= 20 and self.pokemon1.defense  >= 10:
            self.pokemon2.__vie -= 10
        elif self.pokemon2.attaque >= 10:
            self.pokemon1.__vie -= 20

#En cas de perdant, je retourne une valeur bool
    def perdant(self):
        if self.pokemon1.accesseur_vie() == 0:
            return True
        elif self.pokemon2.accesseur_vie() == 0:
            return True
        return False
    
#Méthode pour faire tourner la partie, et faire combattre les pokémons
    def jeux(self):
        
        while True:
            result = self.aléatoire()
            if result == 1:
                self.pokemon1.mutateur_vie(self.pokemon1.accesseur_vie() - 1)
                self.pokemon1.mutateur_defense(self.pokemon1.accesseur_defense() + 1) 
                print("pok0 vie", self.pokemon1.accesseur_vie())
                print("Defense pok0",self.pokemon1.accesseur_defense())
            elif result == 0:
                self.pokemon2.mutateur_vie(self.pokemon2.accesseur_vie() - 1)
                self.pokemon2.mutateur_defense(self.pokemon2.accesseur_defense() + 1)
                print("pok1 vie", self.pokemon2.accesseur_vie())
                print("Defense pok1",self.pokemon2.accesseur_defense())
            if self.perdant():
                break


dracofeu  = Type2('dracofeu')
chenipan  = Feu('chenipan')
instance3 = Combat(dracofeu,chenipan)

print(instance3.jeux())