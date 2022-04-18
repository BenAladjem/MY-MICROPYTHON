message = input()
message_id = 1
data_type = 1
#message_lenght = 1
start_bytes  = b'\x55\xaa'

def ByteToHex(byteStr):
    return " ".join(["{:02x}".format(x) for x in byteStr])

def dec_hex_byte(value, num_bytes):
    res = (value).to_bytes(num_bytes, byteorder='big')
    return res

def to_bytes_without_len(d):
    # Convert int to bytearray / unknown num of bytes, returns bytearray
    count = 0
    res = (d).to_bytes(7, 'big')
    print(res[0])
    for i in range(7):
        if res[i] != 0:
            count += 1
    result = (d).to_bytes(count, 'big')
    return result

def data_protokol(k_data, v_data, t_data ):
    #Чете всички Data и ги пакетира побитово по шаблона
    res = b''
    for i in range(len(k_data)):

        data = to_bytes_without_len(int(v_data[i]))
        data_len = dec_hex_byte(len(data), 1)
        data_type = dec_hex_byte(int(t_data), 1)
        data_type_id = dec_hex_byte(int(k_data[i]),2)
        res += (data_type_id +data_type + data_len +data)
    return res

def crc16(data: bytes, poly=0x8408):
    '''
    CRC-16-CCITT Algorithm
    '''
    data = bytearray(data)
    crc = 0xFFFF
    for b in data:
        cur_byte = 0xFF & b
        for _ in range(0, 8):
            if (crc & 0x0001) ^ (cur_byte & 0x0001):
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
            cur_byte >>= 1
    crc = (~crc & 0xFFFF)
    crc = (crc << 8) | ((crc >> 8) & 0xFF)

    return crc & 0xFFFF

command = message.split('&')
imei = int([x for x in command if "IMEI" in x][0].split('=')[1])
data = [x for x in command if "data" in x][0]
all_data = data.split('=')[1]
all_data = all_data.split(';')
keys_data = [x.split(',')[0] for x in all_data]
values_data = [x.split(',')[1] for x in all_data]
data_protokols = data_protokol(keys_data, values_data, data_type)

source_id = dec_hex_byte(imei, 7)
message_id = (message_id).to_bytes(1, 'big')

message_lenght = (len(start_bytes) + 1 + len(source_id) + 1 + len(data_protokols) + 2).to_bytes(1, 'big')
protokol = start_bytes + message_lenght + source_id+message_id + data_protokols
checksum = crc16(protokol)
protokol += checksum.to_bytes(2, 'big')


print(protokol)
print(ByteToHex(protokol))



m = 'IMEI=865456053906614&data=216,14241;222,55;210,40'
m1 = 'IMEI=865456053906614&data=216,14241;222,55;210,40&345&fgh&3ed&34'
m2 = 'IMEI=865456053906614&data=216,14241'