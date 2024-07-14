import csv

with open('exercicios/para-sala/abril-2024-tratado.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)