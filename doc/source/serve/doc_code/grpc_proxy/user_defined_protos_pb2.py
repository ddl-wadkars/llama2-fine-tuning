# __begin__
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_defined_protos.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19user_defined_protos.proto\x12\x11userdefinedprotos"?\n\x12UserDefinedMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06origin\x18\x02 \x01(\t\x12\x0b\n\x03num\x18\x03 \x01(\x03"4\n\x13UserDefinedResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t\x12\x0b\n\x03num\x18\x02 \x01(\x03"\x15\n\x13UserDefinedMessage2"(\n\x14UserDefinedResponse2\x12\x10\n\x08greeting\x18\x01 \x01(\t"*\n\tImageData\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t"4\n\nImageClass\x12\x0f\n\x07\x63lasses\x18\x01 \x03(\t\x12\x15\n\rprobabilities\x18\x02 \x03(\x02\x32\xae\x02\n\x12UserDefinedService\x12Y\n\x08__call__\x12%.userdefinedprotos.UserDefinedMessage\x1a&.userdefinedprotos.UserDefinedResponse\x12_\n\x0cMultiplexing\x12&.userdefinedprotos.UserDefinedMessage2\x1a\'.userdefinedprotos.UserDefinedResponse2\x12\\\n\tStreaming\x12%.userdefinedprotos.UserDefinedMessage\x1a&.userdefinedprotos.UserDefinedResponse0\x01\x32\x64\n\x1aImageClassificationService\x12\x46\n\x07Predict\x12\x1c.userdefinedprotos.ImageData\x1a\x1d.userdefinedprotos.ImageClassB:\n#io.ray.examples.user_defined_protosB\x11UserDefinedProtosP\x01\x62\x06proto3'  # noqa: E501
)


_USERDEFINEDMESSAGE = DESCRIPTOR.message_types_by_name["UserDefinedMessage"]
_USERDEFINEDRESPONSE = DESCRIPTOR.message_types_by_name["UserDefinedResponse"]
_USERDEFINEDMESSAGE2 = DESCRIPTOR.message_types_by_name["UserDefinedMessage2"]
_USERDEFINEDRESPONSE2 = DESCRIPTOR.message_types_by_name["UserDefinedResponse2"]
_IMAGEDATA = DESCRIPTOR.message_types_by_name["ImageData"]
_IMAGECLASS = DESCRIPTOR.message_types_by_name["ImageClass"]
UserDefinedMessage = _reflection.GeneratedProtocolMessageType(
    "UserDefinedMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _USERDEFINEDMESSAGE,
        "__module__": "user_defined_protos_pb2"
        # @@protoc_insertion_point(class_scope:io.ray.examples.user_defined_protos.UserDefinedMessage)
    },
)
_sym_db.RegisterMessage(UserDefinedMessage)

UserDefinedResponse = _reflection.GeneratedProtocolMessageType(
    "UserDefinedResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _USERDEFINEDRESPONSE,
        "__module__": "user_defined_protos_pb2"
        # @@protoc_insertion_point(class_scope:io.ray.examples.user_defined_protos.UserDefinedResponse)
    },
)
_sym_db.RegisterMessage(UserDefinedResponse)

UserDefinedMessage2 = _reflection.GeneratedProtocolMessageType(
    "UserDefinedMessage2",
    (_message.Message,),
    {
        "DESCRIPTOR": _USERDEFINEDMESSAGE2,
        "__module__": "user_defined_protos_pb2"
        # @@protoc_insertion_point(class_scope:io.ray.examples.user_defined_protos.UserDefinedMessage2)
    },
)
_sym_db.RegisterMessage(UserDefinedMessage2)

UserDefinedResponse2 = _reflection.GeneratedProtocolMessageType(
    "UserDefinedResponse2",
    (_message.Message,),
    {
        "DESCRIPTOR": _USERDEFINEDRESPONSE2,
        "__module__": "user_defined_protos_pb2"
        # @@protoc_insertion_point(class_scope:io.ray.examples.user_defined_protos.UserDefinedResponse2)
    },
)
_sym_db.RegisterMessage(UserDefinedResponse2)

ImageData = _reflection.GeneratedProtocolMessageType(
    "ImageData",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMAGEDATA,
        "__module__": "user_defined_protos_pb2"
        # @@protoc_insertion_point(class_scope:io.ray.examples.user_defined_protos.ImageData)
    },
)
_sym_db.RegisterMessage(ImageData)

ImageClass = _reflection.GeneratedProtocolMessageType(
    "ImageClass",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMAGECLASS,
        "__module__": "user_defined_protos_pb2"
        # @@protoc_insertion_point(class_scope:io.ray.examples.user_defined_protos.ImageClass)
    },
)
_sym_db.RegisterMessage(ImageClass)

_USERDEFINEDSERVICE = DESCRIPTOR.services_by_name["UserDefinedService"]
_IMAGECLASSIFICATIONSERVICE = DESCRIPTOR.services_by_name["ImageClassificationService"]
if _descriptor._USE_C_DESCRIPTORS is False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\026io.ray.examples.user_defined_protosB\013UserDefinedProtosP\001\370\001\001"  # noqa: E501
    _USERDEFINEDMESSAGE._serialized_start = 43
    _USERDEFINEDMESSAGE._serialized_end = 125
    _USERDEFINEDRESPONSE._serialized_start = 127
    _USERDEFINEDRESPONSE._serialized_end = 194
    _USERDEFINEDMESSAGE2._serialized_start = 196
    _USERDEFINEDMESSAGE2._serialized_end = 217
    _USERDEFINEDRESPONSE2._serialized_start = 219
    _USERDEFINEDRESPONSE2._serialized_end = 269
    _IMAGEDATA._serialized_start = 271
    _IMAGEDATA._serialized_end = 328
    _IMAGECLASS._serialized_start = 330
    _IMAGECLASS._serialized_end = 406
    _USERDEFINEDSERVICE._serialized_start = 409
    _USERDEFINEDSERVICE._serialized_end = 663
    _IMAGECLASSIFICATIONSERVICE._serialized_start = 665
    _IMAGECLASSIFICATIONSERVICE._serialized_end = 749
# @@protoc_insertion_point(module_scope)

# __end__
