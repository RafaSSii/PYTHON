import random

opcoes = ["pedra", "papel", "tesoura"]
computador = random.choice(opcoes)

user = input("Escolha pedra, papel ou tesoura: ").lower()

if user not in opcoes:
    print("Opção inválida! Tente novamente.")
        

    print(f"\nComputador escolheu: {computador}")
    
if user == computador:
     print("Empate!")

elif user == "pedra" and computador == "tesoura" or \
        user == "papel" and computador == "pedra" or \
        user == "tesoura" and computador == "papel":
            print("Você ganhou!")

else:
    print("Você perdeu!")
