import gmpy2
import libnum
import binascii
from Cryptodome.Util.number import long_to_bytes


def encrypt_Rsa(p, q, n, e, m):
    m = libnum.s2n(m)
    c = libnum.n2s(pow(m, e, n))
    c = binascii.hexlify(c)
    return c


def decrypt_Rsa(p, q, n, e, c):
    phi = (p - 1) * (q - 1)
    d = gmpy2.invert(e, phi)
    c = binascii.unhexlify(c)
    c=libnum.s2n(c)
    m = pow(c, d, n)
    m=long_to_bytes(m)
    return d, m
