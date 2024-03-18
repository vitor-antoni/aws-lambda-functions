import boto3, json, pytz
from datetime import datetime, timedelta

def lambda_handler(event, context):
  utc_time = pytz.utc
  client = boto3.client("s3")
  bucket_name = "{bucketName}"
  
  # Se desejar rodar esta função faseadamente
  # dividindo a execução por folders, informe o nome da folder
  # no argumento ", Prefix="{folderName})" logo após de "bucket_name"
  listObjects = client.list_objects(Bucket=bucket_name)
  objetos = listObjects["Contents"]

  # Data hoje
  dataHoje = datetime.now(tz=utc_time)
  dataCalculo = calcularData(dataHoje)
  
  iterandoObjetos = 0
  while iterandoObjetos < len(objetos):
    # Remove as pastas da listagem
    if "." not in objetos[iterandoObjetos]["Key"]:
      iterandoObjetos += 1
      continue

    if objetos[iterandoObjetos]["LastModified"] < dataCalculo:
      print(f"Removendo o objeto: {objetos[iterandoObjetos]["Key"]}")
      client.delete_object(Bucket=bucketName, Key=objetos[iterandoObjetos]["Key"])

    iterandoObjetos += 1

def calcularData(dataHoje):
  diasDelta = dataHoje - timedelta(days=1)

  return diasDelta
  
