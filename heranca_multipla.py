class Animal:
    def __init__(self, nro_de_patas):
        self.nro_de_patas = nro_de_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_do_pelo, **kw):
        super().__init__(**kw)
        self.cor_do_pelo = cor_do_pelo

class Ave(Animal):
    def __init__(self, cor_do_bico, **kw):
        super().__init__(**kw)
        self.cor_do_bico = cor_do_bico

class Gato(Mamifero):
    def __init__(self, cor_do_pelo, raca, **kw):
        super().__init__(cor_do_pelo, **kw)
        self.raca = raca

class Orinitorrinco(Mamifero, Ave):
    def __init__(self, cor_do_bico, cor_do_pelo, nro_de_patas):

        super().__init__(cor_do_pelo=cor_do_pelo, 
                         cor_do_bico = cor_do_bico, nro_de_patas = nro_de_patas)


gato = Gato(nro_de_patas = 4, cor_do_pelo="frajola", raca="Não definida")
print("Objeto: ", gato)

orinitorrinco = Orinitorrinco(nro_de_patas=2, cor_do_pelo="vermelho", cor_do_bico="laranja")
print("Objeto: ", orinitorrinco)