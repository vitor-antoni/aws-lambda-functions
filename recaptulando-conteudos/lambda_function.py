import boto3, json, os

regionName = "us-east-1"

def lambda_handler(event, context):
    client = boto3.client("ec2", region_name=regionName)
    
    for record in event["Records"]:
        instaceId = record["body"]
        print(f"ID da Instancia EC2: {instaceId}")
        
    print(f"Variavel ambiente: {variavelAmbiente()}")
    
def variavelAmbiente():
    return os.environ["Senha"]
