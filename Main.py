import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style

from tkinter.filedialog import askopenfilename

from Classical import Caser, playfair
from Classical.Affine import *
from Classical.Vigenere import *
from Classical.乘法密码 import *
from Cryptodome.Util.number import getPrime

from Nowadays import AES, DES

import gmpy2
import libnum

from RSA import Text_tips as tips
from OpenSSL import crypto
from RSA import RSA as R_rsa
from RSA import Rsa_npq
import rsa
from Algorithm.Hash import *

style = Style(theme="morph")  # 使用的主题名称
root = style.master

# root = tk.Tk()
root.geometry('1150x700')
root.title('密码学工具箱 by iRuri')

# 建立一个notebook，对不同的加密方式进行分类
notebook = ttk.Notebook(root)
# 三个选项卡，分别对应古典密码、现代密码、RSA
Classical = tk.Frame()
Nowadays = tk.Frame()
RSA = tk.Frame()
Algorithm = tk.Frame()
Rsa_2 = tk.Frame()

global Public_key
global Private_key
'''  #############################################  框架显示  #############################################  '''
# 两个文本框，用于输入和输出  Class中
input_Class = tk.Text(Classical, width=158, height=12)
input_Class.place(x=6, y=30)
output_Class = tk.Text(Classical, width=158, height=12)
output_Class.place(x=6, y=435)

# 两个文本框，用于输入和输出  Nowadays中
input_Now = tk.Text(Nowadays, width=158, height=12)
input_Now.place(x=6, y=30)
output_Now = tk.Text(Nowadays, width=158, height=12)
output_Now.place(x=6, y=435)

# 两个文本框，用于输入和输出  RSA中
input_RSA = tk.Text(RSA, width=158, height=12)
input_RSA.place(x=6, y=30)
output_RSA = tk.Text(RSA, width=158, height=12)
output_RSA.place(x=6, y=435)

# 两个文本框，用于输入和输出  摘要算法中
input_Alg = tk.Text(Algorithm, width=158, height=12)
input_Alg.place(x=6, y=30)
output_Alg = tk.Text(Algorithm, width=158, height=12)
output_Alg.place(x=6, y=435)

# 两个文本框，用于输入和输出 Rsa中
input_Rsa_2 = tk.Text(Rsa_2, width=158, height=4)
input_Rsa_2.place(x=6, y=30)
Rsa_p = tips.Gen_Text(Rsa_2, "p")
Rsa_p.place(x=6, y=120, width=400, height=80)
Rsa_q = tips.Gen_Text(Rsa_2, "q")
Rsa_q.place(x=415, y=120, width=400, height=80)
Rsa_e = tips.Gen_Text(Rsa_2, "e")
Rsa_e.place(x=825, y=120, width=300, height=80)
Rsa_n = tips.Gen_Text(Rsa_2, "n")
Rsa_n.place(x=6, y=210, width=1118, height=80)
Rsa_d = tips.Gen_Text(Rsa_2, "d {[无需填写]}")
Rsa_d.place(x=6, y=300, width=1118, height=80)

output_Rsa_2 = tk.Text(Rsa_2, width=158, height=12)
output_Rsa_2.place(x=6, y=435)

'''  #############################################  Classical加解密实现  #############################################  '''


