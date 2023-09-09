class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
       self.cor = cor
       self.modelo = modelo
       self.ano = ano
       self.valor = valor
    
    def buzinar(self):
        print("Triiiiiimmm... Triiiimmmmmm")
    
    def parar(self):
        print("Bicicleta parando...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vruuuuuuuuuuuuuuuuuuuumm")
    
    def __str__(self):
        return f"{self.__class__, __name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        

b1 = Bicicleta("azul", "Berlineta", 2022, 1200)
b2 = Bicicleta("vermelha", "Caloi", 2023, 1000)

b1.buzinar()
b1.parar()
b1.correr()

print("A bicicleta ", b1.modelo, "é do ano ", b1.ano)