import json, boto3

# Nome do aplicativo CodeDeploy
app_name = 'DeployingAplication'

# Nome do grupo de implantação CodeDeploy
deployment_group = 'ImplantacaoApp'

def lambda_handler(event, context):    
    # Nome do bucket S3 onde o objeto foi enviado
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    
    # Nome do objeto que foi enviado
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Criação de um cliente do CodeDeploy
    codedeploy_client = boto3.client('codedeploy')
    
    # Criação de um objeto de revisão de implantação do CodeDeploy
    revision_deploy = {
        'revisionType': 'S3',
        's3Location': {
            'bucket': bucket_name,
            'key': object_key,
            'bundleType': 'zip'
        }
    }
    
    # Criação de um objeto de implantação do CodeDeploy
    deployment = {
        'applicationName': app_name,
        'deploymentGroupName': deployment_group,
        'revision': revision_deploy
    }
    
    # Inicia a implantação do CodeDeploy
    response = codedeploy_client.create_deployment(applicationName=app_name, 
    deploymentGroupName=deployment_group, revision=revision_deploy)
    
    # Retorna o ID da implantação criada
    deployment_id = response['deploymentId']
    return f'Implantação iniciada com sucesso. ID da implantação: {deployment_id}'