# 根据选项，对不同的加密方式进行加解密
def run_Classical():
    # 清空output_Class中的内容
    output_Class.delete(1.0, tk.END)
    try:
        # 凯撒加密
        if v_class.get() == 1 and type_class.get() == 1:
            # 获取input_Class中的明文
            plaintext = input_Class.get(1.0, tk.END).rstrip()
            # 获取key_Class_entry1中的密钥
            Class_key = key_Class_entry1.get()
            # 调用凯撒密码的加密函数
            ciphertext = Caser.Encode_Caser(plaintext, int(Class_key))
            # 将加密后的密文显示在output_Class中
            output_Class.insert(tk.END, ciphertext)
        # 凯撒解密
        elif v_class.get() == 2 and type_class.get() == 1:
            plaintext = input_Class.get(1.0, tk.END).rstrip()
            Class_key = key_Class_entry1.get()
            ciphertext = Caser.Decode_Caser(plaintext, int(Class_key))
            output_Class.insert(tk.END, ciphertext)
        # playfair加密
        elif v_class.get() == 1 and type_class.get() == 2:
            plaintext = input_Class.get(1.0, tk.END).rstrip()
            Class_key = key_Class_entry1.get()
            ciphertext = playfair.Encode_playfair(plaintext, Class_key)
            output_Class.insert(tk.END, ciphertext)
        # playfair解密
        elif v_class.get() == 2 and type_class.get() == 2:
            plaintext = input_Class.get(1.0, tk.END).rstrip()
            Class_key = key_Class_entry1.get()
            ciphertext = playfair.Decode_playfair(plaintext, Class_key)
            output_Class.insert(tk.END, ciphertext)
        # 乘法加密
        elif v_class.get() == 1 and type_class.get() == 3:
            plaintext = input_Class.get(1.0, tk.END).rstrip()
            Class_key = key_Class_entry1.get()
            ciphertext = Encode_Mul(plaintext, int(Class_key))
            output_Class.insert(tk.END, ciphertext)
        # 乘法解密
        elif v_class.get() == 2 and type_class.get() == 3:
            plaintext = input_Class.get(1.0, tk.END).rstrip()
            Class_key = key_Class_entry1.get()
            ciphertext = Decode_Mul(plaintext, int(Class_key))
            output_Class.insert(tk.END, ciphertext)
        # Affine加密
        elif v_class.get() == 1 and type_class.get() == 4:
            plaintext = input_Class.get(1.0, tk.END).rstrip()
            key1 = key_Class_entry2.get()
            key2 = key_Class_entry3.get()
            ciphertext = Encode_Affine(plaintext, int(key1), int(key2))
            output_Class.insert(tk.END, ciphertext)
        # Affine解密
        elif v_class.get() == 2 and type_class.get() == 4:
            plaintext = input_Class.get(1.0, tk.END).rstrip()
            key1 = key_Class_entry2.get()
            key2 = key_Class_entry3.get()
            ciphertext = Decode_Affine(plaintext, int(key1), int(key2))
            output_Class.insert(tk.END, ciphertext)
        # Vigenere加密
        elif v_class.get() == 1 and type_class.get() == 5:
            plaintext = input_Class.get(1.0, tk.END).rstrip()
            Class_key = key_Class_entry1.get()
            ciphertext = Encode_Vigenere(plaintext, Class_key)
            output_Class.insert(tk.END, ciphertext)
        # Vigenere解密
        elif v_class.get() == 2 and type_class.get() == 5:
            plaintext = input_Class.get(1.0, tk.END).rstrip()
            Class_key = key_Class_entry1.get()
            ciphertext = Decode_Vigenere(plaintext, Class_key)
            output_Class.insert(tk.END, ciphertext)
    except:
        output_Class.insert(tk.END, "输入有误，请检查输入！")


''' #############################################  Nowadays加解密实现  #############################################'''


