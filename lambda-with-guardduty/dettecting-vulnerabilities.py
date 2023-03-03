import json, boto3

def lambda_handler(event, context):
    region = '<region>'
    instanceId = '<instanceId>'
    sgId = ['<sgId>']
    vpcId = '<vpcId>'
    ec2 = boto3.client('ec2', region_name=region)

    ec2.revoke_security_group_ingress(GroupId=sgId, IpPermissions=[{
        'IpProtocol':'tcp',
        'FromPort':22,
        'ToPort':22,
        'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
    }])

    print("Instância isolada com sucesso!")



    ec2.create_security_group(GroupName='', VpcId='', Description='', TagSpecifications=[{
        'ResourceType':'security-group',
        'Tags':[{
            'Key':'Name',
            'Value':'<tagName>'
        }]
    }])

    ec2.authorize_security_group_ingress(GroupId='', IpPermisions=[{
        'IpProtocol':'tcp',
        'FromPort':80,
        'ToPort':80,
        'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
    },
    {
        'IpProtocol':'tcp',
        'FromPort':443,
        'ToPort':443,
        'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
    }])

    ec2.modify_instance_attribute(InstaceId=instanceId, Groups=['<sgIds>'])