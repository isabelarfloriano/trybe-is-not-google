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
  <p>A seguir estão os exemplos para executar a aplicação, descritos no arquivo main.py. Para executar a aplicação, digite o seguinte comando: <code>python3 -m main</code></p>
    <ol>
    <li>Para criar uma instância da classe Queue e adicionar informações presentes nos arquivos TXT localizados no diretório 'statics':
      <dl>
        <dd><code>queue = Queue()</code></dd>
        <dd><code>process('statics/arquivo_teste.txt', queue)</dd>
        <dd><code>process('statics/nome_pedro.txt', queue)</code></dd>
        <dd><code>print('--> Primeiro Elemento da Fila:', queue.search(0))</code></dd>
        <dd><code>print('--> Segundo Elemento da Fila:', queue.search(1))</code></dd>
      </dl>
    </li>
    <li>Para localizar as informações por meio do índice usando a função 'file_metadata':
      <dl>
        <dd><code>file_metadata(queue, 0)</code> - Retorna o primeiro elemento</dd>
        <dd><code>file_metadata(queue, 1)</code> - Retorna o segundo elemento</dd>
        <dd><code>file_metadata(queue, 99)</code> - Retorna "Posição inválida"</dd>
      </dl>
    </li>
    <li>Para criar um relatório de busca de palavras presentes na instância usando as funções 'exists_word' e 'search_by_word':
      <dl>
        <dd><code>print(exists_word('adoção', queue))</code></dd>
        <dd>Retorno:
            [
              {
                'palavra': 'adoção',
                'arquivo': 'statics/arquivo_teste.txt,
                'ocorrencias': [
                    {'linha': 2},
                 ],
              },
            ]
        </dd>
        <dd><code>print(search_by_word('adoção', queue))</code></dd>
        <dd>Retorno:
            [
              {
                'palavra': 'adoção',
                'arquivo': 'statics/arquivo_teste.txt,
                'ocorrencias': [
                    {
                      'linha': 2,
                      'conteudo': 'é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga'
                    },
                 ],
              },
            ]
        </dd>
      </dl>
    </li>
    <li>Para remover as informações presentes na instância criada, use a função 'remove':
      <dl>
        <dd><code>remove(queue)</code> - Arquivo statics/arquivo_teste.txt removido com sucesso</dd>
        <dd><code>remove(queue)</code> - Arquivo statics/nome_pedro.txt removido com sucesso</dd>
        <dd><code>file_metadata(queue, 0)</code> - Retorna "Posição inválida"</dd>
      </dl>
    </li>
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
  <summary><strong>Detalhes sobre Teste Desenvolvido</strong></summary><br />
  <p>tests/priority_queue/test_priority_queue.py</p>
    <ul>
      <li>Implementação dos testes para a classe PriorityQueue</li>
      <li>Garante que arquivos com menos de 5 linhas são armazenados de forma prioritária na fila.</li>
    </ul>	
</details>
<details>
  <summary><strong>Detalhes sobre Classes Desenvolvidos</strong></summary><br />
  <p>ting_file_management/queue.py</p>
    <ul>
      <li>Classe criada para armazenamento de arquivos por filas</li>
    </ul>	
  <p>ting_file_management/file_management.py</p>
    <ul>
      <li>Função capaz de ler os arquivos TXT e retorna em formato de array/lista</li>
    </ul>
  <p>ting_file_management/file_process.py</p>
    <ul>
      <li>Função <code>process</code> - importa informações do arquivo TXT e adicionar na instância da Classe Queue informada</li>
      <li>Função <code>remove</code> - remove o primeiro arquivo presente na instância informada</li>
      <li>Função <code>file_metadata</code> - encontra um dado presente na instância atráves do index informado</li>
    </ul>
  <p>ting_word_searches/word_search.py</p>
    <ul>
      <li>Função <code>exists_word</code> - verifica existência de uma palavra em todos os arquivos processados, retornando um relatório simplificado</li>
      <li>Função <code>search_by_word</code> - verifica existência de uma palavra em todos os arquivos processados, retornando um relatório completo</li>
    </ul>
</details>
