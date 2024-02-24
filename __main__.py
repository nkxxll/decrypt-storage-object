import argparse
import logging

import decryptfek


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
    return "a" * 16


def main():
    logger = logging.getLogger()
    args = get_args()
    enc_fek = get_fek()
    logger.debug(f"Args: {args}")

    tsk = bytes(args.tsk, "utf-8")
    dec_fek = decryptfek.decrypt(enc_fek, tsk, len(tsk))
    print(f"dec_fek: {dec_fek}")


main()
