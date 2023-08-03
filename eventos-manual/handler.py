def lambda_handler(event, context):
    nome = event["nome"]
    sobrenome = event["sobrenome"]

    return f"Ola, {nome} {sobrenome}"