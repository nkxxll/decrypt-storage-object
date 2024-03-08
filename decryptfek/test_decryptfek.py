import decryptfek

FIXTURES_PATH = "../fixtures/"


def test_decrypt():
    """test the decrypton of the FEK that was retrieved from the OPTEE"""
    with open(FIXTURES_PATH + "keys.bin", "rb") as f:
        data = f.read()
    fek: bytes = data[:16]
    enc_fek: bytes = data[16:32]
    tsk: bytes = data[32:]
    assert len(fek) == 16
    assert len(enc_fek) == 16
    assert len(tsk) == 32
    decrypted_fek: bytes = decryptfek.decrypt(enc_fek, tsk)
    assert fek == decrypted_fek
