import hashlib
import TrinityPyDatabase
import secrets
from enum import Enum


class CreationErrors(Enum):
    AccountAlreadyExists = 1,

"""
Python implementation of SRP6 login by xlvan0ff:
https://gist.github.com/xIvan0ff/9e39c07cab8e03e1e51194a4406448ed
"""

def CalculateSRP6Verifier(username, password, salt):
    g = int(7)
    N = int("894B645E89E1535BBDAD5B8B290650530801B18EBFBF5E8FAB3C82872A3E9BB7", 16)
    userpassupper = f'{username}:{password}'.upper()
    h1 = hashlib.sha1(userpassupper.encode('utf-8')).digest()
    h2 = hashlib.sha1(salt + h1)
    h2 = int.from_bytes(h2.digest(), 'little')
    verifier = pow(g,h2,N)
    verifier = verifier.to_bytes(32, 'little')
    verifier = verifier.ljust(32, b'\x00')
    return verifier

def GetSRP6RegistrationData(username, password):
    salt = secrets.token_bytes(32)
    verifier = CalculateSRP6Verifier(username, password, salt)
    return [salt, verifier]

def VerifySRP6Login(username, password, salt, verifier):
    checkVerifier = CalculateSRP6Verifier(username, password, salt)
    return verifier == checkVerifier

def change_password(username, new_password):
    regdata = GetSRP6RegistrationData(username, new_password)
    TrinityPyDatabase.update_salt(username, regdata[0])
    TrinityPyDatabase.update_verifier(username, regdata[1])

def are_credentials_correct(username, password):
    salt = TrinityPyDatabase.get_salt(username)
    verifier = TrinityPyDatabase.get_verifier(username)
    return VerifySRP6Login(username, password, salt, verifier)

def create_account(username, password, email):
    if TrinityPyDatabase.user_exists(username):
        return CreationErrors.AccountAlreadyExists
    regdata = GetSRP6RegistrationData(username, password)
    TrinityPyDatabase.add_account_to_db(username, password, email, regdata[1], regdata[0])