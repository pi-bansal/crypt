from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import base64
import datetime
cipher = AES.new(key, AES.MODE_CTR)

plain_text = cipher.decrypt(cipher_text)

print((plain_text))
