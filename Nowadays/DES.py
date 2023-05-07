from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad
import binascii


# 完成一个DES的CBC模式加密函数
def DES_CBC_Encrypt(key, iv, plaintext):
    key = key.encode()
    iv = iv.encode()
    plaintext = plaintext.encode()
    # 创建一个DES的加密对象
    cipher = DES.new(key, DES.MODE_CBC, iv)
    # 对明文进行填充
    plaintext = pad(plaintext, int(len(key)), style='pkcs7')
    # 加密
    ciphertext = cipher.encrypt(plaintext)
    ciphertext_hex = binascii.hexlify(ciphertext)
    return ciphertext_hex


# 完成一个DES的CBC模式解密函数
def DES_CBC_Decrypt(key, iv, ciphertext):
    key = key.encode()
    iv = iv.encode()
    ciphertext = ciphertext.encode()
    print(ciphertext)
    ciphertext = binascii.unhexlify(ciphertext)
    print(ciphertext)
    # 创建一个DES的解密对象
    cipher = DES.new(key, DES.MODE_CBC, iv)
    # 解密
    plaintext = cipher.decrypt(ciphertext)
    # 去除填充
    plaintext = unpad(plaintext, int(len(key)), style='pkcs7')
    print(plaintext)
    return plaintext


# 完成一个DES的ECB模式加密函数
def DES_ECB_Encrypt(key, plaintext):
    key = key.encode()
    plaintext = plaintext.encode()
    # 创建一个DES的加密对象
    cipher = DES.new(key, DES.MODE_ECB)
    # 对明文进行填充
    plaintext = pad(plaintext, int(len(key)), style='pkcs7')
    # 加密
    ciphertext = cipher.encrypt(plaintext)
    ciphertext_hex = binascii.hexlify(ciphertext)
    return ciphertext_hex


# 完成一个DES的ECB模式解密函数
def DES_ECB_Decrypt(key, ciphertext):
    key = key.encode()
    ciphertext = ciphertext.encode()
    ciphertext = binascii.unhexlify(ciphertext)
    # 创建一个DES的解密对象
    cipher = DES.new(key, DES.MODE_ECB)
    # 解密
    plaintext = cipher.decrypt(ciphertext)
    # 去除填充
    plaintext = unpad(plaintext, int(len(key)), style='pkcs7')
    return plaintext


# 完成一个DES的CTR模式加密函数
def DES_CTR_Encrypt(key, iv, plaintext):
    key = key.encode()
    iv = iv.encode()
    plaintext = plaintext.encode()
    # 创建一个DES的加密对象
    cipher = DES.new(key, DES.MODE_CTR, iv)
    # 加密
    ciphertext = cipher.encrypt(plaintext)
    ciphertext_hex = binascii.hexlify(ciphertext)
    return ciphertext_hex


# 完成一个DES的CTR模式解密函数
def DES_CTR_Decrypt(key, iv, ciphertext):
    key = key.encode()
    iv = iv.encode()
    ciphertext = ciphertext.encode()
    ciphertext = binascii.unhexlify(ciphertext)
    # 创建一个DES的解密对象
    cipher = DES.new(key, DES.MODE_CTR, iv)
    # 解密
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


# 完成一个DES的OFB模式加密函数
def DES_OFB_Encrypt(key, iv, plaintext):
    key = key.encode()
    iv = iv.encode()
    plaintext = plaintext.encode()
    # 创建一个DES的加密对象
    cipher = DES.new(key, DES.MODE_OFB, iv)
    # 加密
    ciphertext = cipher.encrypt(plaintext)
    ciphertext_hex = binascii.hexlify(ciphertext)
    return ciphertext_hex


# 完成一个DES的OFB模式解密函数
def DES_OFB_Decrypt(key, iv, ciphertext):
    key = key.encode()
    iv = iv.encode()
    ciphertext = ciphertext.encode()
    ciphertext = binascii.unhexlify(ciphertext)
    # 创建一个DES的解密对象
    cipher = DES.new(key, DES.MODE_OFB, iv)
    # 解密
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


# 完成一个DES的CFB模式加密函数
def DES_CFB_Encrypt(key, iv, plaintext):
    key = key.encode()
    iv = iv.encode()
    plaintext = plaintext.encode()
    # 创建一个DES的加密对象
    cipher = DES.new(key, DES.MODE_CFB, iv)
    # 加密
    ciphertext = cipher.encrypt(plaintext)
    ciphertext_hex = binascii.hexlify(ciphertext)
    return ciphertext_hex


# 完成一个DES的CFB模式解密函数
def DES_CFB_Decrypt(key, iv, ciphertext):
    key = key.encode()
    iv = iv.encode()
    ciphertext = ciphertext.encode()
    ciphertext = binascii.unhexlify(ciphertext)
    # 创建一个DES的解密对象
    cipher = DES.new(key, DES.MODE_CFB, iv)
    # 解密
    plaintext = cipher.decrypt(ciphertext)
    return plaintext
