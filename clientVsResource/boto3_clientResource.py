import boto3

""" 
Client and resources:

At its core all the Boto3 does is call AWS APIs on your behalf. Boto3 offers two distinct ways of accessing these abstracted APIs:
    1. Client: low-level service access
    2. Resource: higher-level object-oriented service access 
"""

# In the arguments pass the name of the service you want to connect to.
s3_client = boto3.client('s3')

s3_resource = boto3.resource('s3')

# Client service has every option AWS APIs offers, however resource can be limited and not support every operation,
# thus this is why we can use meta interface 'meta.client' out of a resource to access client's methods
s3_resource.meta.client.generate_presigned_url()


