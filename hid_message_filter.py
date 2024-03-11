# Copyright (c) 2020 ruundii. All rights reserved.

from typing import Optional

class HIDMessageFilter:
    def filter_message_to_host(self, msg: bytes) -> Optional[bytes]:
        if len(msg) < 1:
            return None

        result_report = bytearray(msg)
        print(bytes(result_report).hex())

        if len(msg) == 9:
            msg = msg[1:]

        if msg[0] == 0x20:
            if 0x3a <= msg[2] and msg[2] <= 0x45:
                print("host switch")
                return bytes([0xff, msg[2] - 0x03a])

        return b'\xa1\x01' + msg


    def filter_message_from_host(self, msg: bytes) -> Optional[bytes]:
        return msg[1:]
