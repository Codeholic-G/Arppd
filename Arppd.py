try:
    import os
    import smtplib
    from smtplib import SMTPException
    from getmac import get_mac_address as gma
except ImportError:
    print("Please wait installing requirements")
    os.system("pip install getmac")
    from getmac import get_mac_address as gma

pwd=input("Please Enter Your Gmail Password")
ip_rng=[]
get_mc=[]
g='\033[32m'
r='\033[31m'
b='\033[34m'
w='\033[97m'



def banner():
    print(f'{r}    _    ____  ____  ____  ____')
    print('   / \  |  _ \|  _ \|  _ \|  _ \ ')
    print('  / _ \ | |_) | |_) | |_) | | | | ')
    print(' / ___ \|  _ <|  __/|  __/| |_| |')
    print('/_/   \_\_| \_\_|   |_|   |____/')
    print(f'{b}Address Resolution Protocol Poisoning Detector By DarkkCoder')


def ip_r():
    for i in range(0,256):
        ip_rng.append(ipr + str(i))


def get_madd():
    for i in ip_rng:
        get_mc.append(f"{gma(ip=i)}")


def write_file():
    text=open("config.py","w")
    text.write(f"dm={get_mc}\n")
    text.write(f"ipr='{ipr}'\nmail='{mail}'\n")
    text.write(f"Email_id='{Email_id}'")


def detection():
    if mail=="y":
        for i,j,k in zip(dm,get_mc,ip_rng):
            if i==j  or  j.endswith('00:00:00') or j== 'None':
                pass                               
            elif (get_mc.count(j)) > 1:       
                print(f"{r}Arp poisoning detected at {k}:-{j}{w}")
                send_mail()
                #exit()
            elif j in dm:
                print (f"{b} IP changed for mac {j}")
            else:
                print(f"{g} New mac detected at {k}:- {j}{w}")

    else:
        for i,j,k in zip(dm,get_mc,ip_rng):

            if i==j or j.endswith('00:00:00') or j=='None':
                pass
            elif (get_mc.count(j)) > 1:
                print(f"{r}Arp poisoning detected at {k}:-{j}{w}")
            elif j in dm:
                print (f"{b}IP changed for mac {j}") 
            else:
                print(f"{g} New mac detected at {k}:- {j}{w}")


def send_mail():
        conn=smtplib.SMTP('smtp.gmail.com' ,587)
        conn.ehlo()
        conn.starttls()
        conn.login(Email_id,pwd)
        conn.sendmail(Email_id,Email_id, "Subject: Network Security At Risk \n\n Arp Poisoning Detected ")


try:
    banner()
    while True:
        if os.path.exists("config.py"):
            from config import *
            ip_r()
            get_madd()
            detection()
            get_mc.clear()
            ip_rng.clear()
        else:
            mail=input("Do You want to receive mail when Arp Poisoning detected (y/n ):-")
            ip_range=input("please enter ip range in format 192.168.1.  :- ")
            ipr=(ip_range)
            Email_id=str(input('Enter your gmail id :- '))
            ip_r()
            get_madd()
            write_file()



except KeyboardInterrupt:
    print("\nUser Quitted")
except smtplib.SMTPAuthenticationError:
    print("Please Enter Correct Login Details Or allow access to less secure apps from Gmail to send mail ")






