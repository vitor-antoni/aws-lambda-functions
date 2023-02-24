import json, boto3

def lambda_handler(event, context):
    region = 'us-east-1'
    ec2 = boto3.client('ec2', region_name=region)
    
    for record in event['Records']:
        body = record['body']
        print('ID da Instancia: ' + body)
        
        
        # Especifique os grupos de segurança e seus ID's
        bastion_ssh = 'sg-0d125a155483641fb'
        bastion_http = 'sg-041b5cf84769f4688'
        # bastion_https = '<securityGroup_id>'
        
        # Isolando instancia
        try:
            # Desejo desassociar o Security Group que permite
            # entrada de SSH, logo, não especificarei ele 
            ec2.modify_instance_attribute(InstanceId=body, 
                Groups=[bastion_http])
            
            print('Sucesso para modificar a instancia: ' + body)
        except Exception as error:
            print(f'Houve um erro com a função Lambda: {error}')