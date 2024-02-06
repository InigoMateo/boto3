import boto3

"""
Copying or Moving an Object Between Buckets:

If you need to copy files from one bucket to another, Boto3 offers you that possibility. In this example, you’ll copy 
the file from the first bucket to the second, using .copy()
"""

s3_resource = boto3.resource('s3')


def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)


# Remember to substitute the names with the original ones
copy_to_bucket('first_bucket_name', 'second_bucket_name', 'first_file_name')
