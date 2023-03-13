from Pokemon import *

class Type2(Pokemon):
#Classe et méthodes pour définire le type de pokémons    
    def __init__(self,nom):
        Pokemon.__init__(self,nom)
        self.type =  'eau'
