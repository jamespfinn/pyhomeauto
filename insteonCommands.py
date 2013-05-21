''' This file contains "constants" for various Insteon commands
    command reference: http://www.madreporite.com/insteon/commands.htm
'''
class insteonCommand:
    ''' insetonCommand class is initialized
    with the following parameters:
        cmd1: hex string, part 1 of the command
        cmd2: value or array of possible values, part 2 of the command
        name: string, command name
        notes:string, notes about the command
        etc:  string, additional info about the command 
        cmdtype: string, addit'l info about the command, e.g. std, extended (optional, future use)
        
    '''
    def __init__(self, cmd1, cmd2, name, notes, etc, cmdtype="tbd"):
        self.cmd1 = cmd1
        self.cmd2 = cmd2
        self.name = name
        self.notes = notes
        self.etc = etc
        self.cmdtype = cmdtype
        
# Standard preamble for all insteon commands:
PRE     = '0262'        
# BASIC COMMANDS        
ON      = insteonCommand("11","00-FF","ON","Go ON to the specified level (cmd2). In a broadcast group command, the cmd2 is ignored as it relies upon its internal at-link-time setting.","DevCat 0x01, 0x02","Standard Direct Command")
FASTON  = insteonCommand("12","00-FF","ON","Go FAST ON to the specified level (cmd2). In a broadcast group command, the cmd2 is ignored as it relies upon its internal at-link-time setting.","DevCat 0x01, 0x02","Standard Direct Command")
OFF     = insteonCommand("13","00","OFF","Go OFF.","DevCat 0x01, 0x02","Standard Direct Command")
BEEP    = insteonCommand("30","DURATION","BEEP","BEEP DEVICE","")
#DIMMER COMMANDS
BRIGHT  = insteonCommand("15","00","BRIGHT","Brighten the dimmer +1","")
DIM     = insteonCommand("16","00","BRIGHT","Dim the dimmer -1","")

THERMOSTAT = insteonCommand("6B","STORED IN CLASS","Thermostat Control","Various EZTherm-specific commands","")
