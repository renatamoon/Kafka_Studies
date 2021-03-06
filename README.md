# Kafka_Studies

### Links:

https://www.redhat.com/pt-br/topics/integration/what-is-apache-kafka <br>
https://kafka-python.readthedocs.io/en/master/<br>
https://medium.com/azure-na-pratica/apache-kafka-kafdrop-docker-compose-montando-rapidamente-um-ambiente-para-testes-606cc76aa66 <br>
https://www.youtube.com/watch?v=o5yviW6QSrE&list=PL5aY_NrL1rjt_AZxj11kQjiTNLGg4ZaZA&index=1 <br>

# O QUE É O APACHE KAFKA

O Apache Kafka é uma plataforma de transmissão de dados que é capaz de publica, sobscrever e processar fluxos de registros em tempo real. Foi desenvolvido para processar um fluxo de dados provenientes de diversas fontes e entrgá-los a varios clientes. Em resumo, movimenta 
volumes imensos de dados não apenas de um ponto A até o ponto B, mas tbem de A a Z e para qualquer outro ponto simultaneamente. <br>
É uma alternativa de sistemas de mensagens empresariais tradicionais. Inicialmente foi uma solução que o Linkedin criou para processar milhões de mensagens simultaneamente, mas agora, virou uma solução open source.<br>


## INTEGRAÇÃO ASSINCRONA COM O APACHE KAFKA

Eles tornaram os desenvolvedores mais ágeis ao reduzir as dependências, como as camadas de banco de dados compartilhado. No entanto, as aplicações distribuídas que estão sendo criadas pelos desenvolvedores ainda precisam de algum tipo de integração para compartilhar dados. Uma opção de integração muito usada, conhecida como método síncrono, utiliza interfaces de programação de aplicações (APIs) para compartilhar dados entre usuários diferentes.

## QUANDO USAR O APACHE KAFKA

O Apache Kafka é incorporado a pipelines de transmissão que compartilham dados entre sistemas e/ou aplicações, bem como a sistemas e aplicações que consomem esses dados. O Apache Kafka é compatível com vários casos de uso, em que alta produtividade e escalabilidade são fatores vitais. Isso significa que os dados são disponibilizados mais rapidamente aos usuários, o que é uma vantagem para os casos de uso que exigem disponibilidade de dados em tempo real, como operações de TI e comércio eletrônico.<br>

O Apache Kafka é capaz de lidar com milhões de pontos de dados por segundo, o que faz dessa solução a ideal para desafios que envolvem big data. No entanto, o Kafka também é útil para empresas que no momento não operam em cenários com uso tão extremo de dados.<br>

#### USO DO KAFKA NAS OPERAÇÕES DE TI

- Operações de TI
As equipes operações de TI dependem sobretudo de dados. E elas precisam ter acesso rápido a eles. Essa é a única maneira de manter sites, aplicações e sistemas ativos e em funcionamento permanentemente. O Apache Kafka é uma excelente solução para as funções de operações de TI porque elas dependem da coleta de dados de variadas fontes, como os sistemas de monitoramento, alerta e geração de relatórios, as plataformas de gerenciamento de registros e as atividades de monitoramento de sites.

- E-commmerce

O comércio eletrônico é uma oportunidade em crescimento para uso do Apache Kafka, pois ele pode processar dados do tipo cliques de página, curtidas, pesquisas, pedidos, carrinhos de compra e inventários.

- Internet das Coisas

De acordo com as previsões do Gartner, a IoT incluirá mais de 20 bilhões de dispositivos até 2020. O valor da IoT está nos dados acionáveis gerados pela grande variedade de sensores. O Apache Kafka foi desenvolvido para oferecer escalabilidade capaz de processar os imensos volumes de dados provenientes da IoT.

### FLUXO DE DADOS DENTRO DO KAFKA 

