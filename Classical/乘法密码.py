# 加密：E(ai)=aj   j=i*k(mod n)
# 解密：i=j*k^(-1)(mod n)

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def niYuan(a, n):
    a = int(a)
    n = int(n)
    for Ni in range(n):
        if Ni * a % n == 1:
            return int(Ni)


def Encode_Mul(mnc: str, key: int):
    try:
        enclow = ''
        encup = ''
        encnum = ''
        enc = ''
        # 得到加密后的密码表
        for i in range(26):
            enclow += lower[i * key % 26]
            encup += upper[i * key % 26]
        # 加密
        for i in range(len(mnc)):
            if 'a' <= mnc[i] <= 'z':
                enc += enclow[lower.index(mnc[i])]

            elif 'A' <= mnc[i] <= 'Z':
                enc += encup[upper.index(mnc[i])]
            else:
                enc += mnc[i]
        # 打印密文
        return enc
    except:
        return '解密失败，请保证输入正确'


def Decode_Mul(enc: str, key: int):
    try:
        mnclow = ''
        mncup = ''
        mncnum = ''
        mnc = ''
        # 得到解密后的明文表
        for i in range(26):
            mnclow += lower[(i * niYuan(key, 26)) % 26]
            mncup += upper[(i * niYuan(key, 26)) % 26]
        # 解密
        for i in range(len(enc)):
            if 'a' <= enc[i] <= 'z':
                mnc += mnclow[lower.index(enc[i])]

            elif 'A' <= enc[i] <= 'Z':
                mnc += mncup[upper.index(enc[i])]
            else:
                mnc += enc[i]
        # 打印明文
        return mnc
    except:
        return '解密失败，请保证输入正确'
