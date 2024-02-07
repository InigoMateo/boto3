import boto3

"""
Uploading a File:

There are three ways you can upload a file:

    From an Object instance
    From a Bucket instance
    From the client

In each case, you have to provide the Filename, which is the path of the file you want to upload. You’ll now explore 
the three alternatives. Feel free to pick whichever you like most to upload the first_file_name to S3.

    ** You also may come with a question? Can i create "folders" inside a bucket in S3, yes you can. **

When defining the object you can indicate in the file name the path you want to create and the object to be store in.
so for instance a good file path would be:

s3_resource.Object(first_bucket_name, doc/textFile/first_file_name).upload_file(Filename=first_file_name)

S3 is going to build a path inside the bucket doc/textFile/... But Remember this! In aws s3 the concept of folder does
not exist only buckets and objects.
"""

s3_resource = boto3.resource('s3')

# Object Instance Version
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/object/upload_file.html
s3_resource.Object('first_bucket_name', 'first_file_name').upload_file(Filename='first_file_name')

# Bucket Instance Version (Filename is the path of the file to upload)
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/upload_file.html
s3_resource.Bucket('first_bucket_name').upload_file(Filename='first_file_name', Key='first_file_name')

# Client Version
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/upload_file.html
s3_resource.meta.client.upload_file(Filename='first_file_name', Bucket='first_bucket_name', Key='first_file_name')
