from hashlib import sha256
import hmac
import uuid

default_huk = b"\x00" * 32  # this is the default HUK if HUK retrieval is not supported
default_chip_id = bytes(
    [ord(i) for i in ["B", "E", "E", "F"] * 8]
)  # this is the default chip_id if chip_id retrieval is not supported
default_string = "ONLY_FOR_tee_fs_ssk"  # this is the default string for ssk generation


def get_tsk(uuid_tsk: uuid.UUID, ssk) -> bytes:
    return hmac.new(ssk, uuid_tsk.bytes, sha256).digest()


def get_ssk(
    string: str = default_string,
    huk: bytes = default_huk,
    chip_id: bytes = default_chip_id,
) -> bytes:
    print(default_chip_id)
    tmp = hmac.new(huk, chip_id, sha256)
    tmp.update(string.encode("ascii"))
    return tmp.digest()
