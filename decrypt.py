from Crypto.Cipher import AES 
from Crypto import Random
import os
import base64
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC





class decpt_data(object):

    def __init__(self):
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    
    def generate_key(self,password_provided):
        
        password_r = password_provided.encode('utf-8') # Convert to type bytes
        salt = os.urandom(32) 
        key_r=hashlib.sha256(password_r).digest()
        return key_r
       


    def decrypt(self,enc,key):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[16:]))
        