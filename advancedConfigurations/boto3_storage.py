import boto3

"""
Storage:

Every object that you add to your S3 bucket is associated with a storage class. All the available storage classes
offer high durability. You choose how you want to store tour objects based on your application's performance access
requirements.

At present, you can use the following storage classes with s3:

- STANDARD: default for frequently accessed data
- STANDARD_IA: for infrequently used data that needs to be retrieved rapidly when requested
- ONEZONE_AI: for the same use case as STANDARD_IA, but stores the data in one Availability Zone instead of the three.
- REDUCED_REDUNDANCY: for frequently used noncritical data that is easily reproducible.
"""

s3_resource = boto3.resource('s3')

# If you want to change the storage class of an existing object, you need to recreate the object.
# For example reuploading the third_object and setting its storage class to STANDARD_AI
third_object = s3_resource.Object('first_bucket_name', 'third_file_name')
third_object.upload_file('third_file_name', ExtraArgs={
    'ServerSideEncryption': 'AES256',
    'StorageClass': 'STANDARD_IA'})

# In my case I haven't needed it but just in case reload the object
third_object.reload()
# Check the new storage class for your object
third_object.storage_class