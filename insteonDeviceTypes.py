import  config, insteonCommands as ic

class generic:
    ''' This class in meant to be inherited by
    other device classes to prevent redundant use
    of general commands like on/off
    '''
    def __init__(self,deviceID):
        self.id = deviceID
    def on(self,level=config.onLevel):
        self.FLAGS = '00'
        print ( "%X" % level )
        self.EXEC = ic.PRE + self.id + self.FLAGS + ic.ON.cmd1 + ( "%X" % level )
        return(self.EXEC)
    def off(self):
        self.FLAGS = '00'
        self.LEVEL = '00'
        self.EXEC = ic.PRE + self.id + self.FLAGS + ic.OFF.cmd1 + self.LEVEL
        return(self.EXEC)
    def beep(self,duration):
        self.FLAGS = '00'
        self.EXEC = ic.PRE + self.id + self.FLAGS + ic.BEEP.cmd1 + duration
        return(self.EXEC)
class switchLinc(generic):
    ''' This class is to define and instance
    of an Insteon switchLinc device.
    '''
    def fastOn(self,level=255):
        self.FLAGS = '00'
        self.LEVEL = config.onLevel
        self.EXEC = ic.PRE + self.id + self.FLAGS + ic.ON.cmd1 + self.LEVEL
        return(self.EXEC)
    def fastOff(self):
        self.FLAGS = '00'
        self.LEVEL = '00'
        self.EXEC = ic.PRE + self.id + self.FLAGS + ic.OFF.cmd1 + self.LEVEL
        return(self.EXEC)
    def setLevel(self,level):
        self.FLAGS = '00'
        self.LEVEL = hex(level)
        self.EXEC = ic.PRE + self.id + self.FLAGS + ic.ON.cmd1 + self.LEVEL
        return(self.EXEC)

class applianceLinc(generic):
    ''' This class is to define and
    instance of an appliancelinc controller
    '''
    
class outletLinc(generic):
    ''' This class is to define an instance 
    of an Insteon outletLinc device
    '''
    
class ezFlora(generic):
    ''' This class is to define an instance
    of an ezFlora 8-zone irrigation controller
    '''
    def __init__(self,deviceID):
        self.id = deviceID
    def valveOn(self,valveNumber):
        self.FLAGS = '00'
        self.valveNumber = valveNumber
        # 0x40 = Sprinkler Valve On
        self.EXEC = ic.PRE + self.id + self.FLAGS + '40' + self.valveNumber
        return(self.EXEC)
    def valveOff(self,valveNumber):
        self.FLAGS = '00'
        self.valveNumber = valveNumber
        # 0x41 = Sprinkler Valve On
        self.EXEC = ic.PRE + self.id + self.FLAGS + '41' + self.valveNumber
        return(self.EXEC)
    
class ioLinc():
    ''' This class is to define an instance
    of an IOLinc device
    '''
    def __init__(self,deviceID):
        self.id = deviceID
    def outputOn(self,outputNumber):
        self.FLAGS = '00'
        self.outputNumber = outputNumber
        # 0x40 = Sprinkler Valve On
        self.EXEC = ic.PRE + self.id + self.FLAGS + '45' + self.outputNumber
        return(self.EXEC)
    def outputOff(self,outputNumber):
        self.FLAGS = '00'
        self.outputNumber = outputNumber
        # 0x41 = Sprinkler Valve On
        self.EXEC = ic.PRE + self.id + self.FLAGS + '46' + self.outputNumber
        return(self.EXEC)
    
class thermostat():
    ''' This class is to define an instance of
    an insteon-enabled thermostat.  This was tested
    with a ventstar
    '''


    