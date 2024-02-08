import boto3

"""
Traversals:

If you need to retrieve information from or apply an operation to all your S3 resources, boto3 gives you several ways to
iteratively traverse your buckets and your objects. 
"""

s3_resource = boto3.resource('s3')

"""Bucket traversal"""
# To traverse all your buckets in your account, you can use the resource's bucket attribute alongside .all() which gives
# you the complete list of Bucket instances:
# s3_resource.buckets.all() return a list[Bucket]
for bucket in s3_resource.buckets.all():
    print(bucket.name)

# You can use the client to retrieve the bucket information as well, but the code is more complex, as you need to
# extract it from the dictionary that the client returns
# s3_resource.meta.client.list_bucket() return a list[dict[ResponseMetadata, Buckets, Owner]]
# and in the Buckets -> dict[Name, CreationDate] that is why we do a for loop then a get('Buckets') and finally ['Name']
for bucket_dict in s3_resource.meta.client.list_buckets().get('Buckets'):
    print(bucket_dict['Name'])

"""Object traversal"""
# In case we want to iterate all over the objects in a bucket this method will generate and iterator to obtain them
first_bucket = s3_resource.Bucket('first_bucket_name')
for obj in first_bucket.objects.all():
    print(obj.key)

# The obj variable is an ObjectSummary (s3.ObjectSummary(bucket_name, key)). This is a lightweight representation of an
# Object. The summary version doesn't support all the attributes that the Object has. If you need to access them, use
# the Object() sub-resource to create a new reference to the underlying stored key. Then you'll be able to extract
# missing attributes:
for obj in first_bucket.objects.all():
    subrsc = obj.Object()
    print (obj.key, obj.storage_class, obj.last_modified, subrsc.version_id, subrsc.metadata)

