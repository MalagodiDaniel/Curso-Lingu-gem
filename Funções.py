

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

## O que são parâmetros de uma função? ##
# Valores que podem ser passados para a função quando ela é chamada e que permitem que a função
# realize operações com esses valores

## Quantos parâmetros uma função pode receber? ##
# Geralmente não há um limite fixo  #

## Qual é a principal vantagem de usar funções que recebem parâmetros? ##
# Reutilização da mesma lógica da função com diferentes valores de entrada #

