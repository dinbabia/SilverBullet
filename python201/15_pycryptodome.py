"""
pycryptodome - fork of pycrypto library that has been enhanced to add
more functionality and also security fixes to the original pycrypto library

Resources
----------
https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
https://en.wikipedia.org/wiki/Public-key_cryptography
https://en.wikipedia.org/wiki/Symmetric-key_algorithm
https://en.wikipedia.org/wiki/Digital_signature
https://en.wikipedia.org/wiki/Message_authentication_code
https://en.wikipedia.org/wiki/Cryptographic_hash_function
https://en.wikipedia.org/wiki/Salt_(cryptography)
https://en.wikipedia.org/wiki/Padding_(cryptography)
https://en.wikipedia.org/wiki/RC4
https://en.wikipedia.org/wiki/RSA_(cryptosystem)
https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding
https://en.wikipedia.org/wiki/Secure_Hash_Algorithms
"""
from Crypto.Random import get_random_bytes

# A symmetric cipher, 32 bytes
key = get_random_bytes(32)
print(key)
print(len(key))

# --------------------------

from Crypto.Protocol.KDF import PBKDF2
# salt - used to help prevent against dictionary based attacks
# - value doesn't necessarily need to be kept secret, but it should be random for each derivation.
salt = get_random_bytes(32)
password = "asdfgh123" # secret password to generate our key
key = PBKDF2(password, salt, dkLen=32)
print(key)
print(len(key))

# --------------------------

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

to_encrypt = b"encrypt meee"
# CBC - Cipher Blockchaining
cipher = AES.new(key, AES.MODE_CBC)
# iv - initialiazation vector
print(cipher.iv)
ciphered_data = cipher.encrypt(pad(to_encrypt, AES.block_size))
print(ciphered_data)

## WHEN decrypting, we need to be aware that a cipher object is stateful.
## That means, once we've already encrypted a message, we can't also perform decryption with that same object.
# cipher = AES.new(key, AES.MODE_CBC)
# plaintext_data = cipher.decrypt(ciphered_data)
## plaintext_data - still have jumbled data and not the specific string/messsage anymore, because
## we're using another random iv
# print(plaintext_data)

# TO fix that, we need that cipher.iv
# We will also add 'unpad' to remove the padding
cipher = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
plaintext_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
print(plaintext_data)

# -------------------------
# symmetric stream ciphers
from Crypto.Cipher import ARC4

cipher = ARC4.new(key)
encrypted = cipher.encrypt(to_encrypt)
print(encrypted)

cipher = ARC4.new(key)
plaintext = cipher.decrypt(encrypted)
print(plaintext)


# NOTE: If we wanna encrpyt data with an asymmetric cipher such as rsa, then you will need to either have access to
# a public and private RSA key pair, depending on what you are trying to do....or you can generate your own....

from Crypto.PublicKey import RSA

key = RSA.generate(1024)
encrypted_key = key.exportKey(passphrase=password)
print(encrypted_key)

pub = key.publickey()
print(pub.exportKey())

# checks the capability for encrypting data for the key
print(key.can_encrypt())
# checks whether we can sign messages with this key
print(key.can_sign())
# will return true if the private key is present in the object
print(key.has_private())
print(pub.has_private())

# NOTE: We can now use the keys to perform encryption. However, we can ONLY encrypt messages which are slightly shorter than
# the RSA modulus.
# But for this lesson, it's fine because  our encryption messages is also small, though we need to make use of padding.

# ----------------------------

# Optimal Asymmetric encryption padding / OAEP
# padding scheme often used together with RSA encryption

from Crypto.Cipher import PKCS1_OAEP

cipher = PKCS1_OAEP.new(pub)
encrypted = cipher.encrypt(to_encrypt)
print(encrypted)

cipher = PKCS1_OAEP.new(key)
plaintext = cipher.decrypt(encrypted)
print(plaintext)

# --------------------------------

# NOTE: We can also use the key to create and verify digital signature
# Digital Signatures - are based on a public key cryptography concept.
# Whoever signs a message, needs to have the private key, and whoever wants to verify the signature has to have the public key.

from Crypto.Hash import SHA512

plain_hash = SHA512.new(to_encrypt).digest()
hashed = int.from_bytes(plain_hash, byteorder='big')
print(f"Hashed: {hashed}")

# Calculate signature by raising the hash to the power D, modular N, using python's 'pow'
# d and n values - we created when we set up our key.
signature = pow(hashed, key.d, key.n)
print(f"Signature: {signature}")

# Verify it by raising signature to the power e modulo N, using the key material from our public key.
signature_hash = pow(signature, key.e, key.n)
print(f"Signature 2: {signature_hash}")

