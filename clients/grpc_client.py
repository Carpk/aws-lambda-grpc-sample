from __future__ import print_function

import logging

import grpc
import grpc_pb2
import grpc_pb2_grpc
import yaml


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    conf=""
    with open('config.yml', 'r') as file:
        conf = yaml.safe_load(file)

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(grpc_pb2.HelloRequest(name="02:12:00"))

    print("Received: " + response.message)





if __name__ == '__main__':
    logging.basicConfig()
    run()
