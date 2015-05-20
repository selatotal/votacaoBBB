###Setup Servidor
* sudo apt-get install pip
* pip install flask

###Setup Aplicacao
* sqlite3 app/votacaoBBB/db/bbbvoting.db < app/votacaoBBB/db/schema.sql
* export VOTACAOBBB_SETTINGS=config/app.cfg 
