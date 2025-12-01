from Crypto.Hash.MD5 import MD5Hash
from Crypto.Hash.SHA1 import SHA1Hash

DEFAULT_STR_LIST = [
    b'ENSEA',
    b'eNSEA',
    b'eNSeA',
    b'EN5EA',
]

DEFAULT_BIG_STR_LIST = [
    open("data/BigText.txt").read().encode("utf-8")
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

def test_long_hash() -> None:
    print("============================== MD5 Long ==============================")
    for s in DEFAULT_BIG_STR_LIST:
        test_hash_md5 = MD5Hash(s)
        test_hash_sha_1 = SHA1Hash(s)
        print(f"Text as MD5 hash is {test_hash_md5.hexdigest()}")
        print(f"Text as SHA-1 hash is {test_hash_sha_1.hexdigest()}")


test_md5_hash()
test_sha_1_hash()
test_long_hash()