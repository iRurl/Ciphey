# 加密：j=(i*k1+k0)(mod n)
# 解密：i=k1^(-1)(j-k0)(mod n)

psswd = 'abcdefghijklmnopqrstuvwxyz'


def niYuan(a, n):
    for Ni in range(n):
        if Ni * a % n == 1:
            return Ni


def Encode_Affine(mnc: str, key0: int, key1: int):
    try:
        enclist = ''
        enc = ''
        # 计算密文表
        for i in range(26):
            enclist += psswd[(i * key1 + key0) % 26]
        # 密文表匹配1
        for i in range(len(mnc)):
            if mnc[i].islower():
                enc += enclist[psswd.index(mnc[i])]
            elif mnc[i].isupper():
                enc += (enclist[psswd.index(mnc[i].lower())]).upper()
            else:
                enc += mnc[i]
        # 打印密文
        return enc
    except:
        return '加密失败，请保证输入正确'


def Decode_Affine(enc: str, key0: int, key1: int):
    try:
        mnclist = ''
        mnc = ''
        # 计算key1的逆元
        key1Ni = niYuan(key1, 26)
        # 明文列表
        for i in range(26):
            mnclist += psswd[(key1Ni * (i - key0)) % 26]
        # 明文匹配
        for i in range(len(enc)):
            if enc[i].isupper():
                mnc += mnclist[psswd.index(enc[i].lower())].upper()
            elif enc[i].islower():
                mnc += mnclist[psswd.index(enc[i])]
            else:
                mnc += enc[i]
        # 打印明文
        return mnc
    except:
        return '解密失败，请保证输入正确'
