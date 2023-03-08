import json, boto3

def lambda_handler(event, context):
    region = "<region>"
    instanceId = "<instanceId>"
    groupId = "<groupId>"
    ebsVolumeId = "<ebsVolumeId>"

    ec2 = boto3.client('ec2', region_name=region)

    # Renega a permissão da porta 22 descrita no Security Group
    ec2.revoke_security_group_ingress(GroupId=groupId, IpPermissions=[{
        'IpProtocol':'tcp',
        'FromPort':22,
        'ToPort':22,
        'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
    }])

    ec2.create_snapshot(VolumeId=ebsVolumeId, TagSpecifications=[{
        'ResourceType':'snapshot',
        'Tags':[{
            'Key':'Name',
            'Value':'snashot-instancia-isolada'
        }]
    }])

