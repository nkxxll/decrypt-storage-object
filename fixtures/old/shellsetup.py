from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import GCM

with open("tsk", "r") as f:
    lines = f.readlines()
    key = b""
    for line in lines:
        byte = int(line).to_bytes(1, "big")
        key += byte

print(key)
# cipher = Cipher(AES(key), GCM(iv, tag=tag))
# fek =
