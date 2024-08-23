README

Importei os arquivos em CSV para uma planilha sheets. 
Inserir um filtro nas colunas, com a finalidade de verificar erros de digitaçáo e possíveis incongruëncias
nos dados. 
Em uma nova página (integração_vendas) copiei o dados das compras compartilhadas e apliquei a função:
PROCV(chave_pesquisa; intervalo; índice; [classificação]).Onde a chave da pesquisa era o ID_COMPRA;
o intervalo consistiu nos dados da página pessoas; o índice é a coluna do dado que eu quero retornar;
enquanto a classificação, pode ser falso para correspondência exata (recomendado), ou verdadeiro para
correspondêcnia aproximada. 
Após a integração dos dados fiz uma tabela dinâmica que me mostrou a produção por região e produto.
No entanto para aplicar as funções aprendidas em sala de aula, trabalhei os dados na página resumo de vendas,
criando uma tabela com as regiões e uma área para a saída do total de vendas. Onde inseri a função:
SOMASE(intervalo; critério; [intervalo_da_soma]). utilizando como intervalo a coluna 
da região (na tabela integração_vendas); seguido da região específica requerida, como critério; e o intervalo de dados
da produção (R$).
Considerando a aplicação de tais funções em um conjunto de dados mais volumosos, utilizei a combinação das funções: ÍNDICE E
CORRESP, com o objetivo de obter a região com maior produção. Pedindo o valor máximo correspondente ao intervalo do índice.