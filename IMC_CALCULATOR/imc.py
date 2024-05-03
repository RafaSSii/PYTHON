altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

if imc <= 18.4:
    print(" Você está abaixo do peso")
if imc >= 18.5 and imc <= 24.9:
    print(" Você está no peso ideal")
if imc >= 25.0 and imc <= 29.9:
    print(" Você está acima do peso")
if imc >= 30.0 and imc <= 34.9:
    print(" Você está com obesidade grau 1")
if imc >= 35.0:
    print(" Tá quase morto")