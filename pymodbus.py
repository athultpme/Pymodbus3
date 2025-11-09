from pymodbus3.client.sync import ModbusTcpClient

inp = input(u"Press any key and enter to send a packet... (Just enter to quit)")

client = ModbusTcpClient('100.100.100.3')

while (inp):
    client.write_coil(1, True)
    result = client.read_coils(1, 1)
    print(result.bits[0])
    client.close()
    
    inp = input(u"Press any key and enter to send a packet... (Just enter to quit) ")
