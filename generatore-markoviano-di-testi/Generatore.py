import random
import re

class Generatore:

    def __init__(self, filename:str):
        testo = ""

        with open(filename, 'r') as file:
            testo = file.read()   

        pattern = r'[^\w\s]'           
        testo = re.sub(pattern, '', testo)
        testo = testo.lower()
        
        pattern = r'[ \n]' 
        parole = re.split(pattern, testo)

        self.d = {}   

        for i in range(0, len(parole)-1):
            if parole[i] in self.d:
                self.d[parole[i]].append(parole[i+1])
            else: 
                self.d[parole[i]] = [parole[i+1]]
    
    def genera_testo(self, start:str, len_testo):
        testo = ""
        for i in range(0, len_testo-1):
            scelta = random.choice(self.d[start])
            testo += scelta + " "
            start = scelta
        scelta = random.choice(self.d[start])
        testo += scelta
        return testo            

                
        


        


        
g = Generatore('testo.txt') 
testo = g.genera_testo("il",100)
print(testo)