![image](https://user-images.githubusercontent.com/87100340/152412099-691d640f-7b51-43b7-826f-181f9252ee66.png)


#### BROKERS

Um broker Apache Kafka permite que os consumidores busquem mensagens por tópico, consumer group, partição e offset. Brokers fazem parte de um cluster compartilhando informações entre si direta ou indiretamente, sendo que um dos brokers atua como controlador (controller). 

No exemplo abaixo temos 2 brokers. O Kafka sempre tentará distribuir as partições entre os topicos. Se os dados do broker A cair, ainda conseguirão puxar os dados pelo broker B e C. 

![image](https://user-images.githubusercontent.com/87100340/152412133-5d843132-81cd-4bd5-bbc9-0f9e584a6763.png)


- REPLICAÇÃO DE BROKERS:

Imagina se o broker A para de funcionar, então no de replicação, o broker continua funcionando devido ao Broker C ter a partição 1 funcionando.

![image](https://user-images.githubusercontent.com/87100340/152412217-6d9e3d92-5477-4746-bb88-b9a15066eaa8.png)


- DELIVERY DE MENSAGENS – como funciona a entrega de mensagens pelo Kafka. 

As formas de entrega de mensagens, como informa abaixo, são enviadas se não tiver uma key, ela armazena de forma aleatória (primeira mensagem na partição 1, a segunda mensagem na partição 2, a terceira mensagem na partição 3). Agora, se a mensagem tiver uma key chamada SALES, ela entrará sempre na mesma partição pré-definida. 

![image](https://user-images.githubusercontent.com/87100340/152412289-0e4bbb2d-c029-4473-8c03-229199b3a25f.png)


O Kafka faz o armazenamento das mensagens no modelo FIFO (first in first Out), porém, a ordem de leitura das mensagens pode não ser a mesma. Pois cada mensagem pode estar em partições diferentes, desta forma, não sabemos a ordem. Então, as mensagens estarão desordenadas. 

Porém, existem casos em que as mensagens devem estar ORDENADAS. Se tivermos que ter essa ordenação, deveremos sempre que mandar a Key, para que ela sempre seja mandada para a mesma partição. Ou seja, se mandarmos a chave, teremos sempre ordenação nas mensagens, se não, nunca teremos mensagens ordenadas para depois fazer a leitura.

#### PARTITION LEADERSHIP 

Quais são as partições líderes dos nossos brokers. 

Exemplo: As partições abaixo são líderes (cor azul), as partições que não estão em azul, são followers. O que uma partição líder significa? Significa que toda vez que alguém consumir uma mensagem, ela terá que consumir da partição líder.  

Exemplo 2: se o broker A cair, onde a sua partição A caiu, então o Kafka manterá a partição 1 líder para o broker B. 

![image](https://user-images.githubusercontent.com/87100340/152412314-c01ba8fc-ce19-4ce7-a99d-3852e2e572a6.png)


#### PRODUCER

![image](https://user-images.githubusercontent.com/87100340/152412368-1f50fbd1-ca46-4c5a-977d-ec7d94c41748.png)


Delivery Guarantees – caso você queira que haja garantia de entrega de mensagens, no caso, teremos 3 opções. 

ACK  0 (none) – onde você prefere velocidade, onde pode perder uma mensagem ou outra; 

ACK 1 (Leader) - onde você terá velocidade moderada, mas quer uma garantia de entrega moderada tbem, e não total. Ou seja, você tem chance de perda de mensagens no processo. 

ACK –1 (ALL) - Garantia total de entrega de mensagens, porém a velocidade não é a mesma. O Kafka demora muito para processar as mensagens. 

Ainda falando de garantia de entrega:

![image](https://user-images.githubusercontent.com/87100340/152412405-fc18660a-9565-4604-adcc-6edf2fa75a6c.png)


*at most: lose some messages – tem uma performance boa, mas não alta 

*at least once  - quer dizer que a performance é alta, mas não alta, e pode ser que haja duplicação de mensagens; 

*Exacly once: Worst Performance – que é a que tem a mais baixa performance de todas.

#### IDEMPOTENT PRODUCERS

Se setamos que os produtores (produtores de dados) não serão idempotentes (settar como OFF), não podemos duplicar a mensagem. Se settamos como idempotentes (ON), ele consegue ver se as mensagens são ou não duplicadas, e consegue descartar as mensagens. Com isso também consegue ver o timestamp (data e hora) de envio de mensagens e consegue fazer a ordenação. 

![image](https://user-images.githubusercontent.com/87100340/152412462-2db13fda-0711-47ca-9986-47c3ac0ec2b3.png)


- PRODUCERS – que criam as mensagens 

- CONSUMMERS – programa feito com qualquer linguagem de programação que leem e consumirão as mensagens com o Apache Kafka. Eles ficam rodando pra sempre para ler essas mensagens (While == True). 

![image](https://user-images.githubusercontent.com/87100340/152412487-5e624184-5b14-406b-bcf2-504093110953.png)

![image](https://user-images.githubusercontent.com/87100340/152412550-cc4b992c-f93e-451a-b2d1-6d270f39c04a.png)


### KAFKA CONNECT

Pega infos de um lugar, para outro lugar. Funciona basicamente como um ecossistema.
Exemplo: queremos pegar infos vindas de um ERP salesforce ou banco de dados (MYsql), ao inves de codificar tudo isso e colocar pra ler no Kafka, ou selecionar os dados do Mysql, oKafka connect é que temos diversos conectores, que fazem esses serviços de variados meios (mysql, twitter, etc). Ele pega essas infos e publicam nos tópicos.  

O kafka connect não é o Kafka, ele age mais ou menos como um cluster, e ai repassa essas infos que são pegadas de algum lugar (mysql, api etc) e ele joga as infos no Kakfa. 

![image](https://user-images.githubusercontent.com/87100340/152412586-8e182909-814c-43d3-bd6e-6f5fa02b6187.png)


- DATA CAPABILITY – qual o padrão da mensagem. Se criamos uma API, ela tem um formato de leitura e processamento. Temos o nome, e-mail e telefone, só que o consumidor sabe que tem esses campos para processamento de mensagens.  

Só que de repente, o sistema se tornou internacional, gerando números de telefone, nome e e-mail diferentes do normal que devemos aceitar. O sistema não está preparado para aceitar tais informações, ou seja, vai quebrar e dar problema. Ou seja, essa versão de API não está preparada para este tipo de info, porém, pode ser que a outra versão esteja preparada pra isso.

![image](https://user-images.githubusercontent.com/87100340/152412650-f7563db6-f23a-485d-b551-99ff09e724d1.png)

![image](https://user-images.githubusercontent.com/87100340/152412686-77a88c55-f524-45ac-85df-be99f1bab241.png)


Apache AVRO - é um json que recebe os tipos de descrição de mensagem, ai ele fica gravado no Schema Registry, que fica no cache e se torna padrão.

![image](https://user-images.githubusercontent.com/87100340/152412714-d1cfaad7-e88c-44eb-8505-ab239255b99a.png)


Kafka streams é uma lib feita em java. Garante o exactly once. Trabalha nesse processo de processamento em real time. 

Exemplo: tem um conector com o Kafka connect com o banco de dados Mongodb, quando a mensagem chega no topico, ai vou conectar o Kafka Streams e le a mensagem recebida pelo kafka streams e transforma os dados da melhor forma possivel. Uma vez que foi tratado, ela foi processada. 

FLUXO > manda uma mensagem pro Kafka, o kafka processa a mensagem, joga a mensagem novamente pro Kafka e essa mensagem pode ser consumida por qualquer consumidor.  
![image](https://user-images.githubusercontent.com/87100340/152412781-8f4daa46-fac7-4e09-896c-78b0f3387039.png)


Esse segundo exemplo: Uma mensagem que está sendo produzida por um sistema, a mensagem passa pelo Kafka onde ao lado tem dois streams rodando (em java) e faz a transformação dessa mensagem para o padrão que queremos, jogo a mensagem novamente ao Kafka, e o consumidor (programa em qualquer linguagem) pode fazer o consumo novamente dessas mensagens. 

PORQUE O STREAMS é tão importante: consegue pega os dados e processando em tempo real, consegue agrupar, tirar média dos dados.  


### KSQLDB - Rodar comandos SQL nas filas. 

A rest API do ksqlDB – faz o envio de dados granularizados (selecionados) para uma pessoa selecionada, sem passar o Kafka para essa pessoa. Ou seja, da pra criar uma Rest API especifica com os dados pra uma pessoa, sem ela ter acesso ao Kafka inteiro.  

![image](https://user-images.githubusercontent.com/87100340/152412814-56609b51-1d90-462a-b19c-fb38b5295925.png)


### COMANDOS PARA USO DE IMAGEM DOCKER DO KAFKA

#### INSTALAÇÃO DO DOCKER COMPOSE
- `sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose`

- `sudo chmod +x /usr/local/bin/docker-compose`

- `docker-compose --version`

- Arquivo `docker-compose.yml` deve estar dentro da aplicação.

- O serviço zookeeper será criado a partir da imagem `confluentinc/cp-zookeeper`, representando a instância do ZooKeeper;
- Já o serviço kafka fará uso da imagem `confluentinc/cp-kafka`, correspondendo a uma instância do Apache Kafka acessível externamente na porta 9092 (e internamente para a network broker-kafka na porta 29092). Este container também referencia a instância do ZooKeeper em depends_on;

- Para usar os comandos abaixo, devemos estar no mesmo nível onde o arquivo `docker-compose.yml` está.

- `docker-compose up -d` criará um network e os containers esperados, realizando inclusive o download de imagens se as mesmas nao existirem na maquina;

- `docker network ls` podemos verificar que a rede broker-kafka foi iniciada com sucesso;

- `docker-compose ps` mostrará que os containers do Kafka (porta 9092), do Kafdrop (porta 19000) e do ZooKeeper foram gerados;

- TESTANDO O AMBIENTE: Um teste de acesso via browser ao Kafdrop `(http://localhost:19000)` exibirá a tela inicial desta solução;

#### DANDO UM DOCKER COMPOSE:

Podemos olhar as portas com as quais o kafka faz acesso. Desta forma, para o nosso sistema gerador de usuarios, temos sempre que usar a 9092 dentro do nosso código.

![image](https://user-images.githubusercontent.com/87100340/152453782-f7aa7e9a-d862-43e7-8c51-6719295734e0.png)


#### IMAGEM DO KafDrop rodando na porta 19000:

![image](https://user-images.githubusercontent.com/87100340/152453684-9026c5cd-446a-4eac-bd6a-25ddaa9f2786.png)

Entrando dentro do tópico onde mostra os usuários registrados:

![image](https://user-images.githubusercontent.com/87100340/152453650-77ed90ad-60d4-481f-89a0-2740e0d287ec.png)


## USANDO O KAFKA PURO DENTRO DO TERMINAL

- docker exec -it kafka-fullcycle_kafka_1 bash
