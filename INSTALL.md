###Baixar os fontes do GIT
```
git clone https://github.com/SelecaoGlobocom/TalesViegas.git
```

###Setup Servidor

Entrar no diretório com os fontes e executar o arquivo configure com permissao de root
```
cd TalesViegas
sudo ./configure
```
Opcionalmente, pode ser feita a configuração com os comandos abaixo:

```
apt-get install -y git sqlite3 python python-pip
pip install flask flask-recaptcha
sqlite3 app/votacaoBBB/db/bbbvoting.db < app/votacaoBBB/db/schema.sql
```

Necessária a correção da configuração para o TCP/IP bind do serviço.
* Abrir o arquivo app/votacaoBBB/config/app.cfg
* Alterar o parâmetro IP_BIND para o endereço IP do Listener
* Opcionalmente, alterar a porta onde o serviço estará atendendo, no parâmetro PORT

Caso o servidor seja diferente de 'localhost', '172.30.0.246' ou '52.5.97.186', será necessário configurar uma nova chave do Recaptcha ou me comunicar para que eu habilite o IP na mesma chave que tem hoje. Mais detalhes na [documentação da configuração](app/votacaoBBB/config).

###Execução do Servidor

Para executar o servidor é necessário executar o seguinte comando

```
sudo ./run.sh
```

### URLs de Acesso

Página de votação: http://52.5.97.186/
Página de administração: http://52.5.97.186/admin

Após o servidor está no ar, a página de votação pode ser acessada diretamente na raiz do servidor.
Para a página de administração, pode ser acessada através da URL relativa /admin
O usuário e senha padrão podem ser consultados no arquivo de configuração (por padrão é admin/admin)
