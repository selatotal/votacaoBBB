###Setup Servidor
* sudo apt-get install pip
* pip install flask
* pip install flask-recaptcha

###Setup Aplicacao
* sqlite3 app/votacaoBBB/db/bbbvoting.db < app/votacaoBBB/db/schema.sql

###Execução do Servidor
cd app/votacaoBBB
run.sh