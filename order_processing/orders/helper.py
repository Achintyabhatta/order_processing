import jwt, base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as decryptionPadding
from cryptography.hazmat.backends import default_backend
from datetime import date as d, datetime as dt
import os, requests

def NewAuthenticateJWTtoken(request):

    # Load your public RSA key
    with open('customer/key/_._.pharmacy_jwt_pass.click.pkcs8', 'rb') as public_key_file:
        public_key = serialization.load_pem_public_key(
            public_key_file.read(),
            backend=default_backend()
        )

    response = {"mobileNumber" : "", "isValid" : False }

    try:
        jwt_token = request.headers.get('authorization', None)
        jwt_token_bytes = base64.b64decode(jwt_token.encode('utf-8'))
        jwt_token = jwt_token_bytes.decode('utf-8')
    except:
        return response

    try:
        # payload = jwt.decode(jwt_token, JWT_SECRET,algorithms=[JWT_ALGORITHM])
        payload = jwt.decode(jwt_token, public_key, algorithms=['RS256'])
        response = {"mobileNumber": payload["mobileNumber"], "isValid" : True }
    except jwt.DecodeError:
        print(f"JWT Token Decode Error LOG : {str(jwt.DecodeError)}")
    except jwt.ExpiredSignatureError:
        print(f"JWT Token Expired Signature Error LOG : {str(jwt.ExpiredSignatureError)}")
    
    return response

def getInventoryDetailForOrder(itemID):
    url = "" #TODO : Add Inventory URL
    response = requests.post(url, json = {}, headers = {})
    response = response.json()
    return response["data"]

def IncrementInventoryCount(itemID, count):
    url = "" #TODO : Add Inventory URL
    params = {"itemID" : itemID, "count" : count }
    response = requests.post(url, json = params, headers = {})
    response = response.json()
    if response.status_code == 200:
        return True
    return False

def DecrementInventoryCount(itemID, count):
    url = "" #TODO : Add Inventory URL
    params = {"itemID" : itemID, "count" : count }
    response = requests.post(url, json = params, headers = {})
    response = response.json()
    if response.status_code == 200:
        return True
    return False

