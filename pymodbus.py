from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('100.100.100.3')
inp = input("Press any key and enter to send a packet... (Just enter to quit)")
while inp:
    client.write_coil(1, True)
    result = client.read_coils(1, 1)
    print(result.bits[0])
    inp = input("Press any key and enter to send a packet... (Just enter to quit)")
client.close()
