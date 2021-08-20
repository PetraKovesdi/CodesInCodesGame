from passlib.hash import pbkdf2_sha256

import random
import string

HASHES = {
    "first": "$pbkdf2-sha256$29000$4VxL6Z3TutfaO6eUshbi3A$0Uv8CwngzKiRFUPropBEtUbGenK1YHNn9qZI6PL81Qk",
    "second": "$pbkdf2-sha256$29000$LgVgjLEWolQqBSBkrNWakw$83DOWkwpjlsv1S6aoV.0qUErQvrYJuzQHa9BVMZ7rFo",
    "third": "$pbkdf2-sha256$29000$aG2Ncc75f..9t/aeM8b4Hw$iPlY1Dr1PGeoSrLFn0DqLYOgy7wNyqyw/zcOvXqkwuM",
    "fourth": "$pbkdf2-sha256$29000$au2dM0aolVIqxZiTMmbMWQ$EradSGWN0FkQwNYMKvnI1WhEZQK6AczolPAyI8GG45E",
    "fifth": "$pbkdf2-sha256$29000$7r3X2ptzztm7d671PidECA$T5OSaBQas3SbN8wcWyeIEwEdUHESqkHul4G6x6UZ96I",
    "sixth": "$pbkdf2-sha256$29000$JmTMGeO8d85Z651TSiklBA$MjBcJTBxSZQBOHvqGV46R./UEf1oqyYCiaC2kkesGIk",
    "seventh": "$pbkdf2-sha256$29000$MEZoTel9j5GSco4xhvD.Pw$lyaeXKTtSUVZ7Eu8uxua1XKbaALFRmIBBZwPnAQcQKg",
    "eighth": "$pbkdf2-sha256$29000$McZYK0VIiRGiVKqVcu6dsw$7F1dP0i8sVKxKhuRV8f02KlZV5YlmnIY4ARbLXcNA5w"
}

ENCRYPTION_KEY = 5


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


def encryption_rail_fence(message):
    encryptionlist = []
    for i in range(ENCRYPTION_KEY):
        encryptionlist.append([])
    index = 0
    while index < len(message):
        listNumber = 0 #Resetting for next diagonal downwards
        reverseList = ENCRYPTION_KEY - 1 #Resetting for next diagonal upwards, - 1 to avoid adding bottom letter twice
        while listNumber < ENCRYPTION_KEY and index < len(message):
            letter = message[index]
            encryptionlist[listNumber].append(letter)
            listNumber += 1
            index += 1
        #reverseList > 1 to avoid adding letter to first list with 0 index twice, once downwards, once upwards
        while reverseList > 1 and index < len(message):
            letter = message[index]
            encryptionlist[reverseList - 1].append(letter) #reverseList - 1 to match indices
            reverseList -= 1
            index += 1
    encryptedMessage = ""
    for raillist in encryptionlist:
        for letter in raillist:
            encryptedMessage += letter
    return encryptedMessage



if __name__ == '__main__':
    print("Key generated:\n" + generate_key())
