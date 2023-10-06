import contextlib
from concurrent import futures

import recommendations_pb2_grpc
from app.elastic import init_connection
from app.mongo import client
from loguru import logger

import grpc
from .api import BooksServicer


@contextlib.contextmanager
def run_server(port: int):
    server = grpc.server(
        futures.ThreadPoolExecutor(),
    )
    recommendations_pb2_grpc.add_BooksServicer_to_server(BooksServicer(), server)
    server.add_insecure_port(f"[::]:{port}")

    init_connection()
    server.start()

    try:
        yield server, port
    finally:
        logger.info("Closed!")
        client.close()
        server.stop(0)
