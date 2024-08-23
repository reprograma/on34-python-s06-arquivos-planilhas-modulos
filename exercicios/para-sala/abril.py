import csv

data = [['data', 'acessos']]
with open('exercicios/para-sala/abril _limpo.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        if linha != ['data', 'acessos']:
            data.append(linha)
        
with open('exercicios/para-sala/maio_limpo.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        if linha != ['data', 'acessos']:
            data.append(linha)

with open('abril_maio_2024.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerows(data)

print(data)
