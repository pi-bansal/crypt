from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def RSA_pair():
	key = RSA.generate(2048)
	private_PEM = key.export_key()
	public_PEM = key.publickey().export_key()
	return private_PEM,public_PEM
	
def AES_cipher():
	key = get_random_bytes(16)
	cipher = AES.new(key, AES.MODE_CBC)
	print(cipher)
