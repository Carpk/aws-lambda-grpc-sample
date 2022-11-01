from concurrent import futures
import logging

import grpc
import grpc_pb2
import grpc_pb2_grpc
import requests
import yaml


class Greeter(grpc_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        with open('config.yml', 'r') as file:
            conf = yaml.safe_load(file)

        response = requests.get(conf['url'] + "?t=" + conf['time'])
        result = "none found"

        if(not response.json()):
            result = "The time requested was not found in the logs"
        else:
            obj = {'t':conf['time'],'d':conf['delta'],'r':conf['regex'],'b':conf['bucket'],'k':conf['log']}
            result = requests.post(conf['url'], json = obj).json()

        return grpc_pb2.HelloReply(message=' '.join(result))


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
