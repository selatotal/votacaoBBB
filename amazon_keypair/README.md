Como acessar a instancia da Amazon?
===================================

IP da sua instância da Amazon: 52.5.97.186

Para acessar, use o arquivo de chave .pem deste diretorio.

$ chmod 400 selecaoWebmedia.pem

$ ssh -i selecaoWebmedia.pem ubuntu@52.5.97.186

O usuário ubuntu está no sudoers, é só fazer $ sudo su - que você vira root da máquina

Acessos
--------

As seguintes portas estão liberadas:
- 22 TCP
- 80 TCP
- 443 TCP
- 8080 TCP
- 8081 TCP

Se for necessário a liberação de mais alguma porta, é só pedir.