def run_Nowadays():
    output_Now.delete(1.0, tk.END)
    '''#####################   DES加解密   ######################'''
    # DES CBC模式加密
    try:
        if v_now.get() == 1 and type_now.get() == 1 and mode_now.get() == 'CBC':
            # 不保留行尾换行符
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = DES.DES_CBC_Encrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # DES ECB模式加密
        elif v_now.get() == 1 and type_now.get() == 1 and mode_now.get() == 'ECB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            ciphertext = DES.DES_ECB_Encrypt(Now_key, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # DES CFB模式加密
        elif v_now.get() == 1 and type_now.get() == 1 and mode_now.get() == 'CFB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = DES.DES_CFB_Encrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # DES OFB模式加密
        elif v_now.get() == 1 and type_now.get() == 1 and mode_now.get() == 'OFB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = DES.DES_OFB_Encrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # DES CTR模式加密
        elif v_now.get() == 1 and type_now.get() == 1 and mode_now.get() == 'CTR':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = DES.DES_CTR_Encrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # DES CBC模式解密
        elif v_now.get() == 2 and type_now.get() == 1 and mode_now.get() == 'CBC':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = DES.DES_CBC_Decrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # DES ECB模式解密
        elif v_now.get() == 2 and type_now.get() == 1 and mode_now.get() == 'ECB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            ciphertext = DES.DES_ECB_Decrypt(Now_key, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # DES CFB模式解密
        elif v_now.get() == 2 and type_now.get() == 1 and mode_now.get() == 'CFB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = DES.DES_CFB_Decrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # DES OFB模式解密
        elif v_now.get() == 2 and type_now.get() == 1 and mode_now.get() == 'OFB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = DES.DES_OFB_Decrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # DES CTR模式解密
        elif v_now.get() == 2 and type_now.get() == 1 and mode_now.get() == 'CTR':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = DES.DES_CTR_Decrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
    except:
        output_Now.insert(tk.END,
                          '输入有误，请保证输入正确！{[key与IV要求为8个字符]、[密文要求16进制 无空格分割 ]、[明文要求为字符串] }')

    '''#####################   AES加解密   ######################'''
    try:
        # AES CBC模式加密
        if v_now.get() == 1 and type_now.get() == 2 and mode_now.get() == 'CBC':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = AES.AES_CBC_Encrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # AES ECB模式加密
        elif v_now.get() == 1 and type_now.get() == 2 and mode_now.get() == 'ECB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            ciphertext = AES.AES_ECB_Encrypt(Now_key, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # AES CFB模式加密
        elif v_now.get() == 1 and type_now.get() == 2 and mode_now.get() == 'CFB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = AES.AES_CFB_Encrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # AES OFB模式加密
        elif v_now.get() == 1 and type_now.get() == 2 and mode_now.get() == 'OFB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = AES.AES_OFB_Encrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # AES CTR模式加密
        elif v_now.get() == 1 and type_now.get() == 2 and mode_now.get() == 'CTR':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = AES.AES_CTR_Encrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # AES CBC模式解密
        elif v_now.get() == 2 and type_now.get() == 2 and mode_now.get() == 'CBC':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = AES.AES_CBC_Decrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # AES ECB模式解密
        elif v_now.get() == 2 and type_now.get() == 2 and mode_now.get() == 'ECB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            ciphertext = AES.AES_ECB_Decrypt(Now_key, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # AES CFB模式解密
        elif v_now.get() == 2 and type_now.get() == 2 and mode_now.get() == 'CFB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = AES.AES_CFB_Decrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # AES OFB模式解密
        elif v_now.get() == 2 and type_now.get() == 2 and mode_now.get() == 'OFB':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = AES.AES_OFB_Decrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
        # AES CTR模式解密
        elif v_now.get() == 2 and type_now.get() == 2 and mode_now.get() == 'CTR':
            plaintext = input_Now.get(1.0, tk.END).rstrip()
            Now_key = key_Now_entry.get()
            IV = IV_Now_entry.get()
            ciphertext = AES.AES_CTR_Decrypt(Now_key, IV, plaintext)
            output_Now.insert(tk.END, ciphertext)
    except:
        output_Now.insert(1.0,
                          '输入有误，请保证输入正确！{[key与IV要求为16个字符]、[密文要求16进制 无空格分割 ]、[明文要求为字符串] }')


''' #############################################  RSA加解密实现  ############################################# '''


def run_RSA():
    try:
        output_RSA.delete(1.0, tk.END)
        if v_rsa.get() == 1:
            plaintext = input_RSA.get(1.0, tk.END).rstrip()
            Public_key = RSA_public_key.get()
            ciphertext = R_rsa.RSA_Encrypt(Public_key.encode(), plaintext)
            output_RSA.insert(1.0, ciphertext)
        elif v_rsa.get() == 2:
            plaintext = input_RSA.get(1.0, tk.END).rstrip()
            Private_key = RSA_private_key.get()
            ciphertext = R_rsa.RSA_Decrypt(Private_key.encode(), plaintext)
            output_RSA.insert(1.0, ciphertext)
    except:
        output_RSA.delete(1.0, tk.END)
        output_RSA.insert(1.0,
                          '输入有误，请保证输入正确！{[密钥要求为pkcs1填充]、[密文要求16进制 无空格分割 ]、[明文要求为字符串] }')


