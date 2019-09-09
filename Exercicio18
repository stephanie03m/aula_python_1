'''18 - Crie uma classe animal com o método comer,
este método deve  escrever na tela "o animal esta comendo".
Depois disso crie as classes cachorro, cavalo e gato e
implemente o método comer de acordo com o que cada animal
come. Crie uma classe AnimalTeste e coloque os três animais
dentro de uma lista de animais e chame o método comer
polimorficamente (com um for)'''


class Animal:
    def comer(self):
        print("O animal está comendo: ", end=" ")


class Cachorro(Animal):
    def comer(self):
        super().comer()
        print("carne, cachorro")


class Cavalo(Animal):
    def comer(self):
        super().comer()
        print("grama, cavalo")

class Gato(Animal):
    def comer(self):
        super().comer()
        print("peixe, gato")


class AnimalTeste:
    lista = [Gato(), Cachorro(), Cavalo()]
    for animal in lista:
        animal.comer()


if __name__ == '__main__':
    AnimalTeste()
    
