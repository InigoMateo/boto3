# Boto3 examples S3

## Introduction to Boto3: Harness the Power of AWS with Python

**Boto3** is the official **Python SDK** 🐍 (Software Development Kit) provided by Amazon Web Services (AWS). It allows developers to interact with various AWS services programmatically using Python. Whether you’re building web applications, automating infrastructure, or working with data, Boto3 simplifies the process of integrating your Python code with AWS services. Along this repo we will walk together through the most important functionalities in boto3 for S3.

**Credits to:** https://realpython.com/python-boto3-aws-s3/#installation where all the information collected here has been based on.

<p align="center">
<img src="[[https://cdn.romexsoft.com/wp-content/uploads/2019/09/aws-s3-icon.svg](https://www.google.com/url?sa=i&url=https%3A%2F%2Fdev.to%2Faws-builders%2Fgetting-started-with-boto3-a-powerful-and-versatile-aws-sdk-442d&psig=AOvVaw2GqOetHe-uBUFowWCLNKme&ust=1725196409788000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKCAgM-nn4gDFQAAAAAdAAAAABAJ)](https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fe4kppkfy2639q33qzwks.jpg)" width="200" height="200" />
</p>

### Key Features of Boto3:
1. Simple and Pythonic:
- Boto3 follows Python conventions, making it easy to read and write.
- You can use it seamlessly within your Python projects.
2. Wide Range of Services:
- Boto3 supports interactions with over 100 AWS services, including EC2, S3, DynamoDB, Lambda, and more.
- You can create, manage, and monitor resources directly from your Python code.
3. Authentication and Credentials:
- Before using Boto3, set up your AWS credentials (access key and secret key) to authenticate with AWS services.
- Boto3 automatically uses these credentials when making API requests.
4. Resource-Oriented Approach:
- Boto3 provides a resource-based API for interacting with AWS services.
- Resources represent AWS entities (e.g., EC2 instances, S3 buckets) and offer a higher-level abstraction.
5. Client Interface:
- Boto3 also offers a client interface for low-level access to AWS services.
- Clients provide direct access to API actions and responses.For this repo we will center on resources, which is an high level object that allows us to interact with s3 functionalities

### Repo Index:

This index will walk you through the files in this repo and how to advance through it.

1. Installation
2. clientVsResource
   1. boto3_clientResource
3. commonOperations
   1. boto3_buckets
   2. boto3_namingObjects
   3. boto3_objects
   4. boto3_subResources
   5. boto3_uploadingObject
   6. boto3_downloadingObject
   7. boto3_copying
   8. boto3_deleting
4. advancedConfigurations
   1. boto3_acl
   2. boto3_encryption
   3. boto3_storage
   4. boto3_versioning
5. traversals
   1. boto3_bucketTraversal
6. deletingBucketAndObjects
   1. boto3_deleting

### Getting Started with Boto3:

For the initial setup, I recommend going directly to the official web page: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html. Based on my experience, configuring AWS credentials and config files—plain text files that store keys, secret keys, and S3 regions—is straightforward in a Linux environment. Boto3 automatically recognizes the default storage paths at ~/.aws/credentials or ~/.aws/config on Linux or macOS. However, on Windows, you might need to set environment variables or make additional adjustments. Considering all these factors, I encourage you to set up your development environment using a Linux distribution. 

**Installation:**

Install Boto3 using pip install boto3.

**Setting Up AWS Credentials:**

Configure your AWS credentials using the AWS CLI or by setting environment variables (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY).

🚀 And now we are ready to rock!! 🚀

