import random
import string
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_with_aes(input: str, enc_key: str, iv: str):
    key = enc_key.encode()
    nonce = iv.encode()
    plaintext = input.encode()
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    # Change the encrypted bytes to a readable Base64 string
    ciphertext_str = base64.b64encode(ciphertext).decode()
    return ciphertext_str

def decrypt_with_aes(input: str, enc_key: str, iv: str):
    key = enc_key.encode()
    nonce = iv.encode()
    ciphertext = base64.b64decode(input)
    aesgcm = AESGCM(key)
    decrypted = aesgcm.decrypt(nonce, ciphertext, None)
    return decrypted.decode()

def generate_iv_string(length=16):
    # Create a random string for the nonce
    chars = string.ascii_letters + string.digits + "#$()*+,-.:;<=>?@[]_"
    return ''.join(random.choices(chars, k=length))

key = AESGCM.generate_key(bit_length=256)
enc_key = "1Xt5YfM4ZNuFdwp3OfVkwkhhQLagWKtt"  # 32-character secret key
iv = generate_iv_string(12)  # make a random nonce/iv

choice = input("For Encrypt type: 1\n"
               "For Decrypt type: 2\n"
               "Input: ")

if choice == "1":
    input_text = input("\nEnter text to encrypt: ")

    iv = generate_iv_string()

    ciphertext = encrypt_with_aes(input_text, enc_key, iv)

    print("\n===== ENCRYPTION RESULT =====")
    print("Ciphertext:", ciphertext)
    print("IV:", iv)

elif choice == "2":
    ciphertext = input("\nEnter ciphertext: ")
    iv = input("Enter IV: ")

    try:
        decrypted = decrypt_with_aes(ciphertext, enc_key, iv)

        print("\n===== DECRYPTION RESULT =====")
        print("Decrypted text:", decrypted)
    except Exception:
        print("\nError: Invalid ciphertext, key or IV.")
else:
        print("\nInvalid choice. Please choose 1 or 2.")