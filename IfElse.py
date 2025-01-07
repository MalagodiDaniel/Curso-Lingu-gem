#ligou = False

#Robo = ""

#if ligou:
   #print("Robo ativado")
   #Robo = "Robo funcionando normalmente"
#else:
    #print("Robo desligado")
    #Robo = "Falha no sistema"

#print("Status do Robo: " + Robo)


#NiveisDeRotacaoMotor = 2000

#if NiveisDeRotacaoMotor <= 10 : 
        #print("Motor com rotação baixa")
#elif NiveisDeRotacaoMotor >= 10 and NiveisDeRotacaoMotor <= 50:
        #print("Motor com rotação muito alta")

#else:
        #print("Motor do robo explodiu")
        
        
        
        
        
####LAÇOS DE REPETIÇÃO### 

##--FOR & WHILE--##

#for contador in range(5):
    #print(contador)

## A função `range()` em Python é usada para gerar uma sequência de números.
## É comumente utilizado em loops para iterar sobre uma série de valores 


pontos_de_vida = 0

for i in range(1, 11):
    pontos_de_vida += 1
    print("Tomou poção mágica" + str(i))

print(str(pontos_de_vida) + " Totais ")