''' #############################################  Hash摘要算法实现  ############################################# '''


def run_Algorithm():
    output_Alg.delete(1.0, tk.END)
    try:
        text = input_Alg.get(1.0, tk.END).rstrip()
        output_Alg.delete(1.0, tk.END)
        if type_hash.get() == 1:
            Hash_text = md5(text)
            print(Hash_text)
            output_Alg.insert(1.0, Hash_text)
        elif type_hash.get() == 2:
            Hash_text = sha_1(text)
            output_Alg.insert(1.0, Hash_text)
        elif type_hash.get() == 3:
            Hash_text = sha_256(text)
            output_Alg.insert(1.0, Hash_text)
        elif type_hash.get() == 4:
            Hash_text = sm_3(text)
            output_Alg.insert(1.0, Hash_text)
    except:
        output_Alg.insert(1.0, '输入有误，请保证输入正确！{[明文要求为字符串] }')


''' #############################################  Rsa摘要算法实现  ############################################# '''


def run_Rsa():
    output_Rsa_2.delete(1.0, tk.END)
    try:
        rsa_p = Rsa_p.get(1.0, tk.END)
        rsa_q = Rsa_q.get(1.0, tk.END)
        rsa_n = Rsa_n.get(1.0, tk.END)
        rsa_e = Rsa_e.get(1.0, tk.END)
        if v_Rsa.get() == 1:
            plantext = input_Rsa_2.get(1.0, tk.END).rstrip()
            Cipher = Rsa_npq.encrypt_Rsa(int(rsa_p), int(rsa_q), int(rsa_n), int(rsa_e), str(plantext))
            output_Rsa_2.delete(1.0, tk.END)
            output_Rsa_2.insert(1.0, Cipher)
        elif v_Rsa.get() == 2:
            ciphertext = input_Rsa_2.get(1.0, tk.END).rstrip()
            rsa_d, plantext = Rsa_npq.decrypt_Rsa(int(rsa_p), int(rsa_q), int(rsa_n), int(rsa_e), str(ciphertext))
            Rsa_d.delete(1.0, tk.END)
            Rsa_d.insert(1.0, rsa_d)
            output_Rsa_2.delete(1.0, tk.END)
            output_Rsa_2.insert(1.0, plantext)
    except:
        output_Rsa_2.insert(1.0, '输入有误，请保证输入正确！{[ 密文要求输入hex值 ]、[ 明文要求输入字符串 ] }')


def Gen_Key():
    rsa_p = getPrime(1024)
    rsa_q = getPrime(1024)
    n = rsa_p * rsa_q
    phi = (rsa_p - 1) * (rsa_q - 1)
    e = libnum.generate_prime(16)
    Rsa_p.delete(1.0, tk.END)
    Rsa_p.insert(1.0, rsa_p)
    Rsa_q.delete(1.0, tk.END)
    Rsa_q.insert(1.0, rsa_q)
    Rsa_n.delete(1.0, tk.END)
    Rsa_n.insert(1.0, n)
    Rsa_e.delete(1.0, tk.END)
    Rsa_e.insert(1.0, e)


def Cal_n():
    output_Rsa_2.delete(1.0, tk.END)
    try:
        rsa_p = Rsa_p.get(1.0, tk.END)
        rsa_q = Rsa_q.get(1.0, tk.END)
        n = int(rsa_p) * int(rsa_q)
        Rsa_n.delete(1.0, tk.END)
        Rsa_n.insert(1.0, n)
    except:
        output_Rsa_2.insert(1.0, '输入有误，请保证输入正确！{[ 请输入整形的p、q值 ] }')


