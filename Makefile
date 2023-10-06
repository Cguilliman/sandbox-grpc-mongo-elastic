run-server:
	docker stop recommendations
	docker run -p 127.0.0.1:50051:50051/tcp --network grpc-sandbox-network --name recommendations grpc-sandbox-server

build-run-server:
	#docker stop recommendations
	docker rm recommendations
	docker build . -f server/Dockerfile -t grpc-sandbox-server
	docker run -p 127.0.0.1:50051:50051/tcp --network grpc-sandbox-network --name recommendations grpc-sandbox-server

run-client:
	docker run --network grpc-sandbox-network -e RECOMMENDATIONS_HOST=recommendations grpc-sandbox-client

build-run-client:
	docker build . -f client/Dockerfile -t grpc-sandbox-client
	docker run --network grpc-sandbox-network -e RECOMMENDATIONS_HOST=recommendations grpc-sandbox-client

run-mongo:
	docker run -d -p 27017:27017 --name grpc-sandbox-mondodb --network grpc-sandbox-network mongo:latest

proto-server:
	python3 -m grpc_tools.protoc -I ./protobufs --python_out=./server/ --grpc_python_out=./server/ ./protobufs/recommendations.proto

proto-client:
	python3 -m grpc_tools.protoc -I ./protobufs --python_out=./client/ --grpc_python_out=./client/ ./protobufs/recommendations.proto

run-elastic:
	docker run -d --name grpc-sandbox-elastic --network grpc-sandbox-network -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" elasticsearch:8.10.2

