## Tales Viegas

=====================
#### O Problema

O problema que você deve resolver é o problema da votação do paredão do BBB em versão WEB com HTML/CSS/Javascript + backend usando a linguagem de programação e ferramentas open-source da sua preferência.

Nesse repositório você encontra algumas imagens necessárias para implementação da parte web: uma com o desenho da tela e outra com um sprite de imagens que você talvez deseje usar.

O paredão do BBB consiste em uma votação que confronta dois ou mais integrantes do programa BBB, simulando o que acontece na realidade durante uma temporada do BBB. A votação é apresentada em uma interface acessível pela WEB onde os usuários optam por votar em uma das opções apresentadas. Uma vez realizado o voto, o usuário recebe uma tela com o comprovante do sucesso do seu voto e um panorama percentual dos votos por candidato até aquele momento.

============================
#### Regras de negócio

1. Os usuários podem votar quantas vezes quiserem, independente da opção escolhida. Entretanto, a produção do programa não quer receber votos oriundos de uma máquina, apenas votos de pessoas.
2. A votação é chamada na TV em horário nobre, com isso, é esperado um enorme volume de votos concentrados em um curto espaço de tempo. Esperamos ter um teste disso, e por razões práticas (capacidade da nossa VM t2.micro), podemos considerar 100 votos/seg como baseline de performance deste teste.
3. A produção do programa gostaria de ter URLs (a serem especificadas) para consultar: o total de geral votos, o total por participante e o total de votos por hora de cada paredão. Estas URLs precisam estar documentadas em algum lugar do projeto.
4. Além disso, os organizadores do BBB são exigentes. Portanto a interface do produto é algo bem importante. Organize seu tempo para que esse item também tenha a atenção mínima esperada.
