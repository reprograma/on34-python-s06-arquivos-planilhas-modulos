import csv

data=[['Data', 'Acessos']] 

with open('abril-2024-tratado.csv', newline='', encoding='utf-8') as csvfile: 
    leitor = csv.reader(csvfile) 
    for linha in leitor: 
        if linha != ['Data', 'Acessos']: 
            data.append(linha)

with open('maio-2024-tratado.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        if linha != ['Data', 'Acessos']:
            data.append(linha)

with open('abril-maio-2024.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerows(data)