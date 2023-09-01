import boto3

ec2 = boto3.resource('ec2', region_name='us-west-2')

# Create instance
instances = ec2.create_instances(
     ImageId='ami-053b0d53c279acc90', # AMI ID for ubuntu instance
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='practiceKey') # Key pair name


