class chytre_zarizeni:
    def __init__(self, nazev:str, mistnost:str, zapnuto:bool = False):
        self.nazev = nazev
        self.mistnost = mistnost
        self.zapnuto = zapnuto
        pass


    def prepni_stav(self):
        self.zapnuto = not self.zapnuto
        if self.zapnuto:
            return f"{self.nazev} bylo zapnuto!!! "
        
        else:
            return f"{self.nazev} bylo vypnuto!!!"
        
    def proved_akci(self):
        return "zařízení čeká na příkaz!!!"

class chytra_zarovka(chytre_zarizeni):
    def __init__(self, nazev, mistnost, zapnuto = False, barva:str = "bílá"):
        super().__init__(nazev, mistnost, zapnuto)
        self.barva = barva

    def proved_akci(self):
        self.zapnuto = not self.zapnuto
        
        if self.zapnuto:
            return f"{self.nazev} svítí barvou {self.barva}"
        else:
            return "je zhasnuto"
        
    def zmen_barvu(self, nova_barva):
        self.barva = nova_barva
        return f"barva žárovky byla změněna na {self.barva}"
    


class chytra_zasuvka(chytre_zarizeni):
    def __init__(self, nazev, mistnost,aktualni_odber_w:int ,zapnuto = False):
        super().__init__(nazev, mistnost, zapnuto)
        self.aktualni_dober_w = aktualni_odber_w

    def proved_akci(self):
        if self.zapnuto:
            return f"zásuvka propoušit proud. Aktuální odběr {self.aktualni_dober_w}"
        else:
            return "Zásuvka je vypnutá"
        

print("---" *20)


zarovka = chytra_zarovka("Žárovka", "obývák")
print(zarovka.proved_akci())
print(zarovka.zmen_barvu("žlutá"))

print("---" *20)

zasuvka = chytra_zasuvka("zásuvka", "obývák", 20)
print(zasuvka.proved_akci())

print("---" *20)



