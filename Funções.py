

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
def main():
    user_name = get_first_name("Daniel-Almeida-Malagodi", "-")
    print("Seja bem-vindo " + user_name)

    user_name = get_first_name("Memphis César Depay", " ")
    print("Seja bem-vindo " + user_name)

def get_first_name(name, split_char):
    first_name = name.split(split_char)
    return name.replace("-"," ")


if __name__ == "__main__":
    main()

## Função get_first_name:
# A função get_first_name recebe dois argumentos:
# name: Uma string que contém o nome completo.
# split_char: O caractere utilizado para separar as partes do nome.
# Dentro da função, o método .split(split_char) divide a string name em uma lista de partes com base no caractere fornecido em split_char.
# O índice [0] acessa o primeiro elemento da lista, que corresponde ao primeiro nome.
# A função retorna este primeiro nome.
