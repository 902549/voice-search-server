# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from messages import voice_search_server_pb2 as messages_dot_voice__search__server__pb2


class SpeechStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamingRecognize = channel.stream_stream(
                '/audiostream.Speech/StreamingRecognize',
                request_serializer=messages_dot_voice__search__server__pb2.StreamingRecognizeRequest.SerializeToString,
                response_deserializer=messages_dot_voice__search__server__pb2.StreamingRecognizeResponse.FromString,
                )
        self.Enroll = channel.unary_unary(
                '/audiostream.Speech/Enroll',
                request_serializer=messages_dot_voice__search__server__pb2.EnrollRequest.SerializeToString,
                response_deserializer=messages_dot_voice__search__server__pb2.EnrollResponse.FromString,
                )


class SpeechServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamingRecognize(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Enroll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SpeechServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamingRecognize': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamingRecognize,
                    request_deserializer=messages_dot_voice__search__server__pb2.StreamingRecognizeRequest.FromString,
                    response_serializer=messages_dot_voice__search__server__pb2.StreamingRecognizeResponse.SerializeToString,
            ),
            'Enroll': grpc.unary_unary_rpc_method_handler(
                    servicer.Enroll,
                    request_deserializer=messages_dot_voice__search__server__pb2.EnrollRequest.FromString,
                    response_serializer=messages_dot_voice__search__server__pb2.EnrollResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'audiostream.Speech', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Speech(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamingRecognize(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/audiostream.Speech/StreamingRecognize',
            messages_dot_voice__search__server__pb2.StreamingRecognizeRequest.SerializeToString,
            messages_dot_voice__search__server__pb2.StreamingRecognizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Enroll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/audiostream.Speech/Enroll',
            messages_dot_voice__search__server__pb2.EnrollRequest.SerializeToString,
            messages_dot_voice__search__server__pb2.EnrollResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
