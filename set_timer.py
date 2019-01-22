import binascii
import time

from timeout_decorator import timeout

import daemon
from bluepy.btle import Peripheral

''' Please edit here↓ '''
# address: Mac address (String), interval: execution interval [min] (int)
# You can set multiple timers
switch_list = [{'address': 'AA:BB:11:22:C3:D4', 'interval': 60},
               {'address': 'XX:YY:99:88:ZZ:77', 'interval': 30}]
''' Please edit here↑ '''


@timeout(10)
def push(address):
    p = Peripheral(address, 'random')
    hand_service = p.getServiceByUUID('cba20d00-224d-11e6-9fb8-0002a5d5c51b')
    hand = hand_service.getCharacteristics(
        'cba20002-224d-11e6-9fb8-0002a5d5c51b')[0]
    hand.write(binascii.a2b_hex('570100'))
    p.disconnect()


def main():
    # First push all
    for switch in switch_list:
        try:
            push(switch['address'])
        except:
            pass
        switch['last_time'] = time.time()
    # From the second time onwards push at any time
    while True:
        for switch in switch_list:
            if time.time() - switch['last_time'] > switch['interval'] * 60:
                try:
                    push(switch['address'])
                except:
                    pass
                switch['last_time'] = time.time()


if __name__ == '__main__':
    with daemon.DaemonContext():
        main()
