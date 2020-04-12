
from Crypto.Cipher import AES 
from Crypto import Random


import os
import base64
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC



class enc_class(object):

  
    def __init__(self):
        BLOCK_SIZE=16
        self.pad=lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
        


    def generate_key(self,password_provided):
        self.key=hashlib.sha256(password_provided.encode("utf-8")).digest()

    def encrypt(self,raw):    
        raw = self.pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return  base64.b64encode(iv + cipher.encrypt(raw.encode())) 