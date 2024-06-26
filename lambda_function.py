import json
import sys
import botocore
import boto3

def lambda_handler(event, context):
    # TODO implement https://dev.to/aws-builders/modify-the-aws-rds-instance-size-using-lambda-function-1l71
    boto3.client('rds').modify_db_instance(DBInstanceIdentifier='nombre-rds', 
    DBInstanceClass='db.m5.2large',ApplyImmediately=True) 
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
