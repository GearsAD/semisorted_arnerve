"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class role_request_t(object):
    __slots__ = ["timestamp", "userName", "requestedRole", "isUpdatingRole", "newPlannerGroup", "isUpdatingPlannerGroup", "requestedBotNameToPilot", "isUpdatingBot"]

    Observer = 0
    Pilot = 1
    Planner = 2
    Commander = 3

    def __init__(self):
        self.timestamp = 0
        self.userName = ""
        self.requestedRole = 0
        self.isUpdatingRole = 0
        self.newPlannerGroup = ""
        self.isUpdatingPlannerGroup = 0
        self.requestedBotNameToPilot = ""
        self.isUpdatingBot = 0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(role_request_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.timestamp))
        __userName_encoded = self.userName.encode('utf-8')
        buf.write(struct.pack('>I', len(__userName_encoded)+1))
        buf.write(__userName_encoded)
        buf.write("\0")
        buf.write(struct.pack(">bb", self.requestedRole, self.isUpdatingRole))
        __newPlannerGroup_encoded = self.newPlannerGroup.encode('utf-8')
        buf.write(struct.pack('>I', len(__newPlannerGroup_encoded)+1))
        buf.write(__newPlannerGroup_encoded)
        buf.write("\0")
        buf.write(struct.pack(">b", self.isUpdatingPlannerGroup))
        __requestedBotNameToPilot_encoded = self.requestedBotNameToPilot.encode('utf-8')
        buf.write(struct.pack('>I', len(__requestedBotNameToPilot_encoded)+1))
        buf.write(__requestedBotNameToPilot_encoded)
        buf.write("\0")
        buf.write(struct.pack(">b", self.isUpdatingBot))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != role_request_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return role_request_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = role_request_t()
        self.timestamp = struct.unpack(">q", buf.read(8))[0]
        __userName_len = struct.unpack('>I', buf.read(4))[0]
        self.userName = buf.read(__userName_len)[:-1].decode('utf-8', 'replace')
        self.requestedRole, self.isUpdatingRole = struct.unpack(">bb", buf.read(2))
        __newPlannerGroup_len = struct.unpack('>I', buf.read(4))[0]
        self.newPlannerGroup = buf.read(__newPlannerGroup_len)[:-1].decode('utf-8', 'replace')
        self.isUpdatingPlannerGroup = struct.unpack(">b", buf.read(1))[0]
        __requestedBotNameToPilot_len = struct.unpack('>I', buf.read(4))[0]
        self.requestedBotNameToPilot = buf.read(__requestedBotNameToPilot_len)[:-1].decode('utf-8', 'replace')
        self.isUpdatingBot = struct.unpack(">b", buf.read(1))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if role_request_t in parents: return 0
        tmphash = (0x910e43bdfe15bd39) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if role_request_t._packed_fingerprint is None:
            role_request_t._packed_fingerprint = struct.pack(">Q", role_request_t._get_hash_recursive([]))
        return role_request_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

