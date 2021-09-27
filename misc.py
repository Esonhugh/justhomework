import base64

from Crypto.Cipher import ARC4
from hashlib import md5
from base64 import b64decode,b64encode


def debug(a):
    print(a,type(a))
# str in/out
def encrypt(msg :str, key :str):
    chiper = ARC4.new(key)
    return b64encode(chiper.encrypt(msg)).decode()
def decrypt (msg :str, key :str):
    chiper = ARC4.new(key)
    return chiper.decrypt(base64.b64decode(msg)).decode()

def hash(text :str):
    return md5(text.encode('utf-8')).hexdigest()

# print('ls',hash('ls'),type(hash('ls')))
# print('ls',key:='ls',msg:='ls',encrypt(msg,key),type(encrypt(msg,key)))
# print('ls',type(decrypt(encrypt('ls','ls'),'ls')))

urldata = [
    {
        "url": "/",
        "method": "GET",
        "varlist": "None",
        "return": "Api usage,This page."
    },
    {
        "url": "/question",
        "method": "GET",
        "varlist": "None",
        "return": "json"
    },
    {
        "url": "/answer",
        "method": "POST",
        "varlist": "post:answer(the use name)",
        "return": "json"
    },
    {
        "url":"/userdata",
        "method": "POST",
        "varlist": "user=username&image_url=image_url",
        "return": "json"
    }
]
