import boto3

"""
Objects:

Once we have created our file it is time to upload it to our S3 bucket and keep the working workflow. Here comes the 
resource class, as this abstraction makes it easy to work with S3.

To store your data in Amazon S3, you work with resources known as buckets and objects. A bucket is a container for 
objects. An object is a file and any metadata that describes that file.

In this .py we are only creating instances
"""

s3_resource = boto3.resource('s3')


# def get_bucket(s3_connection, first_bucket_name):
#     return s3_connection.Bucket(first_bucket_name)


# def create_object(s3_connection, first_bucket_name, first_file_name):
#     return s3_connection.Object(bucket_name=first_bucket_name, key=first_file_name)


# Replace first_bucket_name with your bucket name
first_bucket = s3_resource.Bucket(name='first_bucket_name')


# Replace your first_bucket_name with your bucket name and first_file_name with your first file
first_object = s3_resource.Object(bucket_name='first_bucket_name', key='first_file_name')
