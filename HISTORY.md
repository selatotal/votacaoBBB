## Arquitetura

===============================
#### Backend em Flask
* Framework web em linguagem Python - http://flask.pocoo.org/
* Decisão por fazer a aplicação utilizando Flask, por possibilitar a criação de um servidor leve, sem a necessidade de todas as bibliotecas de MVC do Django/Rails/etc.
* Utilização do Jinja como linguagem de template Web - http://jinja.pocoo.org/
* Utilização de biblioteca flask-recaptcha para facilitar o uso do Recaptcha - https://github.com/mardix/flask-recaptcha/

### Front-End
* Ideia inicial de não usar Frameworks JavaScript e CSS para o desenvolvimento.
* Assim, as páginas de votação não usam nada de JQuery/Angular/Sass/Less.
* Entretanto, a ideia inicial foi alterada apenas para:
:* Utilização da biblioteca JavaScript D3 (http://d3js.org/), para facilitar a criação de gráficos SVG na página de resultados
:* Utilização da biblioteca Countdown.Js (http://countdownjs.org/), para facilitar a criação do contador da página de resultados
* Para a ferramenta de administração, como não tinha um template pré-definido, foi utilizado o BootStrap (http://getbootstrap.com/)

### Melhorias Futuras
* Automatização do processo de build e configuração
:* Utilização do Jenkins para deploy da aplicação
:* Configurar automaticamente o endereço IP do parâmetro de BIND.
* Colocar o NGinx na frente do serviço Flask e executar via WSGI.
:* Possibilita melhorar a capacidade de atendimento
:* Retira do Flask a entrega dos arquivos estáticos
* Utilizar um supervisor para monitoramento do daemon
:* Se colocar o NGinx, talvez não seja necessári
:* Mas se não colocar, é necessário para que, caso o serviço caia, possa ser reiniciado
* Troca do SQLite3 para um NoSQL
:* Creio que melhoraria a capacidade de atendimento, principalmente para o caso de mais de um servidor (neste caso seria praticamente obrigatório)

===============================
#### Fluxo

Página estática de votação.
/

Escolha do Participante
/vote/1
/vote/2

Incrementa contador


===============================
####Performance Test:

```
ab -n 100 -c 10 http://127.0.0.1:5000/vote/1

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
```

```
ab -n 1000 -c 100 http://127.0.0.1:5000/vote/1

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
```

```
ab -n 10000 -c 100 http://127.0.0.1:5000/vote/1

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
```

```
ab -n 10000 -c 150 http://127.0.0.1:5000/vote/1

Não passou na máquina local
```

```
ab -n 10000 -c 120 http://127.0.0.1:5000/vote/1

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
```

===============================
###Configuração de dependencias
sudo ./configure

===============================
###Execução do Servidor
sudo ./run.sh


