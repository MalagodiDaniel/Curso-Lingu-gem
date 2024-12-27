ligou = False

Robo = ""

if ligou:
    print("Robo ativado")
    Robo = "Robo funcionando normalmente"
else:
    print("Robo desligado")
    Robo = "Falha no sistema"

print("Status do Robo: " + Robo)


NiveisDeRotacaoMotor = 2000

if NiveisDeRotacaoMotor <= 10 : 
        print("Motor com rotação baixa")
elif NiveisDeRotacaoMotor >= 10 and NiveisDeRotacaoMotor <= 50:
        print("Motor com rotação muito alta")
else:
        print("Motor do robo explodiu")
    