''' #############################################   整体界面美化    #############################################  '''
# 一个按钮，用于加密和加密的运行 Class中
encrypt_button = tk.Button(Classical, text='->Crack', width=10, height=1, command=run_Classical)
encrypt_button.place(x=600, y=390)

# 一个按钮，用于加密和加密的运行 Nowadays中
encrypt_button = tk.Button(Nowadays, text='->Crack', width=10, height=1, command=run_Nowadays)
encrypt_button.place(x=600, y=390)

# 一个按钮，用于加密和加密的运行 RSA中
encrypt_button = tk.Button(RSA, text='->Crack', width=10, height=1, command=run_RSA)
encrypt_button.place(x=600, y=390)

# 一个按钮，用于加密和加密的运行 Algorithm中
encrypt_button = tk.Button(Algorithm, text='->Crack', width=10, height=1, command=run_Algorithm)
encrypt_button.place(x=600, y=390)

# 一个按钮，用于加密和加密的运行 Rsa中
encrypt_button = tk.Button(Rsa_2, text='->Crack', width=10, height=1, command=run_Rsa)
encrypt_button.place(x=600, y=390)

# 一个按钮，用于生成 Rsa中的密钥
encrypt_button = tk.Button(Rsa_2, text='Gen_Key', width=10, height=1, command=Gen_Key)
encrypt_button.place(x=800, y=390)

# 一个按钮，用于计算Rsa中的n
encrypt_button = tk.Button(Rsa_2, text='计算{n}', width=10, height=1, command=Cal_n)
encrypt_button.place(x=900, y=390)

# 两个标签，用于显示
encrypt_label = tk.Label(root, text='待处理')
encrypt_label.place(x=16, y=41)
decrypt_label = tk.Label(root, text='输出内容')
decrypt_label.place(x=16, y=445)

''' #####################################   在Class中加入加解密的Radiobutton    ########################################  '''

Class_select = {
    '加密': 1,
    '解密': 2
}
v_class = tk.IntVar()
v_class.set(1)
for i, (k, v) in enumerate(Class_select.items()):
    Class_Crack = tk.Radiobutton(Classical, text=k, variable=v_class, value=v, width=5)
    Class_Crack.place(x=400 + i * 100, y=390)

''' ########################################   在Nowadays中加入加解密的Radiobutton    #####################################  '''
Now_select = {
    '加密': 1,
    '解密': 2
}
v_now = tk.IntVar()
v_now.set(1)
for i, (k, v) in enumerate(Now_select.items()):
    Now_Crack = tk.Radiobutton(Nowadays, text=k, variable=v_now, value=v, width=5)
    Now_Crack.place(x=400 + i * 100, y=390)

''' #######################################    在RSA中加入加解密的Radiobutton    #######################################  '''

RSA_select = {
    '加密': 1,
    '解密': 2
}
v_rsa = tk.IntVar()
v_rsa.set(1)
for i, (k, v) in enumerate(RSA_select.items()):
    RSA_Crack = tk.Radiobutton(RSA, text=k, variable=v_rsa, value=v, width=5)
    RSA_Crack.place(x=400 + i * 100, y=390)

''' #######################################    在RSA中加入加解密的Radiobutton    #######################################  '''

Rsa_select = {
    '加密': 1,
    '解密': 2
}
v_Rsa = tk.IntVar()
v_Rsa.set(1)
for i, (k, v) in enumerate(Rsa_select.items()):
    Rsa_Crack = tk.Radiobutton(Rsa_2, text=k, variable=v_Rsa, value=v, width=5)
    Rsa_Crack.place(x=400 + i * 100, y=390)

''' #######################################    将选项卡加入到notebook中    #######################################  '''
notebook.add(Classical, text='古典密码')
notebook.add(Nowadays, text='对称密码')
notebook.add(RSA, text='RSA')
notebook.add(Algorithm, text='摘要算法')
notebook.add(Rsa_2, text='Rsa')
notebook.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

