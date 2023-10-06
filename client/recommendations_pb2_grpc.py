# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import recommendations_pb2 as recommendations__pb2

import grpc


class BooksStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recommend = channel.unary_unary(
            "/Books/Recommend",
            request_serializer=recommendations__pb2.RecommendationRequest.SerializeToString,
            response_deserializer=recommendations__pb2.RecommendationResponse.FromString,
        )
        self.Create = channel.unary_unary(
            "/Books/Create",
            request_serializer=recommendations__pb2.CreateBookRequest.SerializeToString,
            response_deserializer=recommendations__pb2.Book.FromString,
        )
        self.Update = channel.unary_unary(
            "/Books/Update",
            request_serializer=recommendations__pb2.UpdateBookRequest.SerializeToString,
            response_deserializer=recommendations__pb2.Book.FromString,
        )
        self.Monitor = channel.unary_stream(
            "/Books/Monitor",
            request_serializer=recommendations__pb2.EmptyRequest.SerializeToString,
            response_deserializer=recommendations__pb2.Book.FromString,
        )
        self.Delete = channel.unary_unary(
            "/Books/Delete",
            request_serializer=recommendations__pb2.BookDeleteRequest.SerializeToString,
            response_deserializer=recommendations__pb2.EmptyResponse.FromString,
        )
        self.Search = channel.unary_unary(
            "/Books/Search",
            request_serializer=recommendations__pb2.BookSearchRequest.SerializeToString,
            response_deserializer=recommendations__pb2.BookSearchResponse.FromString,
        )


class BooksServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Recommend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Monitor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_BooksServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Recommend": grpc.unary_unary_rpc_method_handler(
            servicer.Recommend,
            request_deserializer=recommendations__pb2.RecommendationRequest.FromString,
            response_serializer=recommendations__pb2.RecommendationResponse.SerializeToString,
        ),
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=recommendations__pb2.CreateBookRequest.FromString,
            response_serializer=recommendations__pb2.Book.SerializeToString,
        ),
        "Update": grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=recommendations__pb2.UpdateBookRequest.FromString,
            response_serializer=recommendations__pb2.Book.SerializeToString,
        ),
        "Monitor": grpc.unary_stream_rpc_method_handler(
            servicer.Monitor,
            request_deserializer=recommendations__pb2.EmptyRequest.FromString,
            response_serializer=recommendations__pb2.Book.SerializeToString,
        ),
        "Delete": grpc.unary_unary_rpc_method_handler(
            servicer.Delete,
            request_deserializer=recommendations__pb2.BookDeleteRequest.FromString,
            response_serializer=recommendations__pb2.EmptyResponse.SerializeToString,
        ),
        "Search": grpc.unary_unary_rpc_method_handler(
            servicer.Search,
            request_deserializer=recommendations__pb2.BookSearchRequest.FromString,
            response_serializer=recommendations__pb2.BookSearchResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("Books", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Books(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Recommend(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Books/Recommend",
            recommendations__pb2.RecommendationRequest.SerializeToString,
            recommendations__pb2.RecommendationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Create(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Books/Create",
            recommendations__pb2.CreateBookRequest.SerializeToString,
            recommendations__pb2.Book.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Update(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Books/Update",
            recommendations__pb2.UpdateBookRequest.SerializeToString,
            recommendations__pb2.Book.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Monitor(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/Books/Monitor",
            recommendations__pb2.EmptyRequest.SerializeToString,
            recommendations__pb2.Book.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Delete(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Books/Delete",
            recommendations__pb2.BookDeleteRequest.SerializeToString,
            recommendations__pb2.EmptyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Search(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Books/Search",
            recommendations__pb2.BookSearchRequest.SerializeToString,
            recommendations__pb2.BookSearchResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
