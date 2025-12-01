import Crypto
from Crypto.Hash.MD5 import MD5Hash
from Crypto.Hash.SHA1 import SHA1Hash

DEFAULT_STR_LIST = [
    b'ENSEA',
    b'eNSEA',
    b'eNSeA',
    b'EN5EA',
]

def test_md5_hash() -> None:
    print("============================== MD5 ==============================")
    for s in DEFAULT_STR_LIST:
        test_hash = MD5Hash(s)
        print(f"{s} as MD5 hash is {test_hash.hexdigest()}")

def test_sha_1_hash() -> None:
    print("============================== SHA-1 ==============================")
    for s in DEFAULT_STR_LIST:
        test_hash = SHA1Hash(s)
        print(f"{s} as SHA-1 hash is {test_hash.hexdigest()}")


test_md5_hash()
test_sha_1_hash()