# 加密：j=(i+k)(mod n)
# 解密：i=(j-k)(mod n)

psswd = 'abcdefghijklmnopqrstuvwxyzx'


def Encode_Caser(mnc: str, key: int):
    try:

        enclow = ''
        enc = ''
        # 密文表
        for i in range(26):
            enclow += psswd[(i + key) % 26]
        # 密文匹配
        for i in range(len(mnc)):
            if 'A' <= mnc[i] <= 'Z':
                enc += enclow[psswd.index(mnc[i].lower())].upper()
            elif 'a' <= mnc[i] <= 'z':
                enc += enclow[psswd.index(mnc[i])]
            else:
                enc += mnc[i]
        # 打印密文
        return enc
    except:
        return '解密失败，请保证输入正确'


def Decode_Caser(enc: str, key: int):
    try:
        mnc = ''
        mnclow = ''
        # 明文表
        for i in range(26):
            mnclow += psswd[(i + (26 - key)) % 26]
        # 匹配明文
        for i in range(len(enc)):
            if 'A' <= enc[i] <= 'Z':
                mnc += mnclow[psswd.index(enc[i].lower())].upper()
            elif 'a' <= enc[i] <= 'z':
                mnc += mnclow[psswd.index(enc[i])]
            else:
                mnc += enc[i]
        # 打印明文
        return mnc
    except:
        return '解密失败，请保证输入正确'
