import subprocess
import re
import random
import time

class MAC_changer:
    def __init__(self):
        self.MAC=""
    def get_MAC(self,iface):
        output = subprocess.run(["ifconfig",iface],shell=False,capture_output=True)
        cmd_result=output.stdout.decode('utf-8')
        

        pattern=r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'

        regex=re.compile(pattern)

        ans = regex.search(cmd_result)
        current_mac=ans.group().split(" ")[1]
        self.MAC=current_mac
        return current_mac

    

    def change_mac(self,iface):
        def new_mac():
            return "02:%02x:%02x:%02x:%02x:%02x" % (random.randint(0,255),
                                               random.randint(0,255),
                                               random.randint(0,255),
                                               random.randint(0,255),
                                               random.randint(0,255))
        print("[+] Current MAC Address is ", self.get_MAC(iface))

        
        output= subprocess.run(["ifconfig", iface, "down"], shell=False, capture_output=True)
        print(output.stderr.decode('utf-8'))

        upd=new_mac()
        output= subprocess.run(["ifconfig", iface, "hw","ether",upd], shell=False, capture_output=True)
        print(output.stderr.decode('utf-8'))

        output=subprocess.run(["ifconfig",iface,"up"], shell=False,capture_output=True)
        print(output.stderr.decode('utf-8'))

        print("[+] Updated MAC Address is ", self.get_MAC(iface))

        return self.get_MAC(iface)


        