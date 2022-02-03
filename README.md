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

### COMANDOS PARA USO DO KAFKA

- Creating User: `sudo adduser kafka`
- Adding Kafka Use to the group: `sudo adduser kafka sudo`
- Loging to the Kafka account: `su -l kafka`