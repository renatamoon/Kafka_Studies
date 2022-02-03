# Kafka_Studies
<hr>

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

#### BROKERS

Um broker Apache Kafka permite que os consumidores busquem mensagens por tópico, consumer group, partição e offset. Brokers fazem parte de um cluster compartilhando informações entre si direta ou indiretamente, sendo que um dos brokers atua como controlador (controller). 

No exemplo abaixo temos 2 brokers. O Kafka sempre tentará distribuir as partições entre os topicos. Se os dados do broker A cair, ainda conseguirão puxar os dados pelo broker B e C. 

- REPLICAÇÃO DE BROKERS:

Imagina se o broker A para de funcionar, então no de replicação, o broker continua funcionando devido ao Broker C ter a partição 1 funcionando.

- DELIVERY DE MENSAGENS – como funciona a entrega de mensagens pelo Kafka. 

As formas de entrega de mensagens, como informa abaixo, são enviadas se não tiver uma key, ela armazena de forma aleatória (primeira mensagem na partição 1, a segunda mensagem na partição 2, a terceira mensagem na partição 3). Agora, se a mensagem tiver uma key chamada SALES, ela entrará sempre na mesma partição pré-definida. 

O Kafka faz o armazenamento das mensagens no modelo FIFO (first in first Out), porém, a ordem de leitura das mensagens pode não ser a mesma. Pois cada mensagem pode estar em partições diferentes, desta forma, não sabemos a ordem. Então, as mensagens estarão desordenadas. 

Porém, existem casos em que as mensagens devem estar ORDENADAS. Se tivermos que ter essa ordenação, deveremos sempre que mandar a Key, para que ela sempre seja mandada para a mesma partição. Ou seja, se mandarmos a chave, teremos sempre ordenação nas mensagens, se não, nunca teremos mensagens ordenadas para depois fazer a leitura.

#### PARTITION LEADERSHIP 

Quais são as partições líderes dos nossos brokers. 

Exemplo: As partições abaixo são líderes (cor azul), as partições que não estão em azul, são followers. O que uma partição líder significa? Significa que toda vez que alguém consumir uma mensagem, ela terá que consumir da partição líder.  

Exemplo 2: se o broker A cair, onde a sua partição A caiu, então o Kafka manterá a partição 1 líder para o broker B. 

#### PRODUCER

Delivery Guarantees – caso você queira que haja garantia de entrega de mensagens, no caso, teremos 3 opções. 

ACK  0 (none) – onde você prefere velocidade, onde pode perder uma mensagem ou outra; 

ACK 1 (Leader) - onde você terá velocidade moderada, mas quer uma garantia de entrega moderada tbem, e não total. Ou seja, você tem chance de perda de mensagens no processo. 

ACK –1 (ALL) - Garantia total de entrega de mensagens, porém a velocidade não é a mesma. O Kafka demora muito para processar as mensagens. 

Ainda falando de garantia de entrega:

*at most: lose some messages – tem uma performance boa, mas não alta 

*at least once  - quer dizer que a performance é alta, mas não alta, e pode ser que haja duplicação de mensagens; 

*Exacly once: Worst Performance – que é a que tem a mais baixa performance de todas.

#### IDEMPOTENT PRODUCERS

Se setamos que os produtores (produtores de dados) não serão idempotentes (settar como OFF), não podemos duplicar a mensagem. Se settamos como idempotentes (ON), ele consegue ver se as mensagens são ou não duplicadas, e consegue descartar as mensagens. Com isso também consegue ver o timestamp (data e hora) de envio de mensagens e consegue fazer a ordenação. 

- PRODUCERS – que criam as mensagens 

- CONSUMMERS – programa feito com qualquer linguagem de programação que leem e consumirão as mensagens com o Apache Kafka. Eles ficam rodando pra sempre para ler essas mensagens (While == True). 


### KAFKA CONNECT

Pega infos de um lugar, para outro lugar. Funciona basicamente como um ecossistema.
Exemplo: queremos pegar infos vindas de um ERP salesforce ou banco de dados (MYsql), ao inves de codificar tudo isso e colocar pra ler no Kafka, ou selecionar os dados do Mysql, oKafka connect é que temos diversos conectores, que fazem esses serviços de variados meios (mysql, twitter, etc). Ele pega essas infos e publicam nos tópicos.  

O kafka connect não é o Kafka, ele age mais ou menos como um cluster, e ai repassa essas infos que são pegadas de algum lugar (mysql, api etc) e ele joga as infos no Kakfa. 

- DATA CAPABILITY – qual o padrão da mensagem. Se criamos uma API, ela tem um formato de leitura e processamento. Temos o nome, e-mail e telefone, só que o consumidor sabe que tem esses campos para processamento de mensagens.  

Só que de repente, o sistema se tornou internacional, gerando números de telefone, nome e e-mail diferentes do normal que devemos aceitar. O sistema não está preparado para aceitar tais informações, ou seja, vai quebrar e dar problema. Ou seja, essa versão de API não está preparada para este tipo de info, porém, pode ser que a outra versão esteja preparada pra isso.

Apache AVRO - é um json que recebe os tipos de descrição de mensagem, ai ele fica gravado no Schema Registry, que fica no cache e se torna padrão.

Kafka streams é uma lib feita em java. Garante o exactly once. Trabalha nesse processo de processamento em real time. 

Exemplo: tem um conector com o Kafka connect com o banco de dados Mongodb, quando a mensagem chega no topico, ai vou conectar o Kafka Streams e le a mensagem recebida pelo kafka streams e transforma os dados da melhor forma possivel. Uma vez que foi tratado, ela foi processada. 

FLUXO > manda uma mensagem pro Kafka, o kafka processa a mensagem, joga a mensagem novamente pro Kafka e essa mensagem pode ser consumida por qualquer consumidor.  

Esse segundo exemplo: Uma mensagem que está sendo produzida por um sistema, a mensagem passa pelo Kafka onde ao lado tem dois streams rodando (em java) e faz a transformação dessa mensagem para o padrão que queremos, jogo a mensagem novamente ao Kafka, e o consumidor (programa em qualquer linguagem) pode fazer o consumo novamente dessas mensagens. 

PORQUE O STREAMS é tão importante: consegue pega os dados e processando em tempo real, consegue agrupar, tirar média dos dados.  


### KSQLDB - Rodar comandos SQL nas filas. 

A rest API do ksqlDB – faz o envio de dados granularizados (selecionados) para uma pessoa selecionada, sem passar o Kafka para essa pessoa. Ou seja, da pra criar uma Rest API especifica com os dados pra uma pessoa, sem ela ter acesso ao Kafka inteiro.  

### COMANDOS PARA USO DO KAFKA

- Creating User: `sudo adduser kafka`
- Adding Kafka Use to the group: `sudo adduser kafka sudo`
- Loging to the Kafka account: `su -l kafka`