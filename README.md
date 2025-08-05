# Funções AWS Lambda
### Apresentação
Olá, amigos. Tudo bem? Espero que sim. 😁

Estou começando a trabalhar com a AWS Cloud e seria incrível poder compartilhar minha experiência e conhecimentos aqui no GitHub. Logo, através deste repositório,
estarei compartilhando códigos de funções usando o AWS Lambda Service.
> Datalhe: também haverá um pouco de Shell Scripting. 🤭

Se surgir alguma dúvida ou sugestão, sinta-se à vontade em comentar. Procurarei monitorar diariamente este repositório (ou a medida que for desenvolvendo meus projetos
pessoais).

## 🚀 Projetos
#### Abaixo, você pode conferir um breve resumo sobre cada projeto contido neste repositório:

> Caso tiver interesse em utilizar estas funções, atente-se em atualizar os atributos das variáves de acordo com suas informações e necessidades.

##### [MAIS NOVO - MAIS ANTIGO]

- **Removing-S3-Objects** <br>
A função lista todos os objetos no bucket especificado, calcula a data de corte (que é a data atual menos um dia) e itera sobre a lista de objetos para identificar e excluir aqueles que foram modificados antes da data de corte. Essencialmente, o script atua como uma rotina de manutenção para remover arquivos com mais de 24 horas, ajudando a gerenciar o armazenamento e o custo do bucket S3.

- **Item-Dynamodb** <br>
Função AWS Lambda que interage com o serviço Amazon DynamoDB. A função cria um cliente para o DynamoDB e, em seguida, define um dicionário chamado itemData que representa um novo item a ser inserido. Esse dicionário inclui a chave primária (primaryKey), a chave de ordenação (sortKey) e outros atributos. Por fim, o método put_item é chamado para inserir esse item na tabela do DynamoDB especificada por <tableName>. O código serve como um modelo básico para adicionar novos registros a uma tabela DynamoDB a partir de uma função Lambda.

- **Importing-Aws-Layers** <br>
Automação de instalação das dependências externas (requests e suas bibliotecas relacionadas) em uma pasta local (python/) e depois comprime essa pasta em um arquivo .zip. Este arquivo .zip é exatamente o formato necessário para ser carregado na AWS e registrado como uma Lambda Layer, permitindo que múltiplas funções Lambda compartilhem o mesmo conjunto de bibliotecas sem que elas precisem ser incluídas no pacote de implantação de cada função individualmente.

- **Eventos-Manual** <br>
Um código com estrutura muito simples simples, projetado para receber dados de um evento, processá-los e retornar uma resposta. A função extrai os valores para nome, sobrenome e idade do objeto de evento, imprime uma saudação personalizada no log do CloudWatch e, em seguida, retorna esses mesmos dados em um dicionário como a resposta da função. É um exemplo fundamental de como uma função Lambda pode ser usada para receber entrada, executar uma lógica básica e produzir uma saída estruturada.

- **Deploying-Instances** <br>
Automação do AWS Lambda que automatiza o processo de implantação de um aplicativo usando o AWS CodeDeploy. A função é acionada por um evento, como o upload de um arquivo .zip para um bucket S3. Ao ser ativada, a função extrai o nome do bucket e a chave do objeto do evento, cria um cliente CodeDeploy e define a localização do arquivo .zip no S3 como a nova revisão de implantação. Por fim, a função inicia uma nova implantação no CodeDeploy usando o aplicativo e o grupo de implantação especificados, retornando o ID da implantação recém-criada para confirmação. Essencialmente, este script conecta a automação de eventos do S3 com o fluxo de implantação do CodeDeploy, criando um pipeline simples de CI/CD.

- **GuardDuty-With-Lambda** <br>
Para monitorar e contornar vulnerabilidades apontadas pelo GuardDuty, desenvolvi este projeto para que, quando uma vulnerabilidade for detectada, o AWS EventBridge executará uma função Lambda. Por exemplo: GuardDuty detectou uma vulnerabilidade relacinada a *Unauthorized Access*, o AWS EventBridge identifica a ameça e executa uma função Lambda. **Data:** *03/03/2023*

- **Creating-Security-Groups** <br>
Neste projeto, decidi ousar um pouco mais e apronfudar um pouco mais acerca do projeto anteriormente desenvolvido. Agora, será possível deixar com que a função lambda 
crie, de forma automatizada, o grupo/grupos de segurança para você, defina o tráfego permitido e associe à instãncia. **Data:** *28/02/2023*

- **Isolating-Instancess** <br>
Este projeto parte do mesmo princípio do projeto anterior - um script será executado em uma instância EC2 para enviar uma mensagem, contendo seu ID, ao AWS SQS -, mas
irá executar *- imediatamente -* o script apenas quando um login via SSH (*porta 22*) for detectado. Após executado, modificado os grupos de segurança atribuídos à
instância, isto é, por exemplo, seria possível **REMOVER** o Security Group que permite a entrada do Protocolo SSH e permitir apenas a entrada de requisições HTTP através do código: `ec2.modify_instance_attribute(InstanceId=body, Groups=[bastion_http])`. **Data:** *24/02/2023*

- **Stopping-Instances** <br>
Este projeto foi desenvolvido para que, quando um script fosse executado em uma instância EC2, seria enviado o ID desta Instância para o AWS SQS que, consequentemente,
seria acionado a função Lambda para realizar o desligamento de instância com base no ID da instância recebido através do AWS SQS. **Data:** *23/02/2023*

## 📑 Informações adicionais

Estes projetos foram desenvolvidos para fins de aprendizagem e desenvolvimento profissional acerca do AWS Lambda, logo, não há nenhum código muito complexo e de difícil entendimento. Entretanto, pode ser que haja algumas brechas de erro e vulnerabilidades de segurança. Todavia, não recomendo que seja utilizado em um ambiente de produção real.

Conforme eu avançar e me aprofundar meus conhecimentos neste serviço, pretendo trazer mais conteúdo para este repositório.

Enquanto isto, você pode me acompanhar na minha rede social onde posto alguns conteúdos referentes a Cloud Computing: [LinkedIn](linkedin.com/in/vitor-silva-de-antoni/)
