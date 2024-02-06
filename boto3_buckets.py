import boto3
import uuid

""" 
Bucket in AWS:

Obviously we need a bucket to start working with AWS S3. To create one programmatically, you must first choose a name
for your bucket. Bear in mind that this bucket name must be unique among all the whole AWS platform as bucket names
are DNS compliant.

If you try to create a bucket, but another user has already claimed your desired bucket name, your code will fail. You 
will get the following error botocore.errorfactory.BucketAlreadyExists. You can increase your chance of success when 
creating your bucket by picking a random name. You can generate your own function that does that for you.

That is why we use uuid function to generate a name for us, along with a prefix at the beginning.
"""


def create_bucket_name(bucket_prefix):
    # the generated bucket name must be between 3 and 63 characters.
    return ''.join([bucket_prefix, str(uuid.uuid4())])


# Now we have created a bucket name
print(create_bucket_name('test_name'))


# Now we proceed with the creation of a bucket:
# We define a resource from which we call the function 'create_bucket'. This is not a good practice since we are
# hardcoding the location constraint and when deployed in Production not all users may have this region set.
# s3_resource = boto3.resource('s3')
# s3_resource.create_bucket(Bucket=YOUR_BUCKET_NAME,
#                           CreateBucketConfiguration={
#                               'LocationConstraint': 'eu-west-1'
#                           })


# This is not an ideal situation since we are hardcoding the location constraint and when deployed in Production not
# all users may have this region set. That's why we come with the following function:


# A session is created from user credentials, so you can return the right region no matter where your code is deployed
def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    # We warranty that in case of location 'us-east-1' wea re not getting errors. With 'us-east-1' there used to be
    # errors
    if current_region == 'us-east-1':
        bucket_response = s3_connection.create_bucket(
            Bucket=bucket_name
        )
    else:
        bucket_response = s3_connection.create_bucket(
            Bucket=bucket_name,
            )
    print(bucket_name, current_region)
    return bucket_name, bucket_response


# s3_resource = boto3.resource('s3')
#
# create_bucket('first-python-bucket', s3_resource.meta.client)
