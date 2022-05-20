time1 = str(input("NOME DO PRIMEIRO TIME: "))
time2 = str(input("NOME DO SEGUNDO TIME: "))
golsTime1 = int(input("PLACAR DO PRIMEIRO TIME: "))
golsTime2 = int(input("PLACAR DO SEGUNDO TIME: "))
if golsTime1 > golsTime2:
    print("{} GANHOU O JOGO".format(time1))
elif golsTime2 > golsTime1:
    print("{} GANHHOU O JOGO". format(time2))
else:
    print("O JOGO ENTRE {} E {} TERMINOU EMPATADO.".format(time1, time2))
