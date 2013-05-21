import serial, binascii, time, config, devices

ser = serial.Serial(config.serialPort, config.serialBaud, timeout=2)

lamp = devices.d.switchLinc('165257')
#lamp = insteonDeviceTypes.applianceLinc('1480CC') 
#garage = insteonDeviceTypes.ioLinc('15E5A5')
tvalve = "03"

##garage
#ser.write(binascii.a2b_hex(garage.outputOn('01')))
#s2 = binascii.b2a_hex(ser.read(20))
#ser.write(binascii.a2b_hex(garage.outputOff('01')))
#s2 = binascii.b2a_hex(ser.read(20))

ser.write(binascii.a2b_hex(devices.garage.outputOn('01')))
s2 = binascii.b2a_hex(ser.read(20))
print "command: " + devices.garage.outputOn('01')
print "reply:   " + s2 + "   %%"
print "----"
   
time.sleep(20)

ser.write(binascii.a2b_hex(devices.garage.outputOff('01')))
s2 = binascii.b2a_hex(ser.read(20))

print "command: " + devices.garage.outputOff('01')
print "reply:   " + s2 + "   %%"

