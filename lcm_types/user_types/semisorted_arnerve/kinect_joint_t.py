"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class kinect_joint_t(object):
    __slots__ = ["position", "istracking"]

    def __init__(self):
        self.position = [ 0.0 for dim0 in range(3) ]
        self.istracking = 0

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(kinect_joint_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack('>3d', *self.position[:3]))
        buf.write(struct.pack(">B", self.istracking))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != kinect_joint_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return kinect_joint_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = kinect_joint_t()
        self.position = struct.unpack('>3d', buf.read(24))
        self.istracking = struct.unpack(">B", buf.read(1))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if kinect_joint_t in parents: return 0
        tmphash = (0x35b170c185c3f02b) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if kinect_joint_t._packed_fingerprint is None:
            kinect_joint_t._packed_fingerprint = struct.pack(">Q", kinect_joint_t._get_hash_recursive([]))
        return kinect_joint_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

