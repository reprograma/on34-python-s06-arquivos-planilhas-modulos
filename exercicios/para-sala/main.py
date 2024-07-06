#https://docs.python.org/3/library/functions.html#open
import csv

data=[['Data', 'Acessos']] #definimos uma váriavel global para armazenar nossos dados de ambos os csvs, aqui definimos o cabeçalho

with open('abril-2024_tratado.csv', newline='', encoding='utf-8') as csvfile: #abro meu csv e carrego os dados na variavel csvfile
    leitor = csv.reader(csvfile) #leio meu input csv e transformo ele em um objeto que possa ser manipulado dentro do código

    for linha in leitor: #passo por cada linha do meu csv (aqui é lista)
        if linha != ['Data', 'Acessos']: #faço uma regra para excluir o cabeçalho da minha matriz (lista de listas)
            data.append(linha) #insiro minha linha (lista) na minha variavel global data que já possui o cabeçalho

#aqui minha variavel data já estará com os dados do mês de abril!!!
#data=[
# ['Data', 'Acessos'],
# [01/04/2024, 125],
# [02/04/2024, 125],
# [03/04/2024, 125]
#]

with open('maio-2024_tratado.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)

    for linha in leitor:
        if linha != ['Data', 'Acessos']:
            data.append(linha)

#aqui minha variavel data já estará com os dados do mês de abril e maio!!!
#data=[
# ['Data', 'Acessos'],
# [01/04/2024, 125],
# [02/04/2024, 125],
# [03/04/2024, 125],
# [01/05/2024, 125],
# [02/05/2024, 125],
# [03/05/2024, 125]
#]

#aqui eu crio um novo csv e escrevo os dados da variavel data nele
with open('abril-maio-2024.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerows(data) #aqui os dados estão sendo escritos!!!