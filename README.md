<br />
<p align="center">
  <h3 align="center">Gerenciador de Equipamentos e Manutenções</h3>

  <p align="center">
    Academia do Programadores 2021
    <br />
  </p>
</p>

<details open="open">
  <summary>Tabela de Conteudos</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o projeto</a>
      <ul>
        <li>
            <a href="#construido-com">Construido com</a>
        </li>
        <li>
            <a href="#recursos">Recursos</a>
        </li>
      </ul>
    </li>
    <li>
      <a href="#executando">Executando</a>
      <ul>
        <li>
          <a href="#pré-requisitos">Pré-requisitos</a>
        </li>
        <li>
          <a href="#instalando">Instalando</a>
        </li>
      </ul>
    </li>
    <li>
      <a href="#estrutura-do-projeto">Estrutura do projeto</a>
      <ul>
        <li>
          <a href="#diretorios-e-arquivos">Diretorios e Arquivos</a>
        </li>
        <li>
          <a href="#relações-de-dados">Relações de Dados</a>
        </li>
      </ul>
    </li>
    <li>
      <a href="#rotas">Rotas</a>
      <ul>
        <li>
          <a href="#pagina-inicial">Pagina Inicial</a>
        </li>
        <li>
          <a href="#equipamento">Equipamento</a>
        </li>
        <li>
          <a href="#chamado-manutenção">Chamado Manutenção</a>
        </li>
      </ul>
    </li>
  </ol>
</details>


## Sobre o projeto

![Pagina Inicial](/md_images/tela-index.png)

Este projeto foi feito para a 2° etapa do processo de avaliação da Academia do Programador.

Esta aplicação te permite gerenciar equipamentos e seus chamados para manutenções, oferendo uma interface simples e rápida para isso.


### Construido com

Linguagens de programação usadas e suas bibliotecas:

