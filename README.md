
# AWS Lambda and gRPC Sample

These are a group of scripts used to generate log files on EC2, stored on S3, and read through REST and gRPC calls to a lambda function on AWS.

### Requirements

This was developed using Python 3.9


## Running the Scripts

Each set of scipts are in thier own directory

### Log Generator

The log generator is on an EC2 instance an can be ran using:

`sbt clean compile run | aws s3 cp - s3://log-generator-files-cs441/logs/LogX.log`

Where LogX can be any numerical log, as we use Log2 for testing in the video.

### Python Clients

Adjust the YAML config file to make adjustments to the settings

To make a python REST call:

`python restQuery.py`

To make a gPRC call:

First we need to start the gPRC server

`python grpc_server.py`

Then start the client

`python grpc_client.py`

### Lambda Script

The lambda sripts that are on AWS

`python lambdaRun.py`

### Tests

Tests are only in the lambda directory:

`python lambdaTest.py`

## Video Demonstration

A short video demonstration on how to run the scripts

[https://thekleinbottle.com/alags/index.html](https://thekleinbottle.com/alags/index.html)
