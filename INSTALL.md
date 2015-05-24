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

###Execução do Servidor

Para executar o servidor é necessário executar o seguinte comando

```
sudo ./run.sh
```

O servidor está configurado para realizar o bind do Ip na porta 80, para o IP 127.0.0.1 (localhost).
Pode ser necessário alterar o arquivo de configuração para o IP do servidor que está executando (para a VM disponibilizada foi necessário alterar o IP)
Outro ponto que pode ser necessário é alterar a chave do Recaptcha para votação, caso não seja acessado pelos endereços localhost, 52.5.97.186 ou 172.30.0.246.
A explicação das chaves de configuração podem ser verificadas abaixo

### URLs de Acesso

Página de votação: http://52.5.97.186/
Página de administração: http://52.5.97.186/admin

Após o servidor está no ar, a página de votação pode ser acessada diretamente na raiz do servidor.
Para a página de administração, pode ser acessada através da URL relativa /admin
O usuário e senha padrão podem ser consultados no arquivo de configuração (por padrão é admin/admin)



