import random

class naradi:
    def __init__(self, znacka:str, model:str):
        self.znacka = znacka
        self.model = model

        pass

    def identifikace(self):
        return f"Značka - {self.znacka} a Model {self.model}"

    def pracuj(self):
       return "nářadí pracuje!"


class Akuvratcka(naradi):
    def __init__(self, znacka, model, baterie:int):
        super().__init__(znacka, model)
        self.baterie = baterie

    def pracuj(self):
        if self.baterie > 0:
            self.baterie -= 10
            return f"Vrtačka vrtá! a {self.baterie}%"
        else:
            return f"Nutno nabít! a {self.baterie}%"


class motorovapila(naradi):
    def __init__(self, znacka, model, nadrz_plna:bool):
        super().__init__(znacka, model)
        self.nadrz_plna = nadrz_plna

    def pracuj(self):
        if self.nadrz_plna:
            return "nádrž je plná"
        else:
            return "potřeba doplnit benzin!!!"


Honda = Akuvratcka("Honda", "Barabola", 50)
print(Honda.identifikace())
print(Honda.pracuj())

print("---" *20)

hecht = motorovapila("hecht", "A128", True)
print(hecht.identifikace())
print(hecht.pracuj())

print("---" *20)

while Honda.baterie > 0:
    print(Honda.pracuj())

print("---" *20)

print(Honda.pracuj())