'''#############################################   在Class中根据选择加入显示的key    ###########################################'''

key_Class_label1 = tk.Label(Classical, text='Key')
key_Class_entry1 = tk.Entry(Classical, width=20)
key_Class_label2 = tk.Label(Classical, text='Key₀')
key_Class_entry2 = tk.Entry(Classical, width=20)
key_Class_label3 = tk.Label(Classical, text='Key₁')
key_Class_entry3 = tk.Entry(Classical, width=20)


def dis_Class_key():
    key_Class_label1.place_forget()
    key_Class_entry1.place_forget()
    key_Class_label2.place_forget()
    key_Class_entry2.place_forget()
    key_Class_label3.place_forget()
    key_Class_entry3.place_forget()
    if type_class.get() == 1 or type_class.get() == 2 or type_class.get() == 5 or type_class.get() == 3:
        # 显示key1
        key_Class_label1.place(x=450, y=340)
        key_Class_entry1.place(x=500, y=340)

    elif type_class.get() == 4:
        key_Class_label2.place(x=334, y=340)
        key_Class_entry2.place(x=380, y=340)
        key_Class_label3.place(x=540, y=340)
        key_Class_entry3.place(x=580, y=340)


'''#############################################   在Class中的加解密方法    ###########################################'''
Class_type = {
    '凯撒密码': 1,
    'Playfair密码': 2,
    '乘法密码': 3,
    'Affine密码': 4,
    'Vigenere密码': 5,
}
type_class = tk.IntVar()
type_class.set(0)
for i, (k, v) in enumerate(Class_type.items()):
    Class_Cipher = tk.Radiobutton(Classical, text=k, variable=type_class, value=v, width=10, command=dis_Class_key)
    Class_Cipher.place(x=100 + i * 200, y=280)

'''###########################################   在Nowadays中根据选择加入显示的key  ###########################################'''


def dis_Now_key():
    key_Now_label.place_forget()
    key_Now_entry.place_forget()
    IV_Now_label.place_forget()
    IV_Now_entry.place_forget()
    if (type_now.get() == 1 or type_now.get() == 2) and mode_now.get() == 'ECB':
        key_Now_label.place(x=450, y=330)
        key_Now_entry.place(x=500, y=330)
    elif (type_now.get() == 1 or type_now.get() == 2) and mode_now.get() != 'ECB':
        key_Now_label.place(x=300, y=330)
        key_Now_entry.place(x=350, y=330)
        IV_Now_label.place(x=550, y=330)
        IV_Now_entry.place(x=600, y=330)


def dis_IV(self):
    key_Now_label.place_forget()
    key_Now_entry.place_forget()
    IV_Now_label.place_forget()
    IV_Now_entry.place_forget()
    if type_now.get() != 0:
        dis_Now_key()


'''#############################################   在Nowadays中的加解密方法    ###########################################'''
Now_type = {
    'DES': 1,
    'AES': 2
}
key_Now_label = tk.Label(Nowadays, text='Key')
key_Now_entry = tk.Entry(Nowadays, width=20)
IV_Now_label = tk.Label(Nowadays, text='IV')
IV_Now_entry = tk.Entry(Nowadays, width=20)
type_now = tk.IntVar()
type_now.set(0)
for i, (k, v) in enumerate(Now_type.items()):
    Now_Cipher = tk.Radiobutton(Nowadays, text=k, variable=type_now, value=v, width=10, command=dis_Now_key)
    Now_Cipher.place(x=300 + i * 400, y=280)

'''###########################################   在Nowadays中加入加密模式    ###########################################'''

mode_now = tk.StringVar()
mode_now.set('ECB')
# 设置一个下拉框,包含ECB,CBC,CFB,OFB,CTR五种模式
mode_now_chosen = ttk.Combobox(Nowadays, width=12, textvariable=mode_now)
mode_now_chosen.bind("<<ComboboxSelected>>", dis_IV)
mode_now_chosen['values'] = ('ECB', 'CBC', 'CFB', 'OFB', 'CTR')
mode_now_chosen.place(x=500, y=270)

