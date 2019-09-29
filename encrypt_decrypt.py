
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import datetime


user_id = 'Pi'
key = get_random_bytes(32)
print(key)
cipher = AES.new(key, AES.MODE_CTR)
print(cipher)
payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id,
            'This is a long key':'This is a very very very long value string'
        }

cipher_text = cipher.encrypt(bytes(str(payload),'utf-8'))

print(cipher_text)



#print(bytes(str(payload),'utf-8'))
