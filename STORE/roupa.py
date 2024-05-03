roupa = str(input("Qual roupa você vai querer? "))
valor = float(input("Quanto custa essa roupa? (seja honesto) "))
quant = int(input("Quantas você quer? "))

total = valor * quant

print("Você escolheu", f"{quant}", "da peça", f"{roupa}", "isso dá um total de ", f"{total}")