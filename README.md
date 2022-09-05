# Gestão Escolar

Como uma prática de desenvolvimento é interessante criar as telas para depois desenvolver a lógica dentro do Python.

> NOTA: todo HTML é implementado dentro do diretório 'templates'

## Bootstrap - Flask

O Flask possuí uma extensão para desenvolver interfaces modernas e responsiva. Para este desenvolvimento é utilizado o framework Bootstrap, que atualmente é mais utilizado para no desenvolvimento de aplicações web. 

Para instalar a extenesão é necessário instalar o pacote flask-bootstrap. Segue o comando para instação:

```
pip install flask-bootstrap
```

Após a instalação feita é necessário registrar a extensão à variável da aplicação (app). Segue um exemplo:

```
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

...

```
