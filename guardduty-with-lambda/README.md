# GuardDuty With Lambda
### Apresentação
Para monitorar e contornar vulnerabilidades apontadas pelo GuardDuty, desenvolvi este projeto para que, quando uma vulnerabilidade for detectada, o AWS EventBridge executará uma função Lambda. 
**Por exemplo:** GuardDuty detectou uma vulnerabilidade relacinada a Unauthorized Access, o AWS EventBridge identifica a ameça e executa uma função Lambda.

## 🛑 Problematização
Foi identificado que uma instância EC2 está se comunicando com um IP malicioso, além de estar sendo, também, alvo de PortScans. Nossa tarefa é isolar está instância
em seu próprio grupo de segurança (removendo acesso SSH) e criando um _snapshot_ do volume anexado nesta instância.

## ❗ Explicação
Antes de começarmos o passo a passo, vamos começar explicando a existência de arquivo dentro deste diretório: <br>
→ *[Event-Bridge.json](event-bridge.json)* : Este arquivo hospeda o código JSON que iremos utilizar na criação de uma regra do Event Bridge.

→ *[lambda_Function.py](lambda_function.py)* : Nesse arquivo, possuí o código da função Lambda.

## 🔧 Passo a passo
> Serviços estudados neste projeto: VPC; Security Groups; EC2 + EBS; AWS GuardDuty; AWS Event Bridge; AWS Lambda;

> Atente-se: neste projeto foi utilizado o sistema operacional Amazon Linux 2, a partir de uma EC2.

1. Criação da função Lambda _Instance-Isolator_
