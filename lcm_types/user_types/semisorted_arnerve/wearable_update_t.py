"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

import joystick_update_t

class wearable_update_t(object):
    __slots__ = ["timestamp", "numKeysDown", "keysPressed", "joystick"]

    def __init__(self):
        self.timestamp = 0
        self.numKeysDown = 0
        self.keysPressed = []
        self.joystick = None

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(wearable_update_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qb", self.timestamp, self.numKeysDown))
        buf.write(struct.pack('>%dh' % self.numKeysDown, *self.keysPressed[:self.numKeysDown]))
        assert self.joystick._get_packed_fingerprint() == joystick_update_t.joystick_update_t._get_packed_fingerprint()
        self.joystick._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != wearable_update_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return wearable_update_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = wearable_update_t()
        self.timestamp, self.numKeysDown = struct.unpack(">qb", buf.read(9))
        self.keysPressed = struct.unpack('>%dh' % self.numKeysDown, buf.read(self.numKeysDown * 2))
        self.joystick = joystick_update_t.joystick_update_t._decode_one(buf)
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if wearable_update_t in parents: return 0
        newparents = parents + [wearable_update_t]
        tmphash = (0x1b8d2e7c5a7f0fb3+ joystick_update_t.joystick_update_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if wearable_update_t._packed_fingerprint is None:
            wearable_update_t._packed_fingerprint = struct.pack(">Q", wearable_update_t._get_hash_recursive([]))
        return wearable_update_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

