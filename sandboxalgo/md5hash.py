#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2015, The Profitware Group'

from math import fabs, floor, sin
from struct import pack, unpack


class dword(int):
    def __or__(self, other):
        return dword((int(self) | other & 0xFFFFFFFF) & 0xFFFFFFFF)

    def __and__(self, other):
        return dword((int(self) & (other & 0xFFFFFFFF)) & 0xFFFFFFFF)

    def __xor__(self, other):
        return dword((int(self) ^ (other & 0xFFFFFFFF)) & 0xFFFFFFFF)

    def __lshift__(self, other):
        return dword((int(self) << (other & 0xFFFFFFFF)) & 0xFFFFFFFF)

    def __rshift__(self, other):
        return dword((int(self) >> (other & 0xFFFFFFFF)) & 0xFFFFFFFF)

    def __add__(self, other):
        return dword((int(self) + (other & 0xFFFFFFFF)) & 0xFFFFFFFF)


S = map(dword,
    [7, 12, 17, 22] * 4 +
    [5, 9, 14, 20] * 4 +
    [4, 11, 16, 23] * 4 +
    [6, 10, 15, 21] * 4
)

K = [dword(floor(fabs(sin(i + 1)) * (2 ** 32))) for i in xrange(64)]

CHUNK_LENGTH = 512 / 8


def md5(msg):
    """RFC 1321 MD5 Message-Digest Algorithm implementation.

    >>> assert md5('') == 'd41d8cd98f00b204e9800998ecf8427e'

    >>> assert md5('The quick brown fox jumps over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'

    >>> assert md5('The quick brown fox jumps over the lazy dog.') == 'e4d909c290d0fb1ca068ffaddf22cbd0'

    >>> assert md5('A' * 10000) == '0f53217fc7c8e7f89e8a8558e64a7083'

    """

    left_rotate = lambda x, c: (x << c) | (x >> (32 - c))

    a0 = dword(0x67452301)
    b0 = dword(0xefcdab89)
    c0 = dword(0x98badcfe)
    d0 = dword(0x10325476)

    original_length = len(msg) * 8

    msg += chr(0x01 << 7)
    while (len(msg) * 8) % 512 != 448:
        msg += chr(0x00)

    len_long = original_length % (2 ** 64)
    msg += pack("<Q", len_long & 0xFFFFFFFFFFFFFFFF)

    chunk_offset = 0
    while True:
        chunk = msg[chunk_offset: chunk_offset + CHUNK_LENGTH]
        chunk_tuple = unpack('<16I', chunk)

        a, b, c, d = a0, b0, c0, d0

        for i in xrange(64):

            f, g = 0, 0

            if i in range(0, 16):
                f = d ^ (b & (c ^ d))
                g = i
            elif i in range(16, 32):
                f = c ^ (d & (b ^ c))
                g = (5 * i + 1) % 16
            elif i in range(32, 48):
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            elif i in range(48, 64):
                f = c ^ (b | (~d))
                g = (7 * i) % 16

            d_temp = d
            d = c
            c = b
            b += left_rotate(dword(a + f + K[i] + chunk_tuple[g]), S[i])
            a = d_temp

        a0 += a
        b0 += b
        c0 += c
        d0 += d

        chunk_offset += CHUNK_LENGTH
        if chunk_offset >= len(msg):
            break

    md5hash = ''.join([pack("<L", i) for i in (a0, b0, c0, d0)])
    return ''.join("{:02x}".format(ord(c)) for c in md5hash)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
