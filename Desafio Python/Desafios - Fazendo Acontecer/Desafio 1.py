import random

number = random.randint(1, 100)

guess = int(input("Digite um número entre 1 e 100: "))

while guess != number:
    if guess < number:
        print("O número é muito baixo. Tente novamente.")
    else:
        print("O número é muito alto. Tente novamente.")
    guess = int(input("Digite um número entre 1 e 100: "))

print("Parabéns! Você acertou!")
