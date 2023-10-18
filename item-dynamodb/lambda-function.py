import json, boto3

def lambda_handler(context, event):
	dynamo = boto3.client("dynamodb")

	itemData = {
		"primaryKey": {"<S/N>":"<data>"},
		"sortKey":{"<S/N>":"<data>"},
		"<otherAtribute>":{"<S/N/B/BOOL...>":"<data>"}
	}

	dynamo.put_item(TableName="<tableName>", Item=itemData)
