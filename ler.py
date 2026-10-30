import csv
import sys

resultados = []
with open("trades.csv", newline="") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        resultados.append(float(linha["resultado"]))

if len(resultados) == 0:
    print("Sem trades")
    sys.exit()

soma = sum(n for n in resultados)
ganhar = 0
for n in resultados:
    if n > 0:
        ganhar += 1

win_rate = ganhar / len(resultados)
print(f"Total: {soma}, Nº vencedoras: {ganhar}, Win Rate: {win_rate:.1%}")