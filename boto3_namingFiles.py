import uuid

import boto3

"""
Naming Files:

When naming files is important to have a standard naming convection that allows to grow yout files in an order and 
sustain way. Here we are going to talk about more specific cases that help us to understand how s3 works under the
hood and optimize performance.

Once we have created our first bucket we can start adding files to it, as we add more and more files it is important
how we named them. If all our files name have a deterministic prefix that gets repeated for each file, like "YYYY-MM-DD 
hh:mm:ss. What s3 will do is looking at this prefix and it will interpret that all these files are related keeping them 
in the same disk partition. This can cause this partition to slow down if these files are being requested simultaneously.

To avoid this we shouldn't name files with a fix prefix. 
"""


# That is why we are going to create a random file_name (again using uuid library)
# This function can be changed, so you can pass only the file_name and other file content
def create_temp_file(size, file_name, file_content):
    # We set first the uuid generated chain of characters
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name
