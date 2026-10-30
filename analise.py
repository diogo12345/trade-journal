import csv


def ler_resultados(caminho):
    """Lê o CSV e devolve a lista de resultados como floats."""
    resultados = []
    with open(caminho, newline="") as f:
        for linha in csv.DictReader(f):
            resultados.append(float(linha["resultado"]))
    return resultados


def total(resultados):
    """Devolve a soma de todos os resultados."""
    return sum(resultados)


def win_rate(resultados):
    """Devolve a fração de trades ganhadores (entre 0 e 1)."""
    if not resultados:
        return 0
    return sum(1 for n in resultados if n > 0) / len(resultados)


def ganho_medio(resultados):
    """Média dos resultados positivos. Devolve 0 se não houver."""
    ganhos = [n for n in resultados if n > 0]
    if not ganhos:
        return 0
    return sum(ganhos) / len(ganhos)


def perda_media(resultados):
    """Média dos resultados negativos. Devolve 0 se não houver."""
    perdas = [n for n in resultados if n < 0]
    if not perdas:
        return 0
    return sum(perdas) / len(perdas)


def main():
    resultados = ler_resultados("exemplo_trades.csv")
    if not resultados:
        print("Sem trades.")
        return

    print(f"Total:       {total(resultados):.2f}")
    print(f"Win rate:    {win_rate(resultados):.1%}")
    print(f"Ganho médio: {ganho_medio(resultados):.2f}")
    print(f"Perda média: {perda_media(resultados):.2f}")


if __name__ == "__main__":
    main()