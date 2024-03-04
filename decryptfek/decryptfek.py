"""decrypt FEK form the encrypted object file"""
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB

FEK_SIZE = 16
TSK_SIZE = 32


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
    # safety first
    assert len(tsk) == TSK_SIZE, f"TSK size is wrong! TSK size: {TSK_SIZE}"
    assert len(encrypted_fek) == FEK_SIZE, f"FEK size is wrong! FEK size: {FEK_SIZE}"
    mode = ECB()
    aes = AES(tsk)
    cipher = Cipher(aes, mode)
    decryptor = cipher.decryptor()
    res: bytes = decryptor.update(encrypted_fek) + decryptor.finalize()
    assert len(res) == 16
    return res
