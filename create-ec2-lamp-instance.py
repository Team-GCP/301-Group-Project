#/usr/bin/python
# Script:                       301 Final Project Script
# Author:                       Courtney Hans
# Date of latest revision:      9/23/2020
# Purpose:                      Create a new Linux EC2 lamp stack instance in AWS using boto3 SDK

#import boto3 library
import boto3
ec2 = boto3.resource('ec2')

# Declare variables
# Takes user input to determine how many stacks to create
number = input("How many LAMP stacks would you like to create?\n")

# Main

#create a new EC2 instance using boto3 SDK
#ami is for a lamp stack i created and configured in AWS
#security group for Developers configured w/ appropriate permissions (PowerUserAccess)
#IAM role for Developers configured w/ appropriate AWS console/access permissions

instances = ec2.create_instances(
        ImageId='ami-0841edc20334f9287',
        MinCount=1,
        MaxCount=number,
        InstanceType='t2.micro',
        SecurityGroupIds=['sg-08b2201cde476753d',],
        IamInstanceProfile={
                'Arn': 'arn:aws:iam::135314874534:instance-profile/Developers'
        },
        KeyName='beta-key'
)

print("Building your LAMP stack(s)!")
#resources: blog.ipswitch.com/how-to-create-an-ec2-instance-with-python

# End
