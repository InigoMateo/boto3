import boto3

"""
Downloading a File

To download a file from S3 locally, you’ll follow similar steps as you did when uploading. But in this case, the 
Filename parameter will map to your desired local path. 

Exactly the same as for uploading. There are three ways you can download a file:

    From an Object instance
    From a Bucket instance
    From the client
"""

s3_resource = boto3.resource('s3')
first_file_name = 'first_file_name'

# This time, it will download the file to the tmp directory:
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/object/download_file.html
s3_resource.Object('first_bucket_name', first_file_name).download_file(f'/tmp/{first_file_name}')  # Python 3.6+
