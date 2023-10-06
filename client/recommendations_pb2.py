# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommendations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder


# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15recommendations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"8\n\x15RecommendationRequest\x12\x1f\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\r.BookCategory"P\n\x12\x42ookRecommendation\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x1f\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\r.BookCategory".\n\x16RecommendationResponse\x12\x14\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x05.Book"d\n\x11\x43reateBookRequest\x12\x12\n\x05title\x18\x03 \x01(\tH\x00\x88\x01\x01\x12$\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\r.BookCategoryH\x01\x88\x01\x01\x42\x08\n\x06_titleB\x0b\n\t_category"O\n\x11UpdateBookRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x1f\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\r.BookCategory"\xa2\x01\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x1f\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\r.BookCategory\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp",\n\x14\x42ookModifiedResponse\x12\x14\n\x05\x62ooks\x18\x01 \x01(\x0b\x32\x05.Book"\x0e\n\x0c\x45mptyRequest"\x0f\n\rEmptyResponse"\x1f\n\x11\x42ookDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t"#\n\x11\x42ookSearchRequest\x12\x0e\n\x06search\x18\x01 \x01(\t"*\n\x12\x42ookSearchResponse\x12\x14\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x05.Book*?\n\x0c\x42ookCategory\x12\x0b\n\x07MYSTERY\x10\x00\x12\x13\n\x0fSCIENCE_FICTION\x10\x01\x12\r\n\tSELF_HELP\x10\x02\x32\x93\x02\n\x05\x42ooks\x12<\n\tRecommend\x12\x16.RecommendationRequest\x1a\x17.RecommendationResponse\x12#\n\x06\x43reate\x12\x12.CreateBookRequest\x1a\x05.Book\x12#\n\x06Update\x12\x12.UpdateBookRequest\x1a\x05.Book\x12!\n\x07Monitor\x12\r.EmptyRequest\x1a\x05.Book0\x01\x12,\n\x06\x44\x65lete\x12\x12.BookDeleteRequest\x1a\x0e.EmptyResponse\x12\x31\n\x06Search\x12\x12.BookSearchRequest\x1a\x13.BookSearchResponseb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "recommendations_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_BOOKCATEGORY"]._serialized_start = 787
    _globals["_BOOKCATEGORY"]._serialized_end = 850
    _globals["_RECOMMENDATIONREQUEST"]._serialized_start = 58
    _globals["_RECOMMENDATIONREQUEST"]._serialized_end = 114
    _globals["_BOOKRECOMMENDATION"]._serialized_start = 116
    _globals["_BOOKRECOMMENDATION"]._serialized_end = 196
    _globals["_RECOMMENDATIONRESPONSE"]._serialized_start = 198
    _globals["_RECOMMENDATIONRESPONSE"]._serialized_end = 244
    _globals["_CREATEBOOKREQUEST"]._serialized_start = 246
    _globals["_CREATEBOOKREQUEST"]._serialized_end = 346
    _globals["_UPDATEBOOKREQUEST"]._serialized_start = 348
    _globals["_UPDATEBOOKREQUEST"]._serialized_end = 427
    _globals["_BOOK"]._serialized_start = 430
    _globals["_BOOK"]._serialized_end = 592
    _globals["_BOOKMODIFIEDRESPONSE"]._serialized_start = 594
    _globals["_BOOKMODIFIEDRESPONSE"]._serialized_end = 638
    _globals["_EMPTYREQUEST"]._serialized_start = 640
    _globals["_EMPTYREQUEST"]._serialized_end = 654
    _globals["_EMPTYRESPONSE"]._serialized_start = 656
    _globals["_EMPTYRESPONSE"]._serialized_end = 671
    _globals["_BOOKDELETEREQUEST"]._serialized_start = 673
    _globals["_BOOKDELETEREQUEST"]._serialized_end = 704
    _globals["_BOOKSEARCHREQUEST"]._serialized_start = 706
    _globals["_BOOKSEARCHREQUEST"]._serialized_end = 741
    _globals["_BOOKSEARCHRESPONSE"]._serialized_start = 743
    _globals["_BOOKSEARCHRESPONSE"]._serialized_end = 785
    _globals["_BOOKS"]._serialized_start = 853
    _globals["_BOOKS"]._serialized_end = 1128
# @@protoc_insertion_point(module_scope)
