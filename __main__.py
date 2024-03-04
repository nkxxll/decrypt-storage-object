import argparse
import logging
from typing import Tuple

import decryptdata
import decryptfek

# Data
IV_OFFSET = 0
IV_SIZE = 16
TAG_OFFSET = IV_SIZE
TAG_SIZE = 16
DATA_OFFSET = (
    TAG_OFFSET + TAG_SIZE
)  # data goes until the end then it is padded by aes gcm algo

# Meta
ENC_FEK_OFFSET = 0
ENC_FEK_SIZE = decryptfek.FEK_SIZE


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
    arg_parser.add_argument(
        "-k", "--tsk", type=str, default=None, help="The TSK for the stored object"
    )
    return arg_parser.parse_args()


def get_fek():
    """get the FEK from the file"""
    return b"a" * 16


def get_iv_tag_data(file: str) -> Tuple[bytes, bytes, bytes]:
    """get the iv, tag and data from the file

    Args:
        file (str): the file with the stored object
    Returns:
        (bytes, bytes, bytes): the iv, tag and data
    """
    with open(file, "rb") as f:
        iv = f.read(12)
        tag = f.read(16)
        data = f.read()
    return iv, tag, data


def main():
    logger = logging.getLogger()
    args = get_args()
    enc_fek = get_fek()
    logger.debug(f"Args: {args}")

    tsk = bytes(args.tsk, "utf-8")
    dec_fek = decryptfek.decrypt(enc_fek, tsk)
    (iv, tag, data) = get_iv_tag_data(args.filename)
    dec_data = decryptdata.decrypt(iv, tag, data, dec_fek)
    print(f"dec_fek: {dec_fek}")
    print(f"dec_fek: {dec_data}")


main()
