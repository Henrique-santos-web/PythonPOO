class Gafanhoto: #* Declaração de Classe
    def __init__(self): #* Método construtor

        #* Atributos de Instância (atrbutos do objeto):
        self.nome = ""
        self.idade = 0

    #* Método de Instância (funções do objeto):
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos"

#* Declaração de Objetos (instânciar ou criar o objeto)
g1 = Gafanhoto()
g1.nome = "Pedro"
g1.idade = 12
g1.aniversario()
print(g1.mensagem())
#* O que está acontecendo aqui? Eu criei um objeto que terá todos os atributos e funções
#* E quando eu print ele, chamo a função de mensagem

#! OBS: Quando eu crio um objeto e printo ele, ele mostra apenas seus atributos.
#! OBS: Então tenho que usar um ponto e chamar a função que eu quero que ele execute 
#? Instânciar = Pegar a planta e criar uma casa (planta: MinhaCasa | casa: obj = MinhaCasa())

g2 = Gafanhoto()
g2.nome = "Erick"
g2.idade = 17
g2.aniversario()
print(g2.mensagem())

# objeto.atributo = caracteristicas
# objeto.método() = função