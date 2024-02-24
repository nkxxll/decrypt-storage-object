"""decrypt FEK form the encrypted object file"""
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB


def decrypt(encrypted_fek: bytes, tsk: bytes) -> bytes:
    """decrypt the FEK with the TSK

    Decrypt the FEK with the TSK using AES in ECB mode.
    The TSK is either 32 bytes long the length of the hmac sha256 output.
    Args:
        encrypted_fek (bytes): the encrypted FEK
        tsk (bytes): the TSK
    Returns:
        bytes: the decrypted FEK
    """
    assert len(tsk) == 32
    assert len(encrypted_fek) == 16
    mode = ECB()
    aes = AES(tsk)
    cipher = Cipher(aes, mode)
    decryptor = cipher.decryptor()
    res: bytes = decryptor.update(encrypted_fek) + decryptor.finalize()
    assert len(res) == 16
    return res
