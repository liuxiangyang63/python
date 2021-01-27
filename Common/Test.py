# coding=utf-8
from binascii import b2a_hex, a2b_hex
from Crypto.Cipher import AES
import base64


def decrypt1(text):
    key = '8QaOlwAfQ+Mwyngw'.encode('utf-8')
    # key = bytes('8QaOlwAfQ+Mwyngw',)
    print(key)
    mode = AES.MODE_ECB
    cryptos = AES.new(key, mode)
    # encryptString = bytes(text, 'utf-8')
    # print(type(encryptString))
    # encryptString1 = a2b_hex(text)
    # encryptString12 = b2a_hex(encryptString)
    result = []
    for i in range(0, int(len(text) / 2) + 1):
        high = int(text[i * 2])
        low = int(hex(text[i * 2 + 1])) % 16
        to = high * 16 + low
        tt = bytes(to)
        result.__add__(tt)
    res = bin(int(text, 16))
    print(encryptString)
    plain_text = cryptos.decrypt(result)
    return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    e = '0BF2D8E51F3E7E44453CE8C7C92EB082'
    d = decrypt1(e)  # 解密
    print("解密:", d)
