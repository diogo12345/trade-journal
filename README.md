# Trade Journal

Ferramenta de linha de comandos em Python para analisar um diário de trades a partir de um ficheiro CSV.

## O que calcula

- Total de resultados
- Win rate
- Ganho médio e perda média
- Expectancy e drawdown máximo *(em desenvolvimento)*

## Como usar

Requer Python 3.10 ou superior.

```bash
git clone https://github.com/diogo12345/trade-journal.git
cd trade-journal
python3 analise.py
```

## Formato do CSV

```csv
data,ativo,resultado
2026-10-01,EURUSD,50.0
2026-10-02,AAPL,-20.0
2026-10-05,USDJPY,35.5
2026-10-06,EURUSD,-15.0
```

Há um ficheiro de exemplo em `exemplo_trades.csv`.

## Exemplo de output

```
Total:       50.50
Win rate:    50.0%
Ganho médio: 42.75
Perda média: -17.50
```

## Licença

MIT, ver [LICENSE](LICENSE).