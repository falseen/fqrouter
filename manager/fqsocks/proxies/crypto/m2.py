#!/usr/bin/env python

# Copyright (c) 2014 clowwindy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import absolute_import, division, print_function, \
    with_statement


__all__ = ['ciphers']

import M2Crypto.EVP


def create_cipher(alg, key, iv, op, key_as_bytes=0, d=None, salt=None, i=1,
                  padding=1):

    return M2Crypto.EVP.Cipher(alg.replace('-', '_'), key, iv, op,
                               key_as_bytes=0, d='md5', salt=None, i=1,
                               padding=1)


ciphers = {
    b'aes-128-cfb': (16, 16, create_cipher),
    b'aes-192-cfb': (24, 16, create_cipher),
    b'aes-256-cfb': (32, 16, create_cipher),
    b'bf-cfb': (16, 8, create_cipher),
    b'camellia-128-cfb': (16, 16, create_cipher),
    b'camellia-192-cfb': (24, 16, create_cipher),
    b'camellia-256-cfb': (32, 16, create_cipher),
    b'cast5-cfb': (16, 8, create_cipher),
    b'des-cfb': (8, 8, create_cipher),
    b'idea-cfb': (16, 8, create_cipher),
    b'rc2-cfb': (16, 8, create_cipher),
    b'rc4': (16, 0, create_cipher),
    b'seed-cfb': (16, 16, create_cipher),
    }
