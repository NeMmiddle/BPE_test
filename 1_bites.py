def reversed_bytes(value) -> [bytes, int]:
    if 0 < value <= 65535:

        # Первый способ(он же и быстрее)
        # reverse_bytes = ((value % 256) << 8) | (value >> 8)
        # print(reverse_bytes)

        before_reverse = value.to_bytes(2, byteorder='big', signed=False)

        after_reverse = value.to_bytes(2, byteorder='little', signed=False)

        return f'До:    {before_reverse} - {int.from_bytes(before_reverse)} \n' \
               f'После: {after_reverse} - {int.from_bytes(after_reverse)}'


if __name__ == "__main__":
    print(reversed_bytes(int(input())))
