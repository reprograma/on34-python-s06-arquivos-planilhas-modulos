import csv

norte = []
nordeste = []
co = []
sul = []
sudeste = []

somas = {
    'Norte': 0,
    'Nordeste': 0,
    'Sul': 0,
    'Centro-Oeste': 0,
    'Sudeste': 0
}

pessoas_x_compras = []

with open('pessoas.csv', newline='', encoding='utf-8') as csvfile:
    pessoa = csv.DictReader(csvfile)
    fieldnames = pessoa.fieldnames + ['preço_do_produto']
    
    for linha in pessoa:
        with open('compras_realizadas.csv', newline='', encoding='utf-8') as csvfile2:
            compra = csv.DictReader(csvfile2)
            for _linha in compra:
                if linha['id_compra'] == _linha['id_compra']:
                    linha['preço_do_produto'] = _linha['preço_do_produto']
                    break
            else:
                linha['preço_do_produto'] = ''
        
        
        if linha['id_compra']:
            pessoas_x_compras.append(linha)
            if linha['regiao'] == 'Norte':
                norte.append(linha['id_compra'])

            if linha['regiao'] == 'Nordeste':
                nordeste.append(linha['id_compra'])

            if linha['regiao'] == 'Centro-Oeste':
                co.append(linha['id_compra'])

            if linha['regiao'] == 'Sul':
                sul.append(linha['id_compra'])

            if linha['regiao'] == 'Sudeste':
                sudeste.append(linha['id_compra'])
            print(linha)

with open('pessoas_x_compras.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for linha in pessoas_x_compras:
        writer.writerow(linha)

with open('compras_realizadas.csv', newline='', encoding='utf-8') as csvfile:
    compra = csv.DictReader(csvfile)
    for linha in compra:
        if linha['id_compra'] in norte:
            somas['Norte'] += float(linha['preço_do_produto'].replace('.', '').replace(',', '.'))

        if linha['id_compra'] in nordeste:
            somas['Nordeste'] += float(linha['preço_do_produto'].replace('.', '').replace(',', '.'))

        if linha['id_compra'] in co:
            somas['Centro-Oeste'] += float(linha['preço_do_produto'].replace('.', '').replace(',', '.'))

        if linha['id_compra'] in sul:
            somas['Sul'] += float(linha['preço_do_produto'].replace('.', '').replace(',', '.'))

        if linha['id_compra'] in sudeste:
            somas['Sudeste'] += float(linha['preço_do_produto'].replace('.', '').replace(',', '.'))

regiao_mais_lucro = max(somas, key=somas.get)
resultado = f"A região que mais deu lucro foi: {regiao_mais_lucro} com um lucro de R${somas[regiao_mais_lucro]:.2f}"

print(resultado)
