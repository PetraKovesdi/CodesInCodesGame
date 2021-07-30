from passlib.hash import pbkdf2_sha256

import random
import string

HASHES = {
    "first": "$pbkdf2-sha256$29000$4VxL6Z3TutfaO6eUshbi3A$0Uv8CwngzKiRFUPropBEtUbGenK1YHNn9qZI6PL81Qk"
}

def gethashes(row):
    return HASHES.get(row)


def make_hash(code):
    hash = pbkdf2_sha256.hash(code)
    return hash

def verify_code(code,hash):
    verify = pbkdf2_sha256.verify(code, hash)
    return verify

def generate_key():
    letters = [random.choice(string.ascii_letters) for i in range(10)]
    digits = [random.choice(string.digits) for i in range(10)]
    chars = [random.choice(string.punctuation) for i in range(5)]
    keyList = letters+digits+chars
    random.shuffle(keyList)
    key = "".join(keyList)
    return key

if __name__ == '__main__':
    print("Key generated:\n" + generate_key())
    print(make_hash('937451'))