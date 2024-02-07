import boto3
from commonOperations.boto3_namingObjects import create_temp_file

"""
Encryption:

With S3, you can protect your data using encryption. Here we will see how server-side encryption works using AES-256
algorithm where AWS manages both the encryption and the keys.
"""

s3_resource = boto3.resource('s3')

# We again create a new file that is going to be encrypted
third_file_name = create_temp_file(300, 'thirdFile', 't')
third_object = s3_resource.Object('first_bucket_name', 'third_file_name')

third_object.upload_file('third_file_name', ExtraArgs={'ServerSideEncryption': 'AES256'})


# Checking server side encryption. When uploading a file to S3 by default it is always encrypted in AES256
third_object.server_side_encryption