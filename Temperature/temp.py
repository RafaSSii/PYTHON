temps = []

print("Você quer informar a temperatura? \n1 - Sim \n2 - Não")

escolha = int(input("Digite o número correspondente: "))

if escolha == 1:
    qtdT = int(input("\nQuantas temperaturas você deseja informar? "))

    for x in range(qtdT):

        temp = float(input("Quanto de temperatura? "))
        temps.append(temp)

if temps:
    MAXtemp = max(temps)
    MINtemp = min(temps)

    media = (MINtemp + MAXtemp) / qtdT

    print(f"A maior temperatura foi de {MAXtemp} \nA menor temperatura foi de {MINtemp} \nA média foi de {media}")

else:
    print("Nenhuma temperatura foi informada")