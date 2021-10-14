# DRF-VueJS - API Simples - Certificado

Projeto para um teste prático feito em Django REST Framework (Sqlite) + VueJs (Vuetify)

## Desenvolvimento

Estas são as etapas para executar o projeto:

### Requisitos

Python 3.9=>
Node.js

#### Backend

1. Instalar o gerenciador de pacotes [Poetry](https://python-poetry.org/docs/):
   ```sh
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
   ```
2. Entrar no diretório da aplicação de backend
   ```sh
   cd Teste-Certificado/Backend/
   ```
3. Usar o Poetry para instalar as dependências Python do projeto:
   ```sh
   poetry install
   ```
4. Para ativar um ambiente virtual do Poetry:
   ```sh
   poetry shell
   ```
5. Para alternar entre ambientes virtuais que foram criados:
   ```sh
   poetry env use python3.9
   ```
6. Inicializar o banco de dados
   ```sh
   python manage.py migrate
   ```
7. Carregar dados iniciais do banco (obrigatório caso não aixe diretamente o banco de dados)
   ```sh
   python manage.py loaddata groups.json
   ```
8. Executar a aplicação
   ```sh
   python manage.py runserver
   ```

#### Frontend

1. Entrar no diretório da aplicação de frontend
```sh
cd Teste-Certificado/Frontend/
```
2. Instalar os pacotes node necessários
```sh
npm install
```
ou
```sh
yarn install
```
3. Iniciar a aplicação
```sh
npm run serve
```
ou
```sh
yarn serve
```
