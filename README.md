# FastAPI-REST

Exemplo de REST API em Python com FastAPI

## Instalação

O primeiro passo da instalação é criar um ambiente virtual no diretório do projeto.

**Comando para Windows:**
```
C:\Users\Name\FastAPI-REST> python -m venv venv
```

**Comando para Linux e OS X :**
```
$ python3 -m venv venv
```

Após isso é necessário ativar o ambiente virtual.

**Comando para Windows:**
```
C:\Users\Name\FastAPI-REST> venv\Scripts\activate
```

**Comando para Linux e OS X:**
```
$ source venv/bin/activate
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
3. Comentar as linhas indicadas no arquivo ```database.py```:
![image](https://user-images.githubusercontent.com/69127474/106213071-b097b900-61aa-11eb-9a04-5cb84f05e8d0.png)

## Uso
Com o ambiente virtual ativado digite o seguinte comando no terminal:
```
uvicorn app.main:app 
```
Para visualizar a documentação da API e testa-lá basta acessar o link:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Se tudo deu certo você deve visualizar a seguinte tela:
![docs](https://user-images.githubusercontent.com/69127474/106085512-1c244c80-60ff-11eb-8758-dd642a4463ac.PNG)


