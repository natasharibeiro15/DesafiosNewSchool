import random

print("Jogue Jo Ken Pô!")

jogador1 = input("Jogador 1: Pedra, Papel ou Tesoura?")
jogador2 = input("Jogador 2: Pedra, Papel ou Tesoura?")

def jogo(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate"
    elif jogador1 == "pedra" and jogador2 == "tesoura":
        return "Jogador 1 venceu"
    elif jogador1 == "tesoura" and jogador2 == "papel":
        return "Jogador 1 venceu"
    elif jogador1 == "papel" and jogador2 == "pedra":
        return "Jogador 1 venceu"
    else:
        return "Jogador 2 venceu"


resultado = jogo(jogador1, jogador2)

if resultado == "Jogador 1 venceu":
    print("Jogador 1 venceu!")
elif resultado == "Jogador 2 venceu":
    print("Jogador 2 venceu!")
else:
    print("Empate!")
