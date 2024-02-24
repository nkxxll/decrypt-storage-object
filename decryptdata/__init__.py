from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import GCM


def decrypt(iv: bytes, tag: bytes, data: bytes, password: bytes) -> bytes:
    """decrypt the data with aes gcm

    Decrypt the data with the iv, tag and password using AES in GCM mode.
    Args:
        iv (bytes): the iv
        tag (bytes): the tag
        data (bytes): the data
        password (bytes): the password
    Returns:
        bytes: the decrypted data
    """
    assert len(password) == 16
    aes = AES(password)
    cipher = Cipher(aes, GCM(iv, tag))
    decryptor = cipher.decryptor()
    res: bytes = decryptor.update(data) + decryptor.finalize()
    return res
