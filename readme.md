build protobuf schemas

`python3 -m grpc_tools.protoc -I ./protobufs --python_out=./server --grpc_python_out=./server protobufs/books.proto`

manually build for server

`python3 -m grpc_tools.protoc -I ./protobufs --python_out=./server/ --gpc_python_out=./server/ ./protobufs/recommendations.proto`

manually build for client

`python3 -m grpc_tools.protoc -I ./protobufs --python_out=./client/ --grpc_python_out=./client/ ./protobufs/recommendations.proto`

create network

`docker network create grpc-sandbox-network`

build and run server 

```
docker build . -f server/Dockerfile -t grpc-sandbox-server
docker run -p 127.0.0.1:50051:50051/tcp --network grpc-sandbox-network --name recommendations grpc-sandbox-server
```

build and run client

```
docker build . -f client/Dockerfile -t grpc-sandbox-client
docker run --network grpc-sandbox-network -e RECOMMENDATIONS_HOST=recommendations grpc-sandbox-client
```

Run mongodb

`docker run -p 27017:27017 --name mongo-app -d mongo:latest`
