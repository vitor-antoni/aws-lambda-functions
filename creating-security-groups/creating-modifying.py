import json, boto3

# Caso houver um SG existente, especifique ele aqui e na linha 37 também
existSG = '<sg_id>'

region = '<region>'
vpc_id = '<vpc>'

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)

    try:
        criandoSg = ec2.create_security_group(GroupName='<sg_name>', Description='<sg_desc>',
                                              VpcId=vpc_id, TagSpecifications=[{
                'ResourceType': 'security-group',
                'Tags': [{
                    'Key': 'Name',""
                    'Value': '<sg_tag>'
                }]
            }])

        sgId = criandoSg['GroupId']

        ec2.authorize_security_group_ingress(GroupId=sgId, IpPermissions=[{
            'IpProtocol': '<protocolo>',    # Defina o protocolo a ser usado
            'FromPort': 0,                  # Porta que deseja liberar
            'ToPort': 0,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }])

        print('[SUCESSO] O Security Group foi criado!')

        try:
            for record in event['Records']:
                body = record['body']

                ec2.modify_instance_attribute(InstanceId=body, Groups=[existSG])

            print('[SUCESSO] Modificação dos grupos de segurança na instancia.')

        except Exception as e:
            print(f'[ERRO] Erro para modificar o grupo de segurança das instancias: {e}')

    except Exception as e:
        error_message = str(e)
        if 'InvalidGroup.Duplicate' in error_message:
            print('[ALERTA!] O Security Group NÃO foi criado, pois ele há existe!')
            pass
        else:
            print(e)
