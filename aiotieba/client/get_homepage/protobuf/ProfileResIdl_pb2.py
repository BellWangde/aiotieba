# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProfileResIdl.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..._protobuf import Error_pb2 as Error__pb2
from ..._protobuf import User_pb2 as User__pb2
from ..._protobuf import PostInfoList_pb2 as PostInfoList__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13ProfileResIdl.proto\x1a\x0b\x45rror.proto\x1a\nUser.proto\x1a\x12PostInfoList.proto\"\x83\x02\n\rProfileResIdl\x12\x15\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x06.Error\x12$\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x16.ProfileResIdl.DataRes\x1a\xb4\x01\n\x07\x44\x61taRes\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\x12.\n\tanti_stat\x18\x02 \x01(\x0b\x32\x1b.ProfileResIdl.DataRes.Anti\x12 \n\tpost_list\x18\x04 \x03(\x0b\x32\r.PostInfoList\x1a\x42\n\x04\x41nti\x12\x12\n\nblock_stat\x18\x06 \x01(\x05\x12\x11\n\thide_stat\x18\x07 \x01(\x05\x12\x13\n\x0b\x64\x61ys_tofree\x18\t \x01(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ProfileResIdl_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROFILERESIDL._serialized_start=69
  _PROFILERESIDL._serialized_end=328
  _PROFILERESIDL_DATARES._serialized_start=148
  _PROFILERESIDL_DATARES._serialized_end=328
  _PROFILERESIDL_DATARES_ANTI._serialized_start=262
  _PROFILERESIDL_DATARES_ANTI._serialized_end=328
# @@protoc_insertion_point(module_scope)