'''#############################################   在RSA中的密钥管理   ###########################################'''
# 生成两个文本框，分别用于输入公钥和私钥
RSA_public_key = tips.Gen_Entry(RSA, "请输入公钥")
RSA_private_key = tips.Gen_Entry(RSA, "请输入私钥")
RSA_public_key.place(width=300, height=30, x=150, y=260)
RSA_private_key.place(width=300, height=30, x=650, y=260)

RSA_key_len = tips.Gen_Entry(RSA, "密钥长度")
RSA_key_len.place(width=60, height=30, x=520, y=260)


# 生成公钥的函数，用于生成公钥，并且将公钥的文件放在RSA目录的Generate_Key目录下
def get_key_len():
    if RSA_key_len.get() == '密钥长度':
        return 2048
    else:
        return int(RSA_key_len.get())


def Insert_Public_key(public_key):
    RSA_public_key.focus_set()
    RSA_public_key.delete(0, tk.END)
    RSA_public_key.insert(0, public_key)


def Insert_Private_key(private_key):
    RSA_private_key.focus_set()
    RSA_private_key.delete(0, tk.END)
    RSA_private_key.insert(0, private_key)


def Gen_Public_Private_key():
    RSA_key = crypto.PKey()
    RSA_key.generate_key(crypto.TYPE_RSA, get_key_len())
    Private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, RSA_key)
    Public_key = crypto.dump_publickey(crypto.FILETYPE_PEM, RSA_key)

    Insert_Public_key(Public_key.decode())
    Insert_Private_key(Private_key.decode())

    with open('RSA/Generate_Key/private_key.pem', 'wb') as f:
        f.write(Private_key)
    f.close()
    with open('RSA/Generate_Key/public_key.pem', 'wb') as f:
        f.write(Public_key)
    f.close()


# 生成两个按钮，分别用于生成公钥和私钥
RSA_public_Private_key_button = tk.Button(RSA, text='生成公私钥', command=Gen_Public_Private_key)
RSA_public_Private_key_button.place(width=100, height=30, x=500, y=300)


# 打开公钥和私钥文件
def Open_Public_key():
    # 打开文件资源管理器
    Open = tk.Tk()
    Open.withdraw()  # 隐藏Tk窗口
    # 打开一个文件选择对话框
    file_path = askopenfilename()
    with open(file_path, 'rb') as f:
        Public_key = f.read()
    f.close()
    RSA_public_key.delete(0, tk.END)
    RSA_public_key.insert(0, Public_key.decode())


def Open_Private_key():
    # 打开文件资源管理器
    Open = tk.Tk()
    Open.withdraw()  # 隐藏Tk窗口
    # 打开一个文件选择对话框
    file_path = askopenfilename()
    with open(file_path, 'rb') as f:
        Private_key = f.read()
    f.close()
    RSA_private_key.delete(0, tk.END)
    RSA_private_key.insert(0, Private_key.decode())


# 生成两个打开文件，用于打开公钥和私钥
RSA_public_key_open = tk.Button(RSA, text='打开公钥', command=Open_Public_key)
RSA_private_key_open = tk.Button(RSA, text='打开私钥', command=Open_Private_key)
RSA_public_key_open.place(width=100, height=30, x=150, y=300)
RSA_private_key_open.place(width=100, height=30, x=850, y=300)

'''###########################################   在Algorithm中加入不同模式    ###########################################'''
Hash_type = {
    'MD5': 1,
    'SHA-1': 2,
    'SHA-256': 3,
    'SM-3': 4
}
type_hash = tk.IntVar()
type_hash.set(0)
for i, (k, v) in enumerate(Hash_type.items()):
    Hash_Cipher = tk.Radiobutton(Algorithm, text=k, variable=type_hash, value=v, width=10)
    Hash_Cipher.place(x=200 + i * 200, y=300)

# 设置不可改变窗口大小以及设置循环轮播
root.resizable(False, False)
root.mainloop()
