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


def operation(values, type_id):
    if type_id == 0:
        return sum(values)

    elif type_id == 1:
        mult = 1
        for v in values:
            mult *= v
        return mult

    elif type_id == 2:
        return min(values)

    elif type_id == 3:
        return max(values)

    elif type_id == 5:
        if values[0] > values[1]:
            return 1
        return 0

    elif type_id == 6:
        if values[0] < values[1]:
            return 1
        return 0

    else:
        if values[0] == values[1]:
            return 1
        return 0


def read_packet(msg):
    version = int(msg[0:3], 2)
    type_id = int(msg[3:6], 2)

    msg = msg[6:]

    # literal value
    if type_id == 4:
        value = ''
        packet_size = 6

        # read value group starting with 1
        while msg[0] == '1':
            value += msg[1:5]
            msg = msg[5:]
            packet_size += 5

        # read last value group starting with 0
        value += msg[1:5]
        msg = msg[5:]
        packet_size += 5

        return packet_size, version, int(value, 2)

    # operator
    else:
        if msg[0] == '0':
            data_length = int(msg[1:16], 2)
            msg = msg[16:]
            read_size = 0
            values = []

            # read subpackets until the length of data read is reached
            while read_size != data_length:
                pack_length, subpack_vers, subvalue = read_packet(msg)
                version += subpack_vers
                values.append(subvalue)
                read_size += pack_length
                msg = msg[pack_length:]

            return read_size+7+15, version, operation(values, type_id)

        else:
            subpack_numb = int(msg[1:12], 2)
            msg = msg[12:]
            read_size = 0
            values = []

            # read subpackets until the number of packets read is reached
            for _ in range(subpack_numb):
                pack_length, subpack_vers, subvalue = read_packet(msg)
                version += subpack_vers
                values.append(subvalue)
                read_size += pack_length
                msg = msg[pack_length:]

            return read_size+7+11, version, operation(values, type_id)


def part_one():

    with open("input", "r") as f:
        msg = f.readline().strip()
        msg = conv2bin(msg)

        return read_packet(msg)[1]


def part_two():

    with open("input", "r") as f:
        msg = f.readline().strip()
        msg = conv2bin(msg)

        return read_packet(msg)[2]


print(part_two())
