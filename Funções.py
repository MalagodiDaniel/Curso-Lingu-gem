

def torrar():
    print("torrando pão")

# Chamando a função
torrar()


def injetarPao():
    print("inserindo pão na torradeira")
    
injetarPao()


## NÃO COLOCAR NÚMEROS NO NOME DAS FUNÇÕES ##


## FUNÇÕES COM PARAMETROS ##



def torrar1(pao):
    print("Torrada feita com " + pao)

torrar1("Pão frances")



def torrar1(pao, nome = "cliente"):
    print("Torrada feita com " + pao)
    print("ELe é um pedido do cliente " + nome)


torrar1("Pão frances " , "Malagodi")