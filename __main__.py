import argparse
import uuid
import logging
from typing import Tuple

import decryptdata
import decryptfek
import generatetsk

# Data
IV_OFFSET = 0
IV_SIZE = 12
TAG_OFFSET = IV_SIZE
TAG_SIZE = 16
DATA_OFFSET = (
    TAG_OFFSET + TAG_SIZE
)  # data goes until the end then it is padded by aes gcm algo

# Meta
ENC_FEK_OFFSET = 0
ENC_FEK_SIZE = decryptfek.FEK_SIZE

logging.basicConfig(level=logging.DEBUG)

# 0xf4e750bb, 0x1437, 0x4fbf, 0x87, 0x85, 0x8d, 0x35, 0x80, 0xc3, 0x49, 0x94
"""uuid from the seal-key TA"""
TA_UUID = uuid.UUID(
    bytes=bytes(
        [
            0xF4,
            0xE7,
            0x50,
            0xBB,
            0x14,
            0x37,
            0x4F,
            0xBF,
            0x87,
            0x85,
            0x8D,
            0x35,
            0x80,
            0xC3,
            0x49,
            0x94,
        ]
    )
)


def get_args():
    """get the arguments for the cli program

    The arguments consist of filename, and TSK which is a 16 or 32 bit key for decryption.
    """

    arg_parser = argparse.ArgumentParser(
        description="Cli app that should decrypt a optee storage object with the knowledge of the tsk and the encrypted storage object file"
    )
    arg_parser.add_argument(
        "-f", "--file", type=str, default=None, help="The file with the stored object"
    )
    # we generate the tsk now
    # arg_parser.add_argument(
    #     "-k", "--tsk", type=str, default=None, help="The TSK for the stored object"
    # )
    return arg_parser.parse_args()


def get_enc_fek(filename: str):
    """get the FEK from the file"""
    with open(filename, "rb") as f:
        return f.read(16)


def get_iv_tag_data(filename: str) -> Tuple[bytes, bytes, bytes]:
    """get the iv, tag and data from the file

    Args:
        file (str): the file name with the stored object
    Returns:
        (bytes, bytes, bytes): the iv, tag and data
    """
    with open(filename, "rb") as f:
        content = f.read()
        iv = content[IV_OFFSET : IV_OFFSET + IV_SIZE]
        tag = content[TAG_OFFSET : TAG_OFFSET + TAG_SIZE]
        data = content[TAG_OFFSET + TAG_SIZE :]
    return iv, tag, data


def open_file_add(dict_: dict, file: str):
    with open(file, "r") as f:
        tmp = f.read()
        dict_[file] = tmp


def tsk_file_to_bytes(tsks: dict):
    for k, tsk in tsks:
        tsks[k] = [int.to_bytes(int(integer)) for integer in tsk.split("\n")]


def try_decrypt(meta_file_name, data_file_name):
    enc_fek = get_enc_fek(meta_file_name)
    ssk = generatetsk.get_ssk()
    tsk = generatetsk.get_tsk(TA_UUID, ssk)

    # ,----------------------.
    # |Meta block            |  ,----------------------.
    # |----------------------|  |Data block            |
    # |16 Bytes encrypted FEK|  |----------------------|
    # |==                    |  |12 Data IV            |
    # |12 Meta IV            |  |==                    |
    # |==                    |  |16 Tag                |
    # |... tag               |  |==                    |
    # |==                    |  |...rest encrypted data|
    # |encrypted meta data   |  `----------------------'
    # `----------------------'

    dec_fek = decryptfek.decrypt(enc_fek, tsk)

    # let's try to first use the 0 as meta data and the 1 a block data then the other way
    iv: bytes = b""
    tag: bytes = b""
    data: bytes = b""
    logging.debug(f"decrypted fek:{dec_fek}")
    # read the file contents of the data block
    (iv, tag, data) = get_iv_tag_data(data_file_name)
    logging.debug("-------")
    logging.debug(f"iv:{iv}, tag: {tag} data:{data}")
    logging.debug("-------")
    try:
        dec_data = decryptdata.decrypt(iv=iv, tag=tag, data=data, password=dec_fek)
        logging.debug(f"decrypted data:{dec_data}")
    except:
        logging.debug("didn't work")


def main():
    # args = get_args()
    # logging.debug(f"Args: {args}")
    # I don't know if this works I don't want to delete it but it could be utter shit
    # open_file_add(files, "./fixtures/0")
    # open_file_add(files, "./fixtures/1")
    # open_file_add(files, "./fixtures/2")
    # open_file_add(tsks, "./fixtures/tsk")
    # open_file_add(tsks, "./fixtures/tsk2")

    # kiss keep it simple stupid
    # if args.file is not None:
    #     files["args_file"] = args.file
    logging.debug("hello")

    try_decrypt("./fixtures/new/1", "./fixtures/new/2")
    # ==> the other way
    try_decrypt("./fixtures/new/2", "./fixtures/new/1")
    try_decrypt("./fixtures/new/0", "./fixtures/new/1")
    # ==> the other way
    try_decrypt("./fixtures/new/1", "./fixtures/new/0")


main()
