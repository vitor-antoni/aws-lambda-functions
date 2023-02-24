#!/bin/bash
# Descomente as linhas abaixo caso preciso.
# aws configure set aws_access_key_id <access_key>
# aws configure set aws_secret_access_key <secret_key>
# aws configure set aws_session_token <session_token>

INSTANCE_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id)
REGION=$(curl http://169.254.169.254/latest/meta-data/placement/availability-zone | sed '$s/.$//')

SQS-URL="https://your-sqs-url.com"

aws sqs send-message --queue-url "${SQS-URL}" --message-body "${INSTANCE_ID}" --region "${REGION}"
