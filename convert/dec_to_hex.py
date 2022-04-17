import byte as byte

message = input()
message_id = 1
data_type = 1
message_lenght = 1
start_bytes = ["55", "aa"]  #21930


def dec_hex_byte(a):
    c = [x for x in hex(a)[2:]]
    #c = c[2:]
    if len(c) % 2 != 0:
        c.insert(0, '0')
    result = []
    for i in range(0, len(c), 2):
        result.append(c[i] + c[i + 1])
    return result

def data_protokol(k_data, v_data, t_data):
    res = []
    for i in range(len(k_data)):

        data = dec_hex_byte(int(v_data[i]))
        data_len = dec_hex_byte(len(data))
        data_type = dec_hex_byte(int(t_data))
        if int(k_data[i]) < 256:
            data_type_id = ["00"]
            data_type_id.append(dec_hex_byte(int(k_data[i]))[0])
        else:
            data_type_id = dec_hex_byte(int(k_data[i]))
        [res.append(x) for x in data_type_id]
        #res.append(data_type_id[0])
        [res.append(x) for x in data_type]
        #res.append(data_type[0])
        [res.append(x) for x in data_len]
        #res.append(data_len[0])
        [res.append(x) for x in data]



    return res


def crc16(data: byte, poly=0x1021, offset=0, length=0):
    '''
    CRC-16-CCITT Algorithm
    '''
    data = bytearray(data)
    crc = 0xFFFF
    for i in range(0, length):
        crc ^= data[offset + i] << 8
        for j in range(0, 8):
            if (crc & 0x8000) > 0:
                crc = (crc << 1) ^ poly
            else:
                crc = crc << 1

    return crc & 0xFFFF


command = message.split('&')
imei = int([x for x in command if "IMEI" in x][0].split('=')[1])
data = [x for x in command if "data" in x][0]
all_data = data.split('=')[1]
all_data = all_data.split(';')
keys_data = [x.split(',')[0] for x in all_data]
values_data = [x.split(',')[1] for x in all_data]


source_id_hex = dec_hex_byte(imei)
# print(source_id_hex)
# print(data)
# print(all_data)
# print(keys_data)
# print(values_data)
m = 'IMEI=865456053906614&data=216,14241;222,55;210,40'
m1 = 'IMEI=865456053906614&data=216,14241;222,55;210,40&345&fgh&3ed&34'
m2 = 'IMEI=865456053906614&data=216,14241'

data_protokols = data_protokol(keys_data, values_data, data_type)
message_lenght += len(start_bytes) + len(source_id_hex) + len(data_protokols)
protokol = start_bytes+dec_hex_byte(message_lenght)+source_id_hex+data_protokols
print(protokol)

p = ''.join([x for x in protokol])
print(p)

print(crc16(p))





