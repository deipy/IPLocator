#Script by Deipy (https://www.github.com/deipy/) please let me know if you distribute this script

####################################################################################################

#if you got error code 401, please use your own key, available for free at https://www.ipdata.co/.
#use it once the program asks, or modify the default key below.

key = "e10135594cceca891c0cb18a71140983e4da907a6d9339dd67b8b380"

####################################################################################################

import requests
from colorama import Fore

def banner():
    #everyone likes banners right ?
    print(Fore.BLUE+"._____________"+Fore.YELLOW+".____                         __                 ")
    print(Fore.BLUE+"|   \______   \\"+Fore.YELLOW+"    |    ____   ____ _____ _/  |_  ___________ ")
    print(Fore.BLUE+"|   ||     ___/"+Fore.YELLOW+"    |   /  _ \_/ ___\\__  \\   __\/  _ \_  __ \ ")
    print(Fore.BLUE+"|   ||    |   "+Fore.YELLOW+"|    |__(  <_> )  \___ / __ \|  | (  <_> )  | \/ ")
    print(Fore.BLUE+"|___||____|   "+Fore.YELLOW+"|_______ \____/ \___  >____  /__|  \____/|__|    ")
    print(Fore.YELLOW+"                         \/          \/     \/                              ")
    print(Fore.BLUE+"                                                       By "+Fore.YELLOW+"Deipy")
    print("")

def askForKey(key):
    print(Fore.BLUE+"[?]"+Fore.YELLOW+" This program uses the ipdata.co API, the default key might not work.")
    print(Fore.BLUE + "[?]" + Fore.YELLOW + " Do you wish to use the default key (Y/n) :")
    CKey = str(input())
    if (CKey == "n") or (CKey=="N") :
        print(Fore.BLUE + "[?]" + Fore.YELLOW + " API Key :")
        customKey = str(input())
        return customKey
    else :
        print(Fore.BLUE + "[!]" + Fore.YELLOW + " Alright, using default key.")
        return key

def printOpt():
    #print the options menu
    print(Fore.BLUE+"[1]"+Fore.YELLOW+" GeoInfos   "+Fore.BLUE+"[2]"+Fore.YELLOW+" Organization")
    print(Fore.BLUE+"[3]"+Fore.YELLOW+" Timezones  "+Fore.BLUE+"[4]"+Fore.YELLOW+" Currency")
    print(Fore.BLUE+"[5]"+Fore.YELLOW+" Threat     "+Fore.BLUE+"[6]"+Fore.YELLOW+" All")
    print("")
    print(Fore.BLUE+"[?]"+Fore.YELLOW+" Select an option :")

#print banner, ask for API key,gather info and make a request
banner()
key = askForKey(key)

print("")
print(Fore.BLUE+"[?]"+Fore.YELLOW+" Enter IPv4 address :")
address = input()

print("")
print(Fore.BLUE+"[!]"+Fore.YELLOW+" Reaching server...")
print("")

#Make the request to the API
req = requests.get("https://api.ipdata.co/"+address+"?api-key="+key)

#if the server replied OK, ask and print options, if not, print the error code
if req.status_code == 200:
    infos = str(req.json()).replace('"', "").replace("'","").replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("_", " ").split(",")
    printOpt()
    opt = int(input())

    if opt == 1:
        #print geo infos
        print("Country : " + str(req.json()['country_name']))
        print("Region : " + str(req.json()['region']))
        print("City : " + str(req.json()['city']))
        print("Latitude : " + str(req.json()['latitude']))
        print("Longitude : " + str(req.json()['longitude']))

    elif opt == 2 :
        #print organization infos
        if("asn" in req.json() != None):
            print("ASN : " +str(req.json()['asn']['asn']))
            print("Name : " + str(req.json()['asn']['name']))
            print("Domain : " + str(req.json()['asn']['domain']))
            print("Route : " + str(req.json()['asn']['route']))
            print("Type : " + str(req.json()['asn']['type']))
        else :
            print("No data")

    elif opt == 3 :
        print("Time zone : "+ str(req.json()['time_zone']['name']))
        print("Abbreviation :"+str(req.json()['time_zone']['abbr']))
        print("Current time :"+str(req.json()['time_zone']['current_time']))

    elif opt == 4 :
        #print currency options
        print("Currency : "+str(req.json()['currency']['name']))
        print("Code : " + str(req.json()['currency']['code']))
        print("Symbol : " + str(req.json()['currency']['symbol']))

    elif opt == 5:
        #print threat options
        if "threat" in req.json() != None :
            print("Is tor : " + str(req.json()['threat']['is_tor']))
            print("Is anonymous : " + str(req.json()['threat']['is_anonymous']))
            print("Is known attacker  : " + str(req.json()['threat']['is_known_attacker']))
            print("Is known abuser : " + str(req.json()['threat']['is_known_abuser']))
            print("Is threat : "+str(req.json()['threat']['is_threat']))
            print("Is bogon : "+str(req.json()['threat']['is_bogon']))
        else :
            print("No data")

    elif opt == 6:
        #print everything
        for num, info in enumerate(infos):
            print(str(num) + " : " + info)

elif req.status_code == 400 :
    print(Fore.BLUE+"[!]"+Fore.YELLOW+" Could not gather data : Error code 400 :")
    print("    invalid syntax, probably invalid address.")

elif req.status_code == 401 :
    print(Fore.BLUE+"[!]"+Fore.YELLOW+" Could not gather data : Error code 401 : invalid auth token, key is probably ")
    print("    expired. You can get a new one for free at ipdata.co and paste it once or modify")
    print("    this program.")

elif req.status_code == 403:
    print(Fore.BLUE + "[!]" + Fore.YELLOW + " Could not gather data : Error code 403 : Forbidden operation :")
    print("    either the key used is invalid, or the address was invalid, or both.")

else :
    print(Fore.BLUE+"[!]"+Fore.YELLOW+" Could not gather data : Error code :" + str(req.status_code))
