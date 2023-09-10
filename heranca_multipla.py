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
    pass

class Orinitorrinco(Mamifero, Ave):
    pass


gato = Gato(nro_de_patas = 4, cor_do_pelo="frajola")
print("Objeto: ", gato)

orinitorrinco = Orinitorrinco(nro_de_patas=2, cor_do_pelo="vermelho", cor_do_bico="laranja")
print("Objeto: ", orinitorrinco)