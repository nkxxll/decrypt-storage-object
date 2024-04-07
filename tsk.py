from generatetsk import *
from uuid import UUID

uuid = UUID(
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


def main() -> None:
    print("start")
    ssk = get_ssk()
    for integer in ssk:
        print(int(integer))
    tsk = get_tsk(uuid, ssk)
    print(tsk)
    print("end")


main()
