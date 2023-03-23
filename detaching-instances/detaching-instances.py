import boto3

def lambda_handler(event, context):
	# Prescisa de uma lista de instâncias
	instanceId = ["<id>"]
	vpcId = "<id>"
	asgName = "<id>"

	ec2 = boto3.client("ec2")
	asg = boto3.client("autoscaling")

	try:
		detaching = asg.detach_instances(InstanceIds=instanceId, AutoScalingGroupName=asgName)

		print("Sucesso para desanexar a instância.")

	except Exeception as e:
		print(f"Erro para desanexar a instância: {e}")

	else:
		creatingSg = ec2.create_security_group(VpcId=vpcId, Description="Acesso Instancia Forense",
			GroupName="acessoInstanciaForense")

		groupId = creatingSg["GroupId"]

		modifyIn = ec2.authorize_security_group_ingress(GroupId=groupId, IpPermissions=[{
			"IpProtocol":"tcp",
			"FromPort":22,
			"ToPort":22,
			"UserIdGroupPairs":[{"GroupId":"<gpId>"}]
		}])

		modifyOut = ec2.authorize_security_group_egress(GroupId=groupId, IpPermissions=[{
			"IpProtocol":"tcp",
			"FromPort":22,
			"ToPort":22,
			"UserIdGroupPairs":[{"GroupId":"<gpId>"}]
		}])

		print("Concedido!")

		revokeDefautlRule = ec2.revoke_security_group_egress(GroupId=groupId, IpPermissions=[{
			"IpProtocol":"-1",
			"IpRanges":[{"CidrIp":"0.0.0.0/0"}]
		}])

		print("Revogado!")