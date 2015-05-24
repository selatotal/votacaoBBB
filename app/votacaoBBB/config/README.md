# Arquivo de Configuração

Exemplo do arquivo de configuração:

```
# Configuration
DATABASE = 'db/bbbvoting.db'
DEBUG = True
SECRET_KEY = 'votacaoBBB'
USERNAME = 'admin'
PASSWORD = 'admin'
TESTING = True
PORT = 80
IP_BIND = 127.0.0.1

RECAPTCHA_SITE_KEY = "6Le4LQcTAAAAADxEqxZps9myTRk1YcDstYOr8axM"
RECAPTCHA_SECRET_KEY = "6Le4LQcTAAAAAGM0F93CoZag-MNrKLm3BZexkzsp"
```

Abaixo a descrição de cada uma das chaves de configuração do arquivo app.cfg

## DATABASE
Localização do arquivo da base de dados SQLite3

## DEBUG
Ativa ou desativa o modo de depuração do Flask. Mais detalhes em http://flask.pocoo.org/docs/0.10/quickstart/#debug-mode

## SECRET_KEY
Chave para criptografia dos dados de sessão utilizados no Flask. Mais detalhes em http://flask.pocoo.org/docs/0.10/quickstart/#sessions

## USERNAME
Username habilitado a acessar a interface de administração

## PASSWORD
Senha do username habilitado a acessar a interface de administração

## PORT
TCP/IP Listen Port do servidor

## IP_BIND
Endereço TCP/IP para o bind do listener do servidor

## RECAPTCHA_SITE_KEY
Site key do recaptcha utilizado para exibição do RECAPTCHA na página de votação. Mais detalhes em https://developers.google.com/recaptcha/docs/start 

## RECAPTCHA_SECRET_KEY
Secret key do recaptcha utilizado para exibição do RECAPTCHA na página de votação. Mais detalhes em https://developers.google.com/recaptcha/docs/start
