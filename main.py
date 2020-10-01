from mac import MAC_changer 

if __name__=="__main__":
    mc=MAC_changer()
    print("The default interface is eth0.")
    curr_mac=mc.change_mac("eth0")
    print(curr_mac)

