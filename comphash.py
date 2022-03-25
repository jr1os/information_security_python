# compatator hash with hashlib

import hashlib

arq1 = "a.txt"
arq2 = "b.txt"

hash1 = hashlib.new('ripemd160')
hash1.update(open(arq1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arq2, 'rb').read())


if hash1.digest() != hash2.digest():
    print(f"file {arq1} {hash1.digest()} is different file {arq2} {hash2.digest()}")
else:
    print(f"file {arq1} {hash1.digest()} is equal file {arq2} {hash2.digest()}")
