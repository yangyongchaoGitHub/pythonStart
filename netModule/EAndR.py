# -*- coding: UTF-8 -*-
import base64
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

# message = 'hello ghost, this is a plian text'
# 伪随机数生成器
random_generator = Random.new().read

while 1:
    name_str = raw_input("输入功能选择(1：编码；2：解码):")
    if name_str[0] == '1':
        message = raw_input("输入需要编码的字符串:")
        with open('master-public.pem') as f:
            key = f.read()
            rsakey = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsakey)
            cipher_text = base64.b64encode(cipher.encrypt(message))
            print cipher_text
    else :
        encrypt_text = raw_input("输入需要解码的字符串:")
        with open('master-private.pem') as f:
            key = f.read()
            rsakey = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsakey)
            text = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
            print text
