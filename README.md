
# AWS Lambda and gRPC Sample

These are a group of scripts used to generate log files on EC2, stored on S3, and read through REST and gRPC calls to a lambda function on AWS.

#### Requirements

This was developed using Python 3.9



### Running the Scripts

Each set of scipts are in thier own directory

#### Python Clients

Adjust the YAML config file to make adjustments to the settings

To make a python REST call:

`python restQuery.py`

To make a gPRC call:

First we nee to start the gPRC server





#### Log Generator

The log generator is on an EC2 instance an can be ran using:

`sbt clean compile run | aws s3 cp - s3://log-generator-files-cs441/logs/Log2.log`


