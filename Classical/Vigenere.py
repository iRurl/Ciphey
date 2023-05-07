# 加密：E=(m(i)+k(i))(mod 26)
# 解密：D=(c(i)-k(i))(mod 26)

psswd = 'abcdefghijklmnopqrstuvwxyz'
key = 'abcdefghijklmnopqrstuvwxyz'


def Encode_Vigenere(mnc: str, k: str):
    enc = ''
    j = 0
    try:
        for i in range(len(mnc)):
            if mnc[i].islower():
                enc += psswd[(psswd.index(mnc[i]) + psswd.index(k[j % len(k)].lower())) % 26]
                j += 1
            elif mnc[i].isupper():
                enc += psswd[(psswd.index(mnc[i].lower()) + psswd.index(k[j % len(k)].lower())) % 26].upper()
                j += 1
            else:
                enc += mnc[i]
        return enc
    except:
        return '加密失败，如果密钥中包含数字，请换表重试'


def Decode_Vigenere(enc: str, k: str):
    mnc = ''
    j = 0
    try:
        for i in range(len(enc)):
            if enc[i].islower():
                mnc += psswd[(psswd.index(enc[i]) - psswd.index(k[j % len(k)].lower())) % 26]
                j += 1
            elif enc[i].isupper():
                mnc += psswd[(psswd.index(enc[i].lower()) - psswd.index(k[j % len(k)].lower())) % 26].upper()
                j += 1
            else:
                mnc += enc[i]
        return mnc
    except:
        return '解密失败，如果密钥中包含数字，请换表重试'
