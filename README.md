<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Lidando com arquivos, planilhas e módulos (Em desenvolvimento)

Turma Online On34 | Python | Semana 06 | 2024 | <a href="https://www.linkedin.com/in/jessmitiko/" target="_blank" rel="noopener noreferrer">Professora Jessica Mitiko</a>

### Instruções
Antes de começar, vamos organizar nosso setup.
* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)
* [Add outras intrucoes caso necessario] !!!

### Resumo
O que veremos na aula de hoje?
* [Parte 1: Introdução e Importação de CSV](#tema1)
* [Parte 2: Manipulação de Dados no Google Sheets](#tema2)
* [Parte 3: Funções de Pesquisa](#tema3)
* [Parte 4: ETL e Limpeza de Dados e Exportação](#tema4)

## Conteúdo
### Parte 1: Introdução e Importação de CSV    
1. [Formato de Arquivo CSV](#tema1-topico1)  
2. [O que é Planilha?](#tema1-topico2)
   * [Conceitos Básicos de Planilhas Eletrônicas](#tema1-topico2-subtopico-1)
<!-- 3. [Importação de CSV no Google Sheet](#tema1-topico3) -->
### <a name="tema2"></a>Parte 2: Manipulação de Dados no Google Sheets  
<!-- 1. [Uso de Filtros e Ordenação](#tema2-topico1) -->
1. [Uso de Fórmulas](#tema2-topico2)
   * [Fórmulas Básicas:](#tema2-topico2-subtopico1)
     * `SUM, MAX, MIN`
   * [Fórmulas Condicionais:](#tema2-topico2-subtopico2)  
     * `IF, COUNTIF, SUMIF`
   * [Funções de Texto:](#tema2-topico2-subtopico3)  
     * `CONCATENATE, SPLIT`  
### <a name="tema3"></a>Parte 3: Funções de Pesquisa  
1. [Funções de Pesquisa e Referência ](#tema3-topico1)
   * `VLOOKUP`
   * `HLOOKUP`
   * `MATCH`
   * `INDEX`
2. [Extra: Tabela Dinâmica](#tema3-topico2) !!!
### <a name="tema4"></a>Parte 4: ETL e Limpeza de Dados e Exportação  
1. [Importação do segundo arquivo CSV](#tema4-topico1)
2. [Limpeza de Dados e Transformação](#tema4-topico2)
   * [Identificação e remoção de duplicatas](#tema4-topico2-subtopico1)
   * [Uso de filtros para encontrar dados inconsistentes](#tema4-topico2-subtopico2)
3. [Importação do segundo arquivo CSV](#tema4-topico3)

### <a name="tema1"></a>Parte 1: Introdução e Importação de CSV  
#### <a name="tema1-topico1"></a>Formato de Arquivo CSV  
Um arquivo CSV (Comma-separated values) é um arquivo de texto com um formato específico que permite que dados sejam salvos no formato de uma **tabela estruturada**. Formato específico, pois usa vírgulas para separar valores e quebra de linha para separar linhas.  
!!!

#### <a name="tema1-topico2"></a>O que é Planilha?  
- <u>Definição</u>: Uma Planilha (Eletrônica) é um programa/aplicação utilizado para processamento, organização, análise e armazenamento de dados em formato tabular (linhas e colunas). Cada célula pode conter dados numéricos ou textuais, ou o resultado de fórmulas/cálculos. Também chamamos de planilha o próprio documento que organiza os dados em tabelas formadas por linhas e colunas.  
- <u>Uso</u>: Utilizada para armazenar, organizar e analisar dados de forma eficiente.  

##### <a name="tema1-topico2-subtopico-1"></a>**Conceitos Básicos de Planilhas Eletrônicas**  
- **Página**
  * <u>Definição</u>: Uma planilha pode conter várias páginas ou abas, cada uma representando um conjunto separado de dados dentro do mesmo arquivo.   
  * <u>Visualização</u>: As páginas são acessíveis através das abas na parte inferior da janela do Google Sheets.
  * <u>Exemplo</u>: Em um arquivo de planilha de uma escola, você pode ter uma página para cada turma.  

- **Linha**
  * <u>Definição</u>: Linhas são as divisões horizontais de uma planilha. Cada linha é identificada por um número, começando em 1 no topo.  
  * <u>Uso</u>: Cada linha geralmente representa um registro único ou uma entrada de dados.  
  * <u>Exemplo</u>: Cada linha pode representar um aluno diferente em uma planilha de notas.  

- **Coluna**
  * <u>Definição</u>: Colunas são as divisões verticais de uma planilha. Cada coluna é identificada por uma letra, começando com `A` à esquerda.   
  * <u>Uso</u>: Cada coluna contém um tipo específico de informação.  
  * <u>Exemplo</u>: Em uma planilha de notas, a coluna A pode conter os nomes dos alunos, a coluna B as notas de Matemática, etc.  

- **Célula**
  * <u>Definição</u>: A célula é a interseção de uma linha com uma coluna. Cada célula é identificada por sua referência de célula, que combina a letra da coluna com o número da linha (por exemplo, A1).   
  * <u>Uso</u>: Cada célula pode conter um único dado, como um número, texto ou fórmula.  
  * <u>Exemplo</u>: A célula C2 pode conter a nota do primeiro bimestre do primeiro aluno da lista.  

- **Intervalo**
  * <u>Definição</u>: Um intervalo é uma seleção de múltiplas células adjacentes em uma planilha, definidas pelas células inicial e final (por exemplo, A1).   
  * <u>Uso</u>: Intervalos são usados para aplicar fórmulas e funções a múltiplas células simultaneamente.  
  * <u>Exemplo</u>: O intervalo C2:E11
pode representar todas as notas dos alunos nos três bimestres.  

<!-- #### <a name="tema1-topico3"></a>Importação de CSV no Google Sheet  
  - Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  - Donec erat mauris, laoreet in tortor vel
  - Nunc ante massa, dictum eget justo eget, feugiat tincidunt.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam leo nibh, tempus sed rhoncus et, ultrices vitae orci. Donec erat mauris, laoreet in tortor vel, eleifend suscipit nibh. Mauris pharetra dui quis turpis rutrum blandit. -->


### <a name="tema2"></a>Parte 2: Manipulação de Dados no Google Sheets  
#### <a name="tema2-topico2"></a>Uso de Fórmulas
* <a name="tema2-topico2-subtopico1"></a>Fórmulas Básicas
  * [`SUM`](https://support.google.com/docs/answer/3093669?hl=pt-BR): Soma os valores em um intervalo de células.  
  Fórmula (PT-BR): `SOMA(valor1; [valor2; ...])`  
  Fórmula (EN): `SUM(valor1, [valor2, ...])`  
  Exemplo: `=SOMA(F2:H2)` - Soma os valores das células F2, G2 e H2.

  * [`AVERAGE`](https://support.google.com/docs/answer/3093615?hl=pt-BR): Calcula a média dos valores em um intervalo de células.  
  Fórmula (PT-BR): `MÉDIA(valor1; [valor2; ...])`  
  Fórmula (EN): `AVERAGE(valor1, [valor2, ...])`  
  Exemplo: `=MÉDIA(C2:E2)` - Calcula a média dos valores nas colunas C, D e E na linha 2.

  * [`MAX`](https://support.google.com/docs/answer/3094013?hl=pt-BR): Retorna o maior valor em um intervalo de células.  
  Fórmula (PT-BR): `MÁXIMO(valor1; [valor2; ...])`  
  Fórmula (EN): `MAX(valor1, [valor2, ...])`  
  Exemplo: `=MÁXIMO(C2:C11)` - Encontra o valor máximo nas células de C2 a C10.

  * [`MIN`](https://support.google.com/docs/answer/3094017?hl=pt-BR): Retorna o menor valor em um intervalo de células.  
  Fórmula (PT-BR): `MÍNIMO(valor1; [valor2; ...])`  
  Fórmula (EN): `MIN(valor1, [valor2, ...])`  
  Exemplo: `=MÍNIMO(A2:A100;B2:B100;4;26)` - Encontra o valor mínimo entre a coluna A e B da linha 2 até 100, e os valores 4 e 26. 

* <a name="tema2-topico2-subtopico2"></a>Fórmulas Condicionais
  * [`IF`](https://support.google.com/docs/answer/3093364?hl=pt-BR): Retorna um valor se uma condição for verdadeira e outro valor se for falsa.  
  Fórmula (PT-BR): `SE(expressao_logica; valor_se_verdadeiro; valor_se_falso)`  
  Fórmula (EN): `IF(expressao_logica, valor_se_verdadeiro, valor_se_falso)`  

  * [`AND`](https://support.google.com/docs/answer/3093301?hl=pt-BR): Verifica se **todas** as condições são verdadeiras.  
  Fórmula (PT-BR): `E(expressao_logica1; [expressao_logica2; ...])`  
  Fórmula (EN): `AND(expressao_logica1, [expressao_logica2, ...])`  

  * [`OR`](https://support.google.com/docs/answer/3093306?hl=pt-BR): Verifica se **pelo menos uma** condição é verdadeira.   
  Fórmula (PT-BR): `OU(expressao_logica1; [expressao_logica2; ...]) `  
  Fórmula (EN): `OR(expressao_logica1, [expressao_logica2, ...])`  

  Exemplo: `=SE(E(F2>=6; J2<10); "Aprovado"; "Reprovado")` - Retorna "Aprovado" ou "Reprovado" baseado nas condições, para os valores na linha 2.  

  * [`COUNTIF`](https://support.google.com/docs/answer/3093480?hl=pt-BR): Conta o número de células que atendem a um critério.   
  Fórmula (PT-BR): `CONT.SE(intervalo; critério)`  
  Fórmula (EN): `COUNTIF(intervalo, critério)` 

  * [`SUMIF`](https://support.google.com/docs/answer/3093583?hl=pt-BR): Soma as células em um intervalo que atendem a um critério.   
  Fórmula (PT-BR): `SOMASE(intervalo; critério; [intervalo_soma])`  
  Fórmula (EN): `SUMIF(intervalo, critério, [intervalo_soma])` 

  Exemplo: `CONT.SE(K2:K11; "Aprovado")` - Retorna "Aprovado" a quantidade de valores "Aprovado" presentes no intervalo de K2 à K11.  

* <a name="tema2-topico2-subtopico3"></a>Funções de Texto
  * [`CONCATENATE`](https://support.google.com/docs/answer/3094123?hl=pt-BR): Junta textos de várias células em uma única célula.  
  Fórmula (PT-BR): `CONCATENAR(string1; [string2; ...])`  
  Fórmula (EN): `CONCATENATE(string1, [string2, ...])`  
  Exemplo: `=CONCATENATE(A2, " ", B2)` - Junta o valor da célula A2 e B2 separados por um espaço.  

  * [`SPLIT`](https://support.google.com/docs/answer/3094136?hl=pt-BR): Divide o texto de uma célula em várias células usando um delimitador.  
  Fórmula (PT-BR): `SPLIT(texto; delimitador; [dividir_por_cada], [remover_texto_vazio])`  
  Fórmula (EN): `SPLIT(texto, delimitador, [dividir_por_cada], [remover_texto_vazio])`  
  Exemplo: `=SPLIT("Estou separando esses valores"; " ")` - Divide o texto com o delimitador de espaço. 


### <a name="tema3"></a>Parte 3: Funções de Pesquisa  
#### <a name="tema3-topico1"></a>Funções de Pesquisa e Referência
  * [`PROCV`](https://support.google.com/docs/answer/3093318?hl=pt-BR): A função `PROCV` (Pesquisa Vertical) procura um valor em uma coluna e retorna um valor na mesma linha de uma coluna especificada.  
  Fórmula (PT-BR): `PROCV(chave_pesquisa, intervalo, índice, [é_ordenado])`  
  Fórmula (EN): `VLOOKUP(chave_pesquisa, intervalo, índice, [é_ordenado])`  
  Exemplo: Procurar o nome de um produto com base na aba de produtos:  
  `=PROCV("P001"; produtos!A2:C101; 2; FALSO)`  
  Isso procura o código "P001" na coluna A da aba de produtos e retorna o nome do produto na aba e na coluna correspondente.  
  **Nota**: `PROCV` só pode ser usado quando o valor de pesquisa está à esquerda do atributo desejado a ser retornado.  

  * [`PROCH`](https://support.google.com/docs/answer/3093375?hl=pt-BR): A função `PROCH` (Pesquisa Horizontal) é semelhante ao `PROCV`, mas procura um valor em uma linha e retorna um valor na mesma coluna de uma linha especificada.  
  Fórmula (PT-BR): `PROCH(chave_pesquisa, intervalo, índice, [é_ordenado])`  
  Fórmula (EN): `HLOOKUP(chave_pesquisa, intervalo, índice, [é_ordenado])`  

  * [`CORRESP`](https://support.google.com/docs/answer/3093378?hl=pt-BR): A função CORRESP procura um valor específico em um intervalo e retorna a posição relativa desse valor no intervalo.  
  Fórmula (PT-BR): `CORRESP(chave_pesquisa; intervalo_pesquisa; [tipo_correspondência])`  
  Fórmula (EN): `MATCH(chave_pesquisa; intervalo_pesquisa; [tipo_correspondência])` 

  * [`ÍNDICE`](https://support.google.com/docs/answer/3098242?hl=pt-BR): A função ÍNDICE retorna o valor de uma célula em uma tabela ou intervalo com base nos números da linha e da coluna fornecidos.  
  Fórmula (PT-BR): `ÍNDICE(intervalo; linha; [coluna])`  
  Fórmula (EN): `INDEX(intervalo; linha; [coluna])`  

  **Combinação de `ÍNDICE` e `CORRESP`**: A combinação das funções `ÍNDICE` e `CORRESP` permite procurar valores em qualquer lugar de uma tabela, independentemente da posição relativa dos dados.  

  **Nota**: `ÍNDICE` e `CORRESP` podem ser usados independentemente de onde o valor de pesquisa está localizado em relação ao atributo desejado a ser retornado.

#### <a name="tema3-topico2"></a>Extra: Tabela Dinâmica  
!!!

### <a name="tema4"></a>Parte 4: ETL e Limpeza de Dados e Exportação 
#### Topico4
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam leo nibh, tempus sed rhoncus et, ultrices vitae orci. Donec erat mauris, laoreet in tortor vel, eleifend suscipit nibh. Mauris pharetra dui quis turpis rutrum blandit. Nunc tempor libero tortor, ac commodo erat porttitor ut. Donec vitae orci arcu. Nunc felis mi, maximus a turpis a, mollis pulvinar enim. Vivamus aliquam ante dui, a blandit massa rutrum et. Etiam hendrerit gravida ultrices.


***
### Exercícios 
* [Exercicio para sala](https://github.com/mflilian/repo-example/tree/main/exercicios/para-sala)
* [Exercicio para casa](https://github.com/mflilian/repo-example/tree/main/exercicios/para-casa)
* [Exercícios Extras](https://www.hashtagtreinamentos.com/exercicios-de-excel-2)

### Material da aula 

### Links Úteis
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)


<p align="center">
Desenvolvido com :purple_heart:  
</p>