- [Python](https://www.python.org/)
    - [SQLAlchemy](https://www.sqlalchemy.org/)
    - [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
    - [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)
- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
    - [Materialize](https://materializecss.com/)

E como Banco de Dados
- [SQLite](https://www.sqlite.org/index.html)

### Recursos

Você pode fazer as seguintes coisas nesta aplicação:

- Equipamentos
    - Registrar novos Equipamentos
    - Editar Equipamentos 
    - Excluir Equipamentos
    - Ver Equipamentos registrados
    - Ver Chamados de Manutenção que estão ligados a um determinado Equipamento
    - Ir diretamente à tela de edição de um Chamado ligado a um determinado Equipamento
    ![Tela de Equipamentos](/md_images/tela-equipamentos.png)
    ![Tela de Equipamento modal dos Chamados](/md_images/tela-equipamentos-modal-chamado.png)
    
- Chamados De Manutenção
    - Registrar novos Chamados especificando a qual equipamento ele está ligado
    - Editar Chamados
    - Excluir Chamados
    - Ver Chamados registrados
    - Ver o Equipamento que está ligado a um determinado Chamado
    - Ir diretamento à tela de edição de um Equipamento ligado a um determinado Chamado
    ![Tela de Chamados](/md_images/tela-chamado.png)
    ![Tela de Chamados modal dos Equipamentos](/md_images/tela-chamado-modal-equipamento.png)

- Reponsividade
    - A aplicação é totalmente responsiva, permitindo assim o seu uso em desde telas pequenas a grandes
    ![Tela Mobile do Equipamentos](/md_images/tela-mobile-equipamentos.png)
    ![Tela Mobile do Equipamentos](/md_images/tela-mobile-equipamentos-modal-chamado.png)
    ![Tela Mobile do Equipamentos](/md_images/tela-mobile-editar-equipamento.png)

## Executando

### Pré requisitos
- Python
  - Windows: 
    - Acesse [Download Python](https://www.python.org/downloads/) faça o download e instale-o
  - Linux:
    - Ubuntu:
    ```sh
    sudo apt install python3
    ```
    - Arch:
    ```sh
    sudo pacman -S python3
    ```

- Python pip
  - Windows:
  ```sh
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  py get-pip.py
  ```
  - Linux:
  ```sh
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python get-pip.py
  ```

- Virtualenvwrapper (opcional):
  ```sh
  pip install -g virtualenvwrapper
  ```

- SQLite
  - Windows:
    - Acesse [Download SQLite](https://www.sqlite.org/download.html) faça o download e instale-o
  - Linux:
    - Ubuntu:
    ```sh
    sudo apt install sqlite3
    ```
    - Arch:
    ```sh
    sudo pacman -S sqlite3
    ```

### Instalando

1. Clone o repositorio
```sh
git clone https://github.com/erikborella/AcademiaDoProgramador2021.git
```

2. Entre na pasta no repositorio
```sh
cd AcademiaDoProgramador2021
```

3. Crie um ambiente virtual python usando o Virtualenvwrapper  (Opcional)
```sh
mkvirtualenv academiaDoProgramador2021
```

4. Instale todas as dependecias Python
```sh
pip install -r requirements.txt
```

5. Construa as tabelas do Banco de Dados
```sh
python db_utils.py -m
```

6. Rode o servidor
```sh
python main.py
```

7. Acesse a página inicial da aplicação no seu navegador no endereço: [localhost:5000](http://localhost:5000)

## Estrutura do Projeto
Este projeto foi desenvolvido com base no padrão Model-View-Controller(MVC).

- Model: Gerencia o comportamento dos dados
  - Corresponde ao arquivo [models.py](https://github.com/erikborella/AcademiaDoProgramador2021/blob/main/models.py)

- View: É onde ocorre a representação dos dados
  - Corresponde a todas as pastas templates/. encontradas no diretorio [raiz](https://github.com/erikborella/AcademiaDoProgramador2021) e nas subpastas da pasta [views](https://github.com/erikborella/AcademiaDoProgramador2021/tree/main/views)

- Controller: É o que faz a ponte entre o Model e o View
  - Corresponde ao arquivo [main.py](https://github.com/erikborella/AcademiaDoProgramador2021/blob/main/main.py) e a todos os arquivos .py nas subpastas [views](https://github.com/erikborella/AcademiaDoProgramador2021/tree/main/views)
![Modelo MVC](/md_images/mvc.png)


### Diretorios e Arquivos
Segue uma breve explicação do que cada diretorio e arquivo significam:
- Diretorios:

  - [database/](https://github.com/erikborella/AcademiaDoProgramador2021/tree/main/database) : é onde ficam os arquivos para as persistencia dos dados

  - [static/](https://github.com/erikborella/AcademiaDoProgramador2021/tree/main/static) : Ficam todos os arquivos estaticos
    - [css/](https://github.com/erikborella/AcademiaDoProgramador2021/tree/main/static/css) : Ficam os arquivos .css e onde cada view tem a sua propria subpasta
    - [js/](https://github.com/erikborella/AcademiaDoProgramador2021/tree/main/static/js) : Ficam os arquivos .js e onde cada view tem a sua propria subpasta
    - [img/](https://github.com/erikborella/AcademiaDoProgramador2021/tree/main/static/img) : Ficam todas as imagens

  - [templates/](https://github.com/erikborella/AcademiaDoProgramador2021/tree/main/templates) : Ficam o template base e a view para a pagina inicial

  - [views/](https://github.com/erikborella/AcademiaDoProgramador2021/tree/main/views) : Onde ficam todo o conjunto de arquivos de templates e seu controladores. Segue o seguinte padrão:
    - nome-da-view/
      - templates/
      - `nome-da-view.py`

- Arquivos:

  - [app_creator.py](https://github.com/erikborella/AcademiaDoProgramador2021/blob/main/app_creator.py): Configura todas as dependencias e telas necessarias para a aplicação e cria uma aplicação Flask
  
  - [config.py](https://github.com/erikborella/AcademiaDoProgramador2021/blob/main/config.py): Contem todas as configurações usadas pelo Flask

  - [db_utils.py](https://github.com/erikborella/AcademiaDoProgramador2021/blob/main/db_utils.py): Biblioteca simples para migrar as tabelas do banco de dados e mostrá-las

  - [extensions.py](https://github.com/erikborella/AcademiaDoProgramador2021/blob/main/extensions.py): É declarado todas as variveis das extensões

  - [forms.py](https://github.com/erikborella/AcademiaDoProgramador2021/blob/main/forms.py): É declarado todos os modelos de formulario usados pelo Flask-WTF, que servem para a validação dos formularios

  - [main.py](https://github.com/erikborella/AcademiaDoProgramador2021/blob/main/main.py): Contem o controller da Pagina Incial e também é por onde o servidor é iniciado

  - [models.py](https://github.com/erikborella/AcademiaDoProgramador2021/blob/main/models.py): É declarado todos os modelos usados pelo SQLAlchemy, que manipula o banco de dados

  - [utils.py](https://github.com/erikborella/AcademiaDoProgramador2021/blob/main/utils.py): Contem funções comuns utilizadas por toda a aplicação

  - [requirements.txt](https://github.com/erikborella/AcademiaDoProgramador2021/blob/main/requirements.txt): É declarado todas as dependencias Python


### Relações de Dados
O Bando de Dados é composto por duas tabelas:

* Equipamento:
  
  Tipo | Nome
  -----|-----
  Int (pk) | id
  String(100) | nome
  String(100) | numero_de_serie
  Float | preco_aquisisao
  Date | data_fabricacao
  String(100) | fabricante

* Chamado Manutenção:

  Tipo | Nome
  -----|-----
  Int (pk) | id
  String(100) | titulo
  String(500) | descricao
  Int (fk) | equipamento_id
  Date | data_de_abertura

  Onde Equipamento faz uma relação de 1:N para Chamado Manutenção

  ![Modelo Entidade-Relacionamento](/md_images/er.png)

## Rotas

### Pagina Inicial
  - /
    - get:
      - Mostra a Pagina Inicial

### Equipamento
  - /equipamentos/
    - get:
      - Mostra a tela dos equipamentos

  - /equipamentos/registrar
    - get:
      - Mostra a tela para registrar um Equipamento
    - post:
      - Cadastra um novo Equipamento
      - Formulario:

        tipo | nome
        -----|-----
        String | nome
        Float | preco
        String | numero_de_serie
        String | data_de_fabricacao
        String | fabricante

  - `/equipamentos/editar/<int:id>`
    - get:
      - Mostra a tela para editar o Equipamento com o id passado na url
    - post:
      - Edita o Equipamento com os novos dados
      - Formulario:

        tipo | nome
        -----|-----
        String | nome
        Float | preco
        String | numero_de_serie
        String | data_de_fabricacao
        String | fabricante

  - `/equipamentos/excluir/<int:id>`
    - get:
      - Exclui o Equipamento com o id passado na url junto com todos os Chamados relacionados a ele

### Chamado Manutenção
  - /chamados/
    - get:
      - Mostra todos os Chamados de Manutenção Cadastrados

  - /chamados/registrar/
    - get:
      - Mostra a tela para registro de um novo Chamado de Manutenção
    - post:
      - Registra um novo Chamado de Manutenção
      - Formulario:

        tipo | nome
        -----|-----
        String | titulo
        String | descricao
        String | data_de_abertura
        Int | equipamento_id

  - `/chamados/editar/<int:id>`
    - get:
      - Mostra a tela para editar um Chamado com o id passado na url
    - post:
      - Edita o Chamado com os novos dados
      - Formulario:

        tipo | nome
        -----|-----
        String | titulo
        String | descricao
        String | data_de_abertura
        Int | equipamento_id

  - `/chamados/excluir/<int:id>`
    - get:
      - Exclui o Chamado com o id passado por parametro