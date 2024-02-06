import boto3

"""
Deleting an Object:

Let's delete the new file just created. Again you can delete files from object, bucket or client instances.
"""

s3_resource = boto3.resource('s3')


s3_resource.Object('second_bucket_name', 'first_file_name').delete()