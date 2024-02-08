import boto3

"""
Deleting Buckets and Objects:

To remove all the buckets and objects you have created, you must first make sure that your buckets have no objects within
them

- When deleting a non-empty bucket:
To be able to delete a bucket, you must first delete every single object within the bucket, or else the BucketNonEmpty
exception will be raised. When you have a versioned bucket, you need to delete every object and all its versions.

If you find that a LifeCycle rule that will do this automatically for you isn't suitable to your needs, here is how
you can programmatically delete the objects.

The below code works whether or not you have enabled versioning on your bucket. If you haven't, the version of the objects
will be null. You can batch up to 1000 deletions in one API call, using .delete_objects() on your Bucket instance, which
is more cost-effective than individually deleting each object.
"""

s3_resource = boto3.resource('s3')


# bucket.object_versions.all() returns
# s3.ObjectVersion(bucket_name='firstpythonbucket-63710d96-79bf-4d85-bfea-6eeea47f99b0', object_key='40cc6ethirdFile', id='null')
def delete_all_objects(bucket_name):
    res = []
    bucket = s3_resource.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        res.append({'Key': obj_version.object_key,
                    'VersionId': obj_version.id})
    print(res)
    # Delete objects
    if res:
        bucket.delete_objects(Delete={'Objects': res})
        print(f"Deleted {len(res)} objects from bucket {bucket_name}")
    else:
        print(f"No objects found in bucket {bucket_name}")


# As a final test let's upload a file to the second bucket. This bucket doesn't have versioning enabled,
# thus the version will be null.
s3_resource.Object('second_bucket_name', 'first_file_name').upload_file('first_name_file')
delete_all_objects('second_bucket_name')
