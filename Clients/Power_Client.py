# -*- coding: utf-8 -*-
from pysnmp.entity.rfc3413.oneliner import cmdgen
from Client_util import *

def RaritanRead(oid):
    address = '1.3.6.1.4.1.13742.6.5.2.3.1.4.1.1.'+str(oid)
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData('private'),
        cmdgen.UdpTransportTarget(('192.168.0.250', 161)),
        address
    )

    if errorIndication:
        print (errorIndication)
    else: 
        if errorStatus:
            print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?')
            )
        else:
            for name, val in varBinds:
                pass
            #     print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
            return val
    
if __name__ == "__main__":
    while True:
    	post_request('Status_Power', {"current":       str(RaritanRead('1')),
                                      "voltage":       str(RaritanRead('4')),
                                      "activepower":   str(RaritanRead('5')),
                                      "apparentpower": str(RaritanRead('6')),
                                      "powerfactor":   str(RaritanRead('7'))})
        time.sleep(5)