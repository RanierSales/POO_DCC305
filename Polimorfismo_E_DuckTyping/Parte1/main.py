class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"
    
class Leao(Animal):
    def emitir_som(self):
        return "Rugido"

class Som():
    animais = []
    def adicionar_animal(self, animal):
        Som.animais.append(animal)
    
    def emitir_sons(self):
        for animal in Som.animais:
            print(animal.emitir_som())


som = Som()

som.adicionar_animal(Cachorro())
som.adicionar_animal(Gato())
som.adicionar_animal(Leao())

som.emitir_sons()
