import requests
import json
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64 import b64decode

def create_encryption(url, username, password):
    url = f"{url}/create_encryption"
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=payload)
    data = response.json()
    encrypted_value = data["encrypted_value"]
    private_key = data["private_key"]
    return encrypted_value, private_key

def decrypt_and_verify(url, username, password, encrypted_value):
    private_key = RSA.import_key(password)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_value = cipher_rsa.decrypt(b64decode(encrypted_value)).decode("utf-8")
    
    url = f"{url}/verify_decryption"
    payload = {
        "username": username,
        "password": password,
        "decrypted_value": decrypted_value
    }
    response = requests.post(url, json=payload)
    data = response.json()
    return data["message"]

def execute_sql(url, username, password, sql_query):
    url = f"{url}/execute_sql"
    payload = {
        "username": username,
        "password": password,
        "sql": sql_query
    }
    response = requests.post(url, json=payload)
    data = response.json()
    return data["message"]

if __name__ == "__main__":
    username = "abc"
    password = "123"
    url = "http://0.0.0.0:5000"
    encrypted_value, private_key = create_encryption(username, password)
    decryption_result = decrypt_and_verify(username, private_key, encrypted_value)
    if decryption_result == "驗證成功":
        sql_query = "SELECT * FROM your_table"
        sql_execution_result = execute_sql(username, password, sql_query)
        print(sql_execution_result)
    else:
        print("解密驗證失敗")
