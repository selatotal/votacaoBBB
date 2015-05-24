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

===============================
####Performance Test:

###### ab -n 100 -c 10 http://127.0.0.1:5000/vote/1
Concurrency Level:      10
Time taken for tests:   0.324 seconds
Complete requests:      100
Failed requests:        0
Non-2xx responses:      100
Total transferred:      42200 bytes
HTML transferred:       22300 bytes
Requests per second:    309.02 [#/sec] (mean)
Time per request:       32.360 [ms] (mean)
Time per request:       3.236 [ms] (mean, across all concurrent requests)
Transfer rate:          127.35 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:     3   31   4.7     32      35
Waiting:        3   31   4.7     32      34
Total:          4   31   4.6     32      35

###### ab -n 1000 -c 100 http://127.0.0.1:5000/vote/1

Concurrency Level:      100
Time taken for tests:   3.620 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Total transferred:      422000 bytes
HTML transferred:       223000 bytes
Requests per second:    276.21 [#/sec] (mean)
Time per request:       362.039 [ms] (mean)
Time per request:       3.620 [ms] (mean, across all concurrent requests)
Transfer rate:          113.83 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.6      0       3
Processing:     5  341  82.2    324     450
Waiting:        4  341  82.2    324     450
Total:          7  341  81.7    324     450

###### ab -n 10000 -c 100 http://127.0.0.1:5000/vote/1

Concurrency Level:      100
Time taken for tests:   38.203 seconds
Complete requests:      10000
Failed requests:        0
Non-2xx responses:      10000
Total transferred:      4220000 bytes
HTML transferred:       2230000 bytes
Requests per second:    261.76 [#/sec] (mean)
Time per request:       382.033 [ms] (mean)
Time per request:       3.820 [ms] (mean, across all concurrent requests)
Transfer rate:          107.87 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       2
Processing:     4  380  79.8    341     719
Waiting:        3  380  79.8    340     718
Total:          6  380  79.8    341     719

###### ab -n 10000 -c 150 http://127.0.0.1:5000/vote/1

Não passou na máquina local

###### ab -n 10000 -c 120 http://127.0.0.1:5000/vote/1

Concurrency Level:      120
Time taken for tests:   41.655 seconds
Complete requests:      10000
Failed requests:        0
Non-2xx responses:      10000
Total transferred:      4220000 bytes
HTML transferred:       2230000 bytes
Requests per second:    240.07 [#/sec] (mean)
Time per request:       499.863 [ms] (mean)
Time per request:       4.166 [ms] (mean, across all concurrent requests)
Transfer rate:          98.93 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       3
Processing:     4  495 127.4    482    1131
Waiting:        4  495 127.3    482    1125
Total:          8  496 127.3    483    1132

###Configuração de dependencias
sudo ./configure

###Execução do Servidor
sudo ./run.sh