import time
import base64
import requests

def getRouterUri():
    return "http://192.168.0.1"

def getPasswordBase64():
    data = base64.b64encode(b'your_router_password')
    data = data.decode('utf-8')
    return data

def reboot():
    #send post request TP-Link back end logic
    print("Sending Reboot Request")

    req = requests.Request('POST', getRouterUri() +'/cgi?7', headers={'Host': getRouterUri(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0', 'Accept': '*/*', 'Origin': getRouterUri(), 'Referer': getRouterUri()}, data='[ACT_REBOOT#0,0,0,0,0,0#0,0,0,0,0,0]0,0\r\n', cookies={'Authorization' : 'Basic '+getPasswordBase64()+''})
    prepared = req.prepare()

    s = requests.Session()
    resp = s.send(prepared)

    if resp.status_code != 200 :
        print("Bad response code : " + str(resp.status_code))
    else :
        print("Waiting for Reboot")
        time.sleep(70)

    print("Router has rebooted\n")

def main():
    hasQuit = False

    while not hasQuit:
        print("Please choose an option")
        print("Press R to Reboot")
        print("Press Q to Quit")

        choice = input().lower();

        if choice == "r":
            reboot()

        if choice == "q":
            hasQuit = True;


main()


