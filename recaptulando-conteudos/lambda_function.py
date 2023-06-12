import boto3, json, os

def lambda_handler(event, context):
    for record in event["Records"]:
        instaceId = record["body"]
        print(f"ID da Instancia EC2: {instaceId}")
        
    print(variavelAmbiente())
    
def variavelAmbiente():
    return os.environ["Senha"]