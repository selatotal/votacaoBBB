## Considerações

===============================
#### Cronograma Macro
1. Protótipo 20/05 (tela e votação)
2. Segurança da votação (controle por Cookie, IP/Via, recaptcha caso seja possível utilizar) 22/05
3. URLs de administração 25/05

===============================
#### Cronograma Detalhado
1. Montagem layout tela votação - término em 15/05
2. Montagem layout tela resultado - término em 19/05
3. Elaboração modelo URLs - término em 19/05
4. Criação testes Flask
5. Criação modelos Flask - término em 19/05
6. Criação métodos Flask - término em 19/05
7. Integração tela/votação - término em 19/05
8. Criação testes Flask administração
9. Criação métodos Flask administração
10. Telas administração

===============================
#### Fluxo

Página estática de votação.
/

Escolha do Participante
/vote/1
/vote/2

Incrementa contador

===============================
####Objetos:

Participante
- Quantidade Votos
- Nome

Votacao
- Participantes
- Data-Hora Fim

Votos
- Data-Hora
- Participante