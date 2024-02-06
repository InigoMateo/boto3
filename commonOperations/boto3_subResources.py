import boto3

"""
Sub-resources:

Sub-resources are methods that create a new instance of a child resource. This resource’s identifiers get passed along 
to the child. Bucket and Object are sub-resources of one another. 

If you have a bucket variable created you can create an object directly.

And if you have an Object variable, then you can get its bucket
"""

s3_resource = boto3.resource('s3')
first_bucket = s3_resource.Bucket(name='first_bucket_name')
first_object = s3_resource.Object(bucket_name='first_bucket_name', key='first_file_name')


# For instance, once we have created a bucket we don't need to pass all the information to an object inside that
# bucket, like when we define an object alone: first_object = s3_resource.Object(bucket_name='first_bucket_name',
# key='first_file_name')
first_object_again = first_bucket.Object('first_file_name')


# Again if we have an object, this means it is being created inside a bucket, so we can get directly the bucket.
# first_object = s3_resource.Object(bucket_name='first_bucket_name', key='first_file_name')
first_bucket_again = first_object.Bucket()
