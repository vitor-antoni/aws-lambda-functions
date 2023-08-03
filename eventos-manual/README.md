# Eventos Manual
## Criação e configuração de eventos de forma manual

Quando uma função lambda é acionada por um serviço, o atributo "event" é populado de acordo com o serviço que realizou a invocação. Por exemplo o SQS, envia informações do "corpo/body" da mensagem para o "event".

Mas também, é possível nós mesmo manipular esse atributo event.