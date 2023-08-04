def lambda_handler(event, context):
    nome = event["nomeInput"]
    sobrenome = event["sobrenomeInput"]
    idade = event["idadeInput"]

    print(f"Olá, {nome} {sobrenome}. Você tem {idade} anos.")

    # Para popular o espaço de "response" do ambiente de teste
    # Se não especificar, a função retornará "null" na área de *response*
    response = {
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade
    }

    return response