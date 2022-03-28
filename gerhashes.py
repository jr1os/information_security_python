import hashlib


def hash_encry(string):
    result = hashlib.md5(string.encode('utf-8'))
    return result.hexdigest()


if __name__ == "__main__":
    print(hash_encry("python security with hash"))
