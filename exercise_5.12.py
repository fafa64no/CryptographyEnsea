from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512

mnemonic = "witch collapse practice feed shame open despair creek road again ice least"
passphrase = "mnemonic" 


iterations = 2048
key_length = 64  


seed = PBKDF2(
    mnemonic,
    ("mnemonic" + passphrase).encode('utf-8'), 
    dkLen=key_length,
    count=iterations,
    hmac_hash_module=SHA512
)


print("Seed (hex) :", seed.hex())
print("Taille de la seed :", len(seed), "octets")
