# Projeto TING (Trybe is not Google)!	:red_circle::yellow_circle::computer::green_circle::large_blue_circle:

Foi desenvolvida uma aplicação em Python que simula um algoritmo de indexação de documentos semelhante ao do Google, com capacidade para detectar ocorrências em arquivos TXT.

<details>
  <summary><strong>Objetivos de prática</strong></summary><br />
    <ul>
      <li>Manipular Pilhas</li>
      <li>Manipular Deque</li>
      <li>Manipular Nó & Listas Ligadas</li>
      <li>Manipular Listas Duplamente Ligadas</li>
    </ul>
</details>
<details>
  <summary><strong>Rodando Localmente a Aplicação</strong></summary><br />
  
  <p>Para executar a aplicação e os testes, siga os passos abaixo:</p>
  <ol>
    <li>Clone o projeto.</li>
    <li>Abra o terminal e navegue até a raiz do projeto.</li>
    <li>Crie o ambiente virtual com o comando <code>python3 -m venv .venv</code>.</li>
    <li>Ative o ambiente virtual com o comando <code>source .venv/bin/activate</code>.</li>
    <li>Instale as dependências com o comando <code>python3 -m pip install -r dev-requirements.txt</code>.</li>
    <li>Para executar todos os testes, execute o comando <code>python3 -m pytest</code> na raiz do projeto.</li>
  </ol>
</details>
<details>
  <summary><strong>Estrutura do Projeto</strong></summary><br />

  ```
.
├──statics
│   ├──🔸arquivo_teste.csv
│   ├──🔸arquivo_teste.txt
│   ├──🔸nome_pedro.txt
│   ├──🔸novo_paradigma_globalizado-min.txt
│   └──🔸novo_paradigma_globalizado.txt
├──tests
│   ├──priority_queue
│   │   ├──🔹test_priority_queue.py
│   │   └──🔸__init__.py
│   └──🔸__init__.py
├──ting_file_management
│   ├──🔸__init__.py
│   ├──🔸abstract_queue.py
│   ├──🔹file_management.py
│   ├──🔹file_process.py
│   ├──🔸priority_queue.py
│   └──🔹queue.py
├──ting_word_searches
│   ├──🔸__init__.py
│   └──🔹word_search.py
├──🔸dev-requirements.txt
├──🔹main.py
├── 🔸pyproject.toml
├── 🔹README.md
├── 🔸requirements.txt
├── 🔸setup.cfg
└── 🔸setup.py
  
    Legenda:
  🔸Arquivos de propriedade intelectual da Trybe
  🔹Arquivos desenvolvidos por mim
  ```
</details>
<details>
  <summary><strong>Detalhes sobre Testes Desenvolvidos</strong></summary><br />
  <p>tests/product/test_product.py</p>
    <ul>
      <li>Implementação dos testes para a classe Product</li>
      <li>Verificao correto preenchimento dos seguintes atributos:</li>
            <ul>
                 <li>id (int)</li>
                 <li>nome_da_empresa (string)</li>
                 <li>nome_do_produto (string)</li>
                 <li>data_de_fabricacao (string)</li>
                 <li>data_de_validade (string)</li>
                 <li>numero_de_serie (string)</li>
                 <li>instrucoes_de_armazenamento (string)</li>
             </ul>
      <li>Garante a criação de um novo produto com todos os atributos corretamente preenchidos.</li>
    </ul>	
  <p>tests/product_report/test_product_report.py</p>
    <ul>
      <li>Implementação dos testes para a a criação do relatório presente na classe Product</li>
      <li>Garante a formulação de uma frase construída com as informações do produto, que será muito útil para etiquetarmos o estoque.</li>
      <li>Exemplo da frase:</li>
            <ul>
                 <li>O produto `farinha` fabricado em `01-05-2021` por `Farinini` com validade até `02-06-2023` precisa ser armazenado `ao abrigo de luz`.</li>
             </ul>
    </ul>
  <p>tests/report_decorator/test_report_decorator.py</p>
    <ul>
      <li>Implementação dos testes para a classe ColoredReport</li>
      <li>Garante o retorno do relatório devidamente colorido:
            <ul>
                 <li>🟩 Verde:</li>
                      <ul>
                          <li>"Data de fabricação mais antiga:"</li>
                          <li>"Data de validade mais próxima:"</li>
                          <li>"Empresa com mais produtos:"</li>
                      </ul>
                 <li>🟦 Azul: As datas</li>
                 <li>🟥 Vermelho: Nome da empresa com mais produtos</li>
             </ul>
       </li>
    </ul>	
</details>
<details>
  <summary><strong>Detalhes sobre Classes Desenvolvidos</strong></summary><br />
  <p>inventory_report/reports/simple_report.py</p>
    <ul>
      <li>Classe para gerar a versão simplificada do relatório</li>
    </ul>	
  <p>inventory_report/reports/complete_report.py</p>
    <ul>
      <li>Classe para gerar a versão completa do relatório	inventory_report/reports/complete_report.py</li>
    </ul>
  <p>inventory_report/inventory/inventory.py</p>
    <ul>
      <li>Classe para gerar os relatório a partir de arquivos</li>
    </ul>
  <p>inventory_report/importer/importer.py</p>
    <ul>
      <li>Classe abstrata para aplicar o padrão de projeto Strategy</li>
    </ul>
  <p>inventory_report/inventory/inventory_iterator.py</p>
    <ul>
      <li>Refatoração da classe Inventory para aplicar o padrão de projeto Iterator</li>
    </ul>
</details>
