from math import gcd
from numpy import mat


def playfairTable(key):
    # 生成Playfair密码表格
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    table = []
    key = key.lower().replace('j', 'i')
    for letter in key + alphabet:
        if letter not in table and letter != 'j':
            table.append(letter)
    table = [table[i:i + 5] for i in range(0, 25, 5)]
    return table


def findPositions(table, letter):
    # 查找字母在Playfair密码表格中的位置
    row, col = 0, 0
    for i in range(5):
        for j in range(5):
            if table[i][j] == letter:
                row, col = i, j
    return row, col


def message_change(mnc):
    # 把i换成j
    mnc = mnc.lower().replace('j', 'i').replace(' ', '')
    # 将相邻字母替换为不同的字母
    new_mnc = ''
    for i in range(0, len(mnc), 2):
        if i == len(mnc) - 1 or mnc[i] == mnc[i + 1]:
            new_mnc += mnc[i] + 'x'
        else:
            new_mnc += mnc[i:i + 2]

    # 如果长度为奇数，则添加字母“x”
    if len(new_mnc) % 2 != 0:
        new_mnc += 'x'

    return new_mnc


def Encode_playfair(mnc: str, key: str):
    try:
        table = playfairTable(key)
        new_mnc = message_change(mnc)
        enc = ''
        for i in range(0, len(new_mnc), 2):
            row1, col1 = findPositions(table, new_mnc[i])
            row2, col2 = findPositions(table, new_mnc[i + 1])
            if row1 == row2:
                enc += table[row1][(col1 + 1) % 5]
                enc += table[row2][(col2 + 1) % 5]
            elif col1 == col2:
                enc += table[(row1 + 1) % 5][col1]
                enc += table[(row2 + 1) % 5][col2]
            else:
                enc += table[row1][col2]
                enc += table[row2][col1]

        # 删除添加的“x”字母
        if new_mnc[-1] == 'x':
            enc = enc[:-1]

        return enc
    except:
        return '加密失败，请保证输入正确(key中不可包含数字)'


def Decode_playfair(old_enc: str, key: str):
    try:
        table = playfairTable(key)
        # 使用Playfair密码进行解密
        enc = message_change(old_enc)
        mnc = ''
        for i in range(0, len(enc), 2):
            row1, col1 = findPositions(table, enc[i])
            row2, col2 = findPositions(table, enc[i + 1])
            if row1 == row2:
                mnc += table[row1][(col1 - 1) % 5]
                mnc += table[row2][(col2 - 1) % 5]
            elif col1 == col2:
                mnc += table[(row1 - 1) % 5][col1]
                mnc += table[(row2 - 1) % 5][col2]
            else:
                mnc += table[row1][col2]
                mnc += table[row2][col1]
        # 删除添加的“x”字母
        if mnc[-1] == 'x':
            mnc = mnc[:-1]

        return mnc
    except:
        return '解密失败，请保证输入正确（key中不可包含数字）'
