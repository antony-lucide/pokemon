import random
import json
#Importation fichier json.
def json1():
    f = open('Pokedex.json')
    if f is not None:
        return(json.load(f))

def json2():
    f = open('pokemon.json')
    if f is not None:
        return(json.load(f))

class Pokemon:
#Class pokemon avec les différentes méthodes pour afficher les informations du pokemon
    def __init__(self,nom):
        self.__nom = nom
        self.types = ''
        self.__vie = 100
        self.attaque = 50
        self.defense = 0

    def information(self):
        print(self.__nom,self.types,self.__vie,self.attaque,self.defense,)

    def accesseur_vie(self):
        return self.__vie

    def mutateur_vie(self,vie):
        self.__vie = vie

    def accesseur_nom(self):
        return self.__nom

    def mutateur_nom(self,nom):
        self.__nom = nom
    
    def accesseur_defense(self):
        return self.defense

    def mutateur_defense(self,defense):
        self.defense = defense