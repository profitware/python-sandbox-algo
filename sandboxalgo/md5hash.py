#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2015, The Profitware Group'

from math import fabs, floor, sin
from struct import pack, unpack

S = \
    [7, 12, 17, 22] * 4 + \
    [5, 9, 14, 20] * 4 + \
    [4, 11, 16, 23] * 4 + \
    [6, 10, 15, 21] * 4

K = [int(floor(fabs(sin(i)) * (2 ** 32))) for i in xrange(64)]

CHUNK_LENGTH = 512 / 8

def md5(msg):

    leftrotate = lambda x, c: (x << c) | (x >> (32 - c))

    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476

    original_length = len(msg) * 8

    msg += chr(0x01 << 7)
    while (len(msg) * 8) % 512 != 448:
        msg += chr(0x00)

    print len(msg)

    len_long = original_length % (2 ** 64)
    msg += pack("!Q", len_long & 0xFFFFFFFFFFFFFFFF) # , (len_long >> 64) & 0xFFFFFFFFFFFFFFFF

    chunk_offset = 0
    while True:
        chunk = msg[chunk_offset: chunk_offset + CHUNK_LENGTH]
        print len(chunk)
        chunk_tuple = unpack('>16i', chunk)

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
            print a, f, K[i], chunk_tuple[g], S[i]
            b = b + leftrotate((a + f + K[i] + chunk_tuple[g]), S[i])
            a = d_temp

        a0 += a
        b0 += b
        c0 += c
        d0 += d

        chunk_offset += CHUNK_LENGTH
        if chunk_offset >= len(msg):
            break

    return ''.join([pack("!Q", i & 0xFFFFFFFFFFFFFFFF) for i in (a0, b0, c0, d0)])

if __name__ == '__main__':
    print len(md5('Hello'))