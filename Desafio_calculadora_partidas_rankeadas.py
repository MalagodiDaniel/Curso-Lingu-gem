

vitorias = 100
derrotas = 67
saldo_heroi = int(vitorias) - int(derrotas)



if saldo_heroi < 10:
    nivel = "Ferro"
elif 11 <= saldo_heroi <= 20:
    nivel = "Bronze"
elif 21 <= saldo_heroi <= 50:
    nivel = "Prata"
elif 51 <= saldo_heroi <= 70:
    nivel = "Ouro"
elif 71 <= saldo_heroi <= 80:
    nivel = "Platina"
elif 81 <= saldo_heroi <= 90:
    nivel = "Ascendente"
elif 91 <= saldo_heroi <= 100:
    nivel = "Imortal"
else:  
    nivel = "Radiante"

      
  

  
         
print("O Herói tem saldo de " + str(saldo_heroi) + " está no nível de "+ nivel)      