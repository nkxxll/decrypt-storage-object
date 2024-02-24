"""decrypt FEK form the encrypted object file"""


def decrypt(encrypted_fek: bytes, tsk: bytes, tsk_len: int):
    print(f"encrypted_fek {encrypted_fek}, tsk: {tsk}, tsk_len: {tsk_len}")
