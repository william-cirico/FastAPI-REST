# FastAPI-REST

Exemplo de REST API em Python com FastAPI

## Instalação

O primeiro passo da instalação é criar um ambiente virtual no diretório do projeto:

Comando para Windows:
```
C:\Users\Name\FastAPI-REST> python -m venv venv
```

Comando para Linux e OS X :
```
$ python -m venv venv
```

Após isso é necessário ativar o ambiente virtual:

Comando para Windows:
```
C:\Users\Name\FastAPI-REST> venv\Scripts\activate
```

Comando para Linux e OS X:
```
$ source myvenv/bin/activate
```

Com seu ambiente virtual ativado você deve instalar os pacotes necessários para o projeto:
```
pip install -r requirements.txt
```

A API está configurada para salvar os dados em um banco de dados sqlite. Porém, se você desejar
utilizar o PostgreSQL basta seguir os seguintes passos:

1. Criar um banco de dados no PostgreSQL
2. Criar um arquivo ```.env``` na raiz do projeto e incluir a seguinte linha:
```
SQLALCHEMY_DATABASE_URL = "postgresql://usuario:senha@server/nome_banco"
``` 
3. Comentar a linha 9 no arquivo ```database.py```:
![database](https://user-images.githubusercontent.com/69127474/106083936-16793780-60fc-11eb-8e49-48d5c80fff0d.PNG)

## Uso
Com o ambiente virtual ativado digite o seguinte comando no terminal:
```
uvicorn app.main:app 
```
Para visualizar a documentação da API e testa-lá basta acessar o link:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


