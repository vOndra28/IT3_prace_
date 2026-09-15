class robot:

    def __init__ (self, oznaceni:str, baterie:int, ukol:str = "Vybít hrad v Karpatech"):
            self.oznaceni = oznaceni
            self.baterie = baterie
            self.ukol = ukol

            pass
        
    def zvuk(self):
        return "RrrrRrrRRRRRr"
    
    def diagnostika(self):
        return f"Označení {self.oznaceni} // Baterie {self.baterie}"
    
    def aktualni_ukol(self):
        return f"úkol: {self.ukol}"
    
    def zadej_ukol(self, newukol:str):
        self.ukol = newukol
        return f"nový úkol je {newukol}"
    

Patriot = robot("RPK20", 80)
print(Patriot.oznaceni)
print(Patriot.baterie)
print(Patriot.ukol)
print(Patriot.zvuk())
print(Patriot.diagnostika())
print(Patriot.aktualni_ukol())
print(Patriot.zadej_ukol("Vykašli se na to."))

