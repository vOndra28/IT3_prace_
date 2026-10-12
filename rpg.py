import random

class Postava:
    def __init__(self, jmeno:str, zdravi:int):
        self.jmeno = jmeno
        self.zdravi = zdravi

        pass

    def predstav_se(self):
        return f"jmenuji se {self.jmeno} a moje zdraví je {self.zdravi}"

    def utok(self):
        return "0"

class Rytir(Postava):
    def __init__(self, jmeno, zdravi, brneni:int):
        super().__init__(jmeno, zdravi)
        self.brneni = brneni

    def utok(self):
        poskozeni = random.randint(10, 20)
        return f"udělené poškození je {poskozeni}"

    def zablokuj(self):
        return "zablokováno"


class Mag(Postava):
    def __init__(self, jmeno, zdravi, mana:int):
        super().__init__(jmeno, zdravi)
        self.mana = mana

    def utok(self):
        if self.mana >= 10:
            self.mana -=10
            poskozeni = random.randint(25, 40)
            return f"Holí udeřil {poskozeni}"
        else:
            return "Nemá dostatek many, a proto udeřil holí za 5"

MgVapko = Rytir("MgVapko", 80, 60)
print(MgVapko.predstav_se())
print(MgVapko.utok())

print("---" *20)

MgJabko = Mag("MgJabko", 40, 60)
print(MgJabko.predstav_se())
print(MgJabko.utok())


print("---" *20)



druzina = [MgVapko, MgJabko]

for postava in druzina:
    print(postava.predstav_se())
