from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import binascii


# 完成AES的CBC模式加密函数
def AES_CBC_Encrypt(key, iv, plaintext):
    key = key.encode()
    iv = iv.encode()
    plaintext = plaintext.encode()
    # 创建一个AES的加密对象
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 对明文进行填充
    plaintext = pad(plaintext, int(len(key)), style='pkcs7')
    # 加密
    ciphertext = cipher.encrypt(plaintext)
    ciphertext_hex = binascii.hexlify(ciphertext)
    return ciphertext_hex


# 完成AES的CBC模式解密函数
def AES_CBC_Decrypt(key, iv, ciphertext):
    key = key.encode()
    iv = iv.encode()
    ciphertext = ciphertext.encode()
    ciphertext = binascii.unhexlify(ciphertext)
    # 创建一个AES的解密对象
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 解密
    plaintext = cipher.decrypt(ciphertext)
    # 去除填充
    plaintext = unpad(plaintext, int(len(key)), style='pkcs7')
    return plaintext


# 完成AES的ECB模式加密函数
def AES_ECB_Encrypt(key, plaintext):
    key = key.encode()
    plaintext = plaintext.encode()
    # 创建一个AES的加密对象
    cipher = AES.new(key, AES.MODE_ECB)
    # 对明文进行填充
    plaintext = pad(plaintext, int(len(key)), style='pkcs7')
    # 加密
    ciphertext = cipher.encrypt(plaintext)
    ciphertext_hex = binascii.hexlify(ciphertext)
    return ciphertext_hex


# 完成AES的ECB模式解密函数
def AES_ECB_Decrypt(key, ciphertext):
    key = key.encode()
    ciphertext = ciphertext.encode()
    ciphertext = binascii.unhexlify(ciphertext)
    # 创建一个AES的解密对象
    cipher = AES.new(key, AES.MODE_ECB)
    # 解密
    plaintext = cipher.decrypt(ciphertext)
    # 去除填充
    plaintext = unpad(plaintext, int(len(key)), style='pkcs7')
    return plaintext


# 完成AES的CTR模式加密函数
def AES_CTR_Encrypt(key, iv, plaintext):
    key = key.encode()
    iv = iv.encode()
    plaintext = plaintext.encode()
    # 创建一个AES的加密对象
    cipher = AES.new(key, AES.MODE_CTR, iv)
    # 加密
    ciphertext = cipher.encrypt(plaintext)
    ciphertext_hex = binascii.hexlify(ciphertext)
    return ciphertext_hex


# 完成AES的CTR模式解密函数
def AES_CTR_Decrypt(key, iv, ciphertext):
    key = key.encode()
    iv = iv.encode()
    ciphertext = ciphertext.encode()
    ciphertext = binascii.unhexlify(ciphertext)
    # 创建一个AES的解密对象
    cipher = AES.new(key, AES.MODE_CTR, iv)
    # 解密
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


# 完成AES的OFB模式加密函数
def AES_OFB_Encrypt(key, iv, plaintext):
    key = key.encode()
    iv = iv.encode()
    plaintext = plaintext.encode()
    # 创建一个AES的加密对象
    cipher = AES.new(key, AES.MODE_OFB, iv)
    # 加密
    ciphertext = cipher.encrypt(plaintext)
    ciphertext_hex = binascii.hexlify(ciphertext)
    return ciphertext_hex


# 完成AES的OFB模式解密函数
def AES_OFB_Decrypt(key, iv, ciphertext):
    key = key.encode()
    iv = iv.encode()
    ciphertext = ciphertext.encode()
    ciphertext = binascii.unhexlify(ciphertext)
    # 创建一个AES的解密对象
    cipher = AES.new(key, AES.MODE_OFB, iv)
    # 解密
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


# 完成AES的CFB模式加密函数
def AES_CFB_Encrypt(key, iv, plaintext):
    key = key.encode()
    iv = iv.encode()
    plaintext = plaintext.encode()
    # 创建一个AES的加密对象
    cipher = AES.new(key, AES.MODE_CFB, iv)
    # 加密
    ciphertext = cipher.encrypt(plaintext)
    ciphertext_hex = binascii.hexlify(ciphertext)
    return ciphertext_hex


# 完成AES的CFB模式解密函数
def AES_CFB_Decrypt(key, iv, ciphertext):
    key = key.encode()
    iv = iv.encode()
    ciphertext = ciphertext.encode()
    ciphertext = binascii.unhexlify(ciphertext)
    # 创建一个AES的解密对象
    cipher = AES.new(key, AES.MODE_CFB, iv)
    # 解密
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# if __name__ == '__main__':
#     # 密钥
#     key = '12345679sssassss'
#     # 初始向量
#     iv = '12345679ssssssss'
#     # 明文
#     plaintext = 'csdscsd'
#     # 加密
#     ciphertext = AES_CFB_Encrypt(key, iv, plaintext)
#     print(ciphertext.decode())
#     # 解密
#     ciphertext=ciphertext.decode()
#     plaintext = AES_CFB_Decrypt(key, iv, ciphertext)
#     print(plaintext.decode())
