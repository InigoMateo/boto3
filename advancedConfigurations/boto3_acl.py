import boto3
from commonOperations.boto3_namingObjects import create_temp_file

"""
ACL (Access Control Lists):

Access Control Lists (ACLs) help you manage access to your buckets and the objects within them. They are considered
the legacy way of administrating permissions to S3. Why should i know about them? If you have to manage access to 
individual object, then you would use an Object ACL.

By default, when you upload an object to S3, that object is private. If you want to make this object available to 
someone else, you can set the object's ACL to be public at creation time.
"""

s3_resource = boto3.resource('s3')

# Here we are going to use upload_dile using the parameters it has assigned.
# You see that we are defining the object name with a previous function created "create_temp_file"
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html#boto3.s3.transfer.TransferConfig


# IMPORTANT:
# Remember when modifying your object 'ACL' to enable the following options in the bucket.
# Buckets > 'bucket_name' >  Edit Object Ownership
# Buckets > 'bucket_name' > Edit Block public access (bucket settings)

second_file_name = create_temp_file(400, 'secondfile.txt', 's')
second_object = s3_resource.Object('first_name_bucket', second_file_name)
# With this ACL level set you are granting read rights to all user in the internet, with or without AWS credentials
second_object.upload_file(second_file_name, ExtraArgs={'ACL': 'public-read'})

# You can get the ObjectAcl instance from the Object, as it is one of its sub-resource classes:
second_object_acl = second_object.Acl()

# To see who has access to your project, use grants attribute:
second_object_grants = second_object_acl.grants

# You can make your object private again, without needing to re-upload it:
response = second_object_acl.put(ACL='private')
second_object_acl.grants
