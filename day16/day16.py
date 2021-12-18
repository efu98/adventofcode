hex2bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
    }


def conv2bin(msg):
    bin_msg = ''
    for char in msg:
        bin_msg += hex2bin[char]
    return bin_msg


def read_message(msg):
    print(msg)
    pack_vers = int(msg[0:3], 2)
    pack_type = int(msg[3:6], 2)

    msg = msg[6:]
    # literal value
    if pack_type == 4:
        value = ''
        packet_size = 6
        while msg[0] == '1':
            value += msg[1:5]
            msg = msg[5:]
            packet_size += 5
        value += msg[1:5]
        print(int(value, 2))
        msg = msg[5:]
        packet_size += 5
        return packet_size, pack_vers

    else:
        if msg[0] == '0':
            subpack_length = int(msg[1:16], 2)
            msg = msg[16:]
            read_size = 0
            while read_size != subpack_length:
                pack_length, subpack_vers = read_message(msg)
                pack_vers += subpack_vers
                msg = msg[pack_length:]
                read_size += pack_length
            return subpack_length+7+15, pack_vers

        else:
            subpack_numb = int(msg[1:12], 2)
            msg = msg[12:]
            subpack_length = 0
            for _ in range(subpack_numb):
                pack_length, subpack_vers = read_message(msg)
                subpack_length += pack_length
                pack_vers += subpack_vers
                msg = msg[pack_length:]
            return subpack_length+7+11, pack_vers


def part_one():

    with open("input", "r") as f:
        messages = [msg.strip() for msg in f.readlines()]
        for msg in messages:
            msg = conv2bin(msg)
            print(read_message(msg))


part_one()
