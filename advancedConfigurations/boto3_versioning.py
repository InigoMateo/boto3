import boto3

"""
Versioning:

You should use versioning to keep a complete track of your objects over time. It also acts as a protection mechanism
against accidental deletion of your objects.  When you request a versioned object, boto3 will retrieve the latest 
version.

IMPORTANT: when you add a new version of an object, the storage that object takes in total is the sunm of the size of 
its versions. So if you are storing an object of 1GB, and you create 10 version, then you have to pau for 10GB of 
storage. (bear in min this for data accumulation)
"""

s3_resource = boto3.resource('s3')


# Enable versioning for the first bucket. To do this, you need to use the BucketVersioning class:
def enable_bucket_versioning(bucket_name):
    bkt_versioning = s3_resource.BucketVersioning(bucket_name)
    bkt_versioning.enable()
    print(bkt_versioning.status)


# enable_bucket_versioning('first_bucket_name')

# Then create two new versions for the first file Object, one with the contents of the original file and one with the
# contents of the third file:
s3_resource.Object('first_bucket_name', 'first_file_name').upload_file('first_file_name')
s3_resource.Object('first_bucket_name', 'first_file_name').upload_file('third_file_name')


# Now reupload the second file, which will create a new version:
s3_resource.Object('first_bucket_name', 'first_file_name').upload_file('second_file_name')


# You can retrieve the latest available version of your objects like so:
s3_resource.Object('first_bucket_name', 'first_file_name').version_id