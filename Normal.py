from Pokemon import *


class Normal(Pokemon):
#Classe et méthodes pour définire le type de pokémons    
    def __init__(self):
        Pokemon.__init__(self)
        self.normal = 'normal'