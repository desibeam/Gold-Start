aws_service_list = []

aws_service_list.append("DynamoDB")

aws_service_list.append("CloudFront")

aws_service_list.append("Lambda")

aws_service_list.append("Athena")

aws_service_list.append("SageMaker")

aws_service_list.append("Kinesis")

aws_service_list.append("EC2")

aws_service_list.append("Redshift")

aws_service_list.append("S3")

aws_service_list.append("ECS")

print(aws_service_list)

print(len(aws_service_list))

del aws_service_list [2]

del aws_service_list [5]

print(aws_service_list)

print(len(aws_service_list))
