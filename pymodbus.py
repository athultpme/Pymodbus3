from pymodbus.client.sync import ModbusTcpClient

inp = input("Press any key and enter to send a packet... (Just enter to quit): ")

client = ModbusTcpClient('100.100.100.3')

while inp:
    client.write_coil(1, True)
    result = client.read_coils(1, 1)
    print(result.bits[0])
    client.close()
    
    inp = input("Press any key and enter to send a packet... (Just enter to quit): ")