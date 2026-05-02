# Abreviando o método mensagem usando uma def __str__ (métodos mágicos ou dunder methods)

# ! (Vermelho): Alertas ou avisos críticos (Ex: // ! IMPORTANTE: Não alterar esta linha).

# ? (Azul): Dúvidas ou perguntas (Ex: // ? Por que este loop está aqui?).

# TODO (Laranja): Tarefas pendentes (Ex: // TODO: Refatorar esta função).

# * (Verde): Informações de destaque ou comentários formatados.

# // (Riscado/Cinza): Comentários que devem ser ignorados ou "comentados para fora".

class Gafanhoto: #* Declaração de Classe
    def __init__(self, nome = "", idade = 0): #* Método construtor

        #* Atributos de Instância (atrbutos do objeto):
        self.nome = nome
        self.idade = idade

    #* Método de Instância (funções do objeto):
    def aniversario(self):
        self.idade += 1

    #//                                                            
    #TODO Método clássico
    # def mensagem(self):
    #     return f"{self.nome} é Gafanhoto e tem {self.idade} anos"

    #* g2 = Gafanhoto("Erick", 17)
    #* g2.aniversario()
    #* print(g2.mensagem())
    #//                                                            

    #* Método abreviado
    def __str__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos"

    

#* Declaração de Objetos (instânciar ou criar o objeto)
g1 = Gafanhoto("Pedro", 12) #? O que está acontecendo aqui? Eu criei um objeto que terá todos os atributos e funções (instânciei).
g1.aniversario() #? Chamei a def aniversário que executa a função de pegar a própria(self) idade e somar mais um (+1).
print(g1) #? Aqui está só g1, pois a def __str__ com return permite chamar o objeto com sua função (sua função é retornar os dados escritos ao lado de return).


#! OBS: Quando eu crio um objeto e printo ele, ele mostra apenas seus atributos
#! OBS: Então tenho que usar um ponto e chamar a função que eu quero que ele execute.

#! OBS: No método mágico (def "__str__"), isso muda e está explicado na linha 41 até 43.


# objeto.atributo = caracteristicas
# objeto.método() = função