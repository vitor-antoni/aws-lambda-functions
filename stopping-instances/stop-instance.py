import json, boto3

region = '<region>'

def lambda_handler(event, context):
    ec2 = boto3.client('ec2',region_name=region)
    
    for record in event['Records']:
        body = record['body']
        print('ID da Instancia: ' + body)
        
        # Desligando instancia
        instances = [body]
        try:
            ec2.stop_instances(InstanceIds=instances)
            print('Sucesso para desligar instancia: ' + instances)
        except Exception as error:
            print(f'Houve um erro com a função Lambda: {error}')
            
