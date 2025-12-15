from base64 import b64decode
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

# Mot de passe
password = b"123PetitsChats"

# Sel encodé en Base64 (extrait du JSON)
salt_b64 = "JR53k2vFWO11bPrXZLcCYEE01fxSQhTy/8oWaco0bIs="
salt = b64decode(salt_b64)

# Paramètres PBKDF2
iterations = 600_000
key_length = 32  # 256 bits

# Dérivation de la clé
key = PBKDF2(
    password,
    salt,
    dkLen=key_length,
    count=iterations,
    hmac_hash_module=SHA256
)

# Affichage
print("Salt (hex) :", salt.hex())
print("Clé dérivée (hex) :", key.hex())
print("Taille de la clé :", len(key), "octets")
