from passlib.hash import pbkdf2_sha256

import random
import string

HASHES = {
    "first": "$pbkdf2-sha256$29000$4VxL6Z3TutfaO6eUshbi3A$0Uv8CwngzKiRFUPropBEtUbGenK1YHNn9qZI6PL81Qk",
    "second": "$pbkdf2-sha256$29000$LgVgjLEWolQqBSBkrNWakw$83DOWkwpjlsv1S6aoV.0qUErQvrYJuzQHa9BVMZ7rFo",
    "third": "$pbkdf2-sha256$29000$aG2Ncc75f..9t/aeM8b4Hw$iPlY1Dr1PGeoSrLFn0DqLYOgy7wNyqyw/zcOvXqkwuM",
    "fourth": "$pbkdf2-sha256$29000$au2dM0aolVIqxZiTMmbMWQ$EradSGWN0FkQwNYMKvnI1WhEZQK6AczolPAyI8GG45E",
    "fifth": "$pbkdf2-sha256$29000$7r3X2ptzztm7d671PidECA$T5OSaBQas3SbN8wcWyeIEwEdUHESqkHul4G6x6UZ96I",
    "sixth": "$pbkdf2-sha256$29000$JmTMGeO8d85Z651TSiklBA$MjBcJTBxSZQBOHvqGV46R./UEf1oqyYCiaC2kkesGIk"
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
