import key_gen
import datetime
import jwt

user_id = 'Pi'

payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }

print(payload)
private_key,public_key = key_gen.RSA_pair()

encoded_jwt = jwt.encode(payload,private_key,algorithm='RS256')

print(encoded_jwt)

decoded_payload = jwt.decode(encoded_jwt,public_key)

print(decoded_payload)

print(payload == decoded_payload)

