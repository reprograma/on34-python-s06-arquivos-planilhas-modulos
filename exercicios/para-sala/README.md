# Exercício de Sala 🏫  

## ETL com Google Sheets e python

- **Explicação do exercício**: Vamos explorar os dados de acessos ao nosso site para os meses de Abril e Maio, iremos tratar esses dados no Google Sheets e depois unificarmos ambos já devidamente tratados utilizando o módulo `csv` com python.

  Em resumo faremos:
  - A importação dos CSVs em um Google Sheets;
  - Exploração e limpeza desses dados dentro da nossa planilha;
  - Exportação dos nossos dados já devidamente tratados no formato CSV;
  - União dos 2 CSVs utilizando o módulo `csv` + python.


**Como realizar a leitura de um CSV com python**:
   ```python
   import csv

   with open('produtos.csv', newline='', encoding='utf-8') as csvfile:
       leitor = csv.reader(csvfile)
       for linha in leitor:
           print(linha)
   ```

**Como realizar a escrita dos dados em um CSV**:
   ```python
   import csv

   funcionarios = [
       [1, 'Ana', 'Financeiro'],
       [2, 'Carlos', 'TI'],
       [3, 'Beatriz', 'RH']
   ]

   with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
       escritor = csv.writer(csvfile)
       escritor.writerow(['id', 'nome', 'departamento'])
       escritor.writerows(funcionarios)
   ```

---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
