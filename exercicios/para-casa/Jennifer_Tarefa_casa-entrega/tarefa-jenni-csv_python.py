import pandas as pd
from io import StringIO

# Dados fornecidos
dados1 = """id_compra,nome_pessoa,regiao
João da Silva,Sul
Ana Souza,Sudeste
Felipe Lima,Centro-Oeste
74,Ana Souza,Nordeste
João da Silva,Norte
14,Ana Souza,Nordeste
79,Ana Souza,Sul
62,Maria Oliveira,Sudeste
94,Ana Souza,Norte
Felipe Lima,Centro-Oeste
Carlos Santos,Nordeste
Felipe Lima,Norte
66,João da Silva,Sudeste
42,Maria Oliveira,Centro-Oeste
64,Ana Souza,Sul
Carlos Santos,Norte
46,João da Silva,Nordeste
90,Carlos Santos,Sul
50,Carlos Santos,Centro-Oeste
8,Felipe Lima,Norte
92,Maria Oliveira,Sudeste
João da Silva,Nordeste
20,Carlos Santos,Sul
Felipe Lima,Centro-Oeste
João da Silva,Norte
12,Maria Oliveira,Sudeste
Maria Oliveira,Nordeste
Ana Souza,Sul
Felipe Lima,Centro-Oeste
59,Ana Souza,Norte
34,Ana Souza,Sudeste
10,Carlos Santos,Nordeste
João da Silva,Sul
72,Maria Oliveira,Centro-Oeste
84,Ana Souza,Norte
Ana Souza,Sudeste
19,Ana Souza,Nordeste
100,Carlos Santos,Sul
Maria Oliveira,Centro-Oeste
48,Felipe Lima,Norte
Felipe Lima,Sudeste
João da Silva,Nordeste
Maria Oliveira,Sul
16,João da Silva,Centro-Oeste
Felipe Lima,Norte
João da Silva,Sudeste
80,Carlos Santos,Nordeste
Ana Souza,Sul
Carlos Santos,Centro-Oeste
3,Carlos Santos,Norte
36,João da Silva,Sudeste
44,Ana Souza,Nordeste
40,Carlos Santos,Sul
Ana Souza,Centro-Oeste
Felipe Lima,Norte
Felipe Lima,Sudeste
30,Carlos Santos,Nordeste
Carlos Santos,Sul
Maria Oliveira,Centro-Oeste
Maria Oliveira,Norte
João da Silva,Sudeste
86,João da Silva,Nordeste
32,Maria Oliveira,Sul
68,Felipe Lima,Centro-Oeste
Felipe Lima,Norte
Carlos Santos,Sudeste
70,Carlos Santos,Nordeste
Felipe Lima,Sul
Carlos Santos,Centro-Oeste
Ana Souza,Norte
82,Maria Oliveira,Sudeste
João da Silva,Nordeste
60,Carlos Santos,Sul
5,João da Silva,Centro-Oeste
1,João da Silva,Norte
Maria Oliveira,Sudeste
22,Maria Oliveira,Nordeste
Carlos Santos,Sul
Felipe Lima,Centro-Oeste
Maria Oliveira,Norte
99,Ana Souza,Sudeste
39,Ana Souza,Norte
Maria Oliveira,Sudeste
26,João da Silva,Nordeste
João da Silva,Sul
96,João da Silva,Centro-Oeste
Carlos Santos,Norte
Carlos Santos,Sudeste
Felipe Lima,Nordeste
Maria Oliveira,Sul
52,Maria Oliveira,Centro-Oeste
Felipe Lima,Norte
76,João da Silva,Sudeste
88,Felipe Lima,Nordeste
28,Felipe Lima,Sul
54,Ana Souza,Centro-Oeste
Maria Oliveira,Norte
24,Ana Souza,Sudeste
Maria Oliveira,Nordeste
"""

dados2 = """id_compra,produto_comprado,preço_do_produto
1,Smartphone,1500.00
3,Laptop,3000.00
5,Tablet,800.00
8,Headphones,150.00
10,Monitor,1200.00
12,Mouse,50.00
14,Keyboard,80.00
16,Speaker,200.00
19,Printer,300.00
20,Smartwatch,500.00
22,Keyboard,80.00
24,Tablet,800.00
26,Laptop,3000.00
28,Monitor,1200.00
30,Mouse,50.00
32,Speaker,200.00
34,Smartphone,1500.00
36,Headphones,150.00
39,Smartwatch,500.00
40,Printer,300.00
42,Smartphone,1500.00
44,Speaker,200.00
46,Mouse,50.00
48,Laptop,3000.00
50,Keyboard,80.00
52,Monitor,1200.00
54,Tablet,800.00
56,Speaker,200.00
59,Smartphone,1500.00
60,Smartwatch,500.00
62,Keyboard,80.00
64,Tablet,800.00
66,Laptop,3000.00
68,Monitor,1200.00
70,Mouse,50.00
72,Speaker,200.00
74,Smartphone,1500.00
76,Headphones,150.00
79,Smartwatch,500.00
80,Printer,300.00
82,Smartphone,1500.00
84,Speaker,200.00
86,Mouse,50.00
88,Laptop,3000.00
90,Keyboard,80.00
92,Monitor,1200.00
94,Tablet,800.00
96,Speaker,200.00
99,Smartphone,1500.00
100,Smartwatch,500.00
"""

# Convertendo as strings 
df1 = pd.read_csv(StringIO(dados1))
df2 = pd.read_csv(StringIO(dados2))

# Ajustando as colunas id_compra para terem o mesmo tipo 
df1['id_compra'] = pd.to_numeric(df1['id_compra'], errors='coerce').astype('Int64')
df2['id_compra'] = df2['id_compra'].astype('Int64')


df1 = df1.dropna(subset=['id_compra'])


df_compilado = pd.merge(df1, df2, on='id_compra')


df_agrupado = df_compilado.groupby('regiao')['preço_do_produto'].sum().reset_index()


# Identificando a região com a maior soma de vendas
regiao_top = df_agrupado.loc[df_agrupado['preço_do_produto'].idxmax()]


print(df_compilado.to_string(index=False))


# Exibindo o resultado
print(f"A região que trouxe mais dinheiro para a loja foi {regiao_top['regiao']} com um total de R$ {regiao_top['preço_do_produto']:,.2f}.")

