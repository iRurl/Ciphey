import binascii
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

def RSA_Encrypt(public_key, plaintext):
    rsakey = RSA.importKey(public_key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = binascii.hexlify(cipher.encrypt(plaintext.encode('utf-8'))).decode()
    return cipher_text


def RSA_Decrypt(private_key, ciphertext):
    ciphertext = binascii.unhexlify(ciphertext)
    private_key = private_key
    rsakey = RSA.importKey(private_key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    decrypted_msg = cipher.decrypt(ciphertext, None)
    return decrypted_msg
