import re

class Generatore:

    def __init__(self, filename:str):
        testo = ""
        with open(filename, 'r') as file:
            testo = file.read()        
            pattern = r'[^\w\s]'           
            testo = re.sub(pattern, '', testo)
        
        pattern = r'[ \n]'
        self.d = {}    
        parole = re.split(pattern, testo)
        print(parole)

g = Generatore('testo.txt') 
