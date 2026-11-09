import base64
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def get_key():
    key = AESGCM.generate_key(bit_length=256)
    print("\nGegenereerde sleutel:")
    print(base64.b64encode(key).decode())
    return key

def load_key():
    key_b64 = input("Plak de eerder gegenereerde sleutel: ")
    return base64.b64decode(key_b64)

def encrypt_with_aes(plaintext: str, key: bytes, nonce: bytes):
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)
    ciphertext_str = base64.b64encode(ciphertext).decode()
    return ciphertext_str

def decrypt_with_aes(ciphertext_b64: str, key: bytes, nonce: bytes):
    ciphertext = base64.b64decode(ciphertext_b64)
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext.decode()

def generate_nonce(length=12) -> bytes:
    return os.urandom(length)

choice = input("For Encrypt type: 1\n"
               "For Decrypt type: 2\n"
               "Input: ")

if choice == "1":
    key = get_key()
    input_text = input("\nEnter text to encrypt: ")

    nonce = generate_nonce()

    ciphertext = encrypt_with_aes(input_text, key, nonce)

    print("\n===== ENCRYPTION RESULT =====")
    print("Ciphertext:", ciphertext)
    print("Nonce:", base64.b64encode(nonce).decode())

elif choice == "2":
    key = load_key()

    ciphertext = input("\nEnter ciphertext: ")
    nonce_b64 = input("Enter Nonce: ")
    nonce = base64.b64decode(nonce_b64)

    try:
        decrypted = decrypt_with_aes(ciphertext, key, nonce)

        print("\n===== DECRYPTION RESULT =====")
        print("Decrypted text:", decrypted)
    except Exception:
        print("\nError: Invalid ciphertext, key or Nonce.")
else:
        print("\nInvalid choice. Please choose 1 or 2.")