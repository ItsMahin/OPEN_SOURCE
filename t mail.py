# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-12-18 14:54:53.089631

import os
import sys
import time
import requests
import json


def psb(z):
    for l in z + "\n":
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.03)

def logopsb(z):
    for l in z + "\n":
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.001)
        


def logo():
	os.system('clear')
	print (""" 
\t\033[1;32m██    ██   ██   ██    ██   ██
\t\033[1;32m██    ██   ██   ██     ██ ██
\t\033[1;32m████████   ███████      ███
\t\033[1;32m██    ██        ██     ██ ██
\t\033[1;32m██    ██        ██    ██   ██

\033[1;32m══════════════════════════════════════════════════════
\033[1;32m[💜]     \033[1;32mCREATED BY\33    :  \033[1;33mMEHEDI\33[0;m\033[1;32m
\033[1;32m[💜]     \033[1;32mFACEBOK      : \033[1;34m MD MEHU
\033[1;32m[💜]     \033[1;32mGITHUB       :  \033[1;35mH4X-GG
\033[1;32m[💜]     \033[1;32mTOOL VIRSION :  \033[1;36m1.0.0
\033[1;32m[💜]    \033[1;32m TOOL TYPE    : \033[1;32m FREE
\033[1;92m══════════════════════════════════════════════════════
	
	""")

def logout():
    psb("\n\033[92m \t[*] Thanks For Using Our Tool..")
    psb("    \n[*] For More Tools, Visit : \n")
    psb("     \n [[>]] https://github.com/H4X-GG\n")
    sys.exit()

def random_mail():
    json_data = {
    "min_name_length" : 10,
    "max_name_length" : 10
    }
    url =  "https://api.internal.temp-mail.io/api/v3/email/new"
    re = requests.post(url, json = json_data)
    data = json.loads(re.text)["email"]
    return data


def domain_choose():
    print("\033[92m\n    [01] cloud-mail.top")
    print("    [02] buy-blog.com")
    print("    [03] the23app.com")
    print("    [04] mac-24.com")
    print("    [05] thejoker5.com")
    print("    [06] greencafe24.com")
    print("    [07] crepeau12.com")
    print("    [08] appzily.com")
    print("    [09] coffeetimer24.com")
    print("    [10] popcornfarm7.com")
    print("    [11] bestparadize.com")
    print("    [12] kjkszpjcompany.com")
    print("    [13] cashflow35.com")
    print("    [14] crossmailjet.com")
    print("    [15] kobrandly.com")
    print("    [16] blondemorkin.com")
    dom = input("\033[92m\n    [*] Enter Your Domain Choice:> \033[37m")
    if not (dom == "10"):
        dom = dom.replace("0", "")
    while not dom in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]:
        print("\n\033[91m    [!] Enter a Correct Choice!!\033[37m")
        dom = input("\033[92m\n    [*] Enter Your Domain Choice:> \033[37m")
        if not (dom == "10"):
            dom = dom.replace("0", "")
    if (dom == "1"):
        doms = "cloud-mail.top"
    elif (dom == "2"):
        doms = "buy-blog.com"
    elif (dom == "3"):
        doms = "the23app.com"
    elif (dom == "4"):
        doms = "mac-24.com"
    elif (dom == "5"):
        doms = "thejoker5.com"
    elif (dom == "6"):
        doms = "greencafe24.com"
    elif (dom == "7"):
        doms = "crepeau12.com"
    elif (dom == "8"):
        doms = "appzily.com"
    elif (dom == "9"):
        doms = "coffeetimer24.com"
    elif (dom == "10"):
        doms = "popcornfarm7.com"
    elif (dom == "11"):
        doms = "bestparadize.com"
    elif (dom == "12"):
        doms = "kjkszpjcompany.com"
    elif (dom == "13"):
        doms = "cashflow35.com"
    elif (dom == "14"):
        doms = "crossmailjet.com"
    elif (dom == "15"):
        doms = "kobrandly.com"
    elif (dom == "16"):
        doms = "blondemorkin.com"
        
    return doms

def create_mail():
    url = "https://api.internal.temp-mail.io/api/v3/email/new"
    name = input("\033[92m\n    [*] Enter Email Name:> \033[37m")
    domain = domain_choose()
    data = name+"@"+domain
    cost_data = {
        "name" : name,
        "domain" : domain
    }
    j = requests.post(url, json = cost_data)
    return data


def print_mail(data):
    data = json.loads(data)
    if not os.path.exists(".tmp"):
        os.system("touch .tmp")
    em_cont = 1
    for em_data in data:
        data_id = str(em_data["id"])
        opn = open(".tmp", "r").read()
        if data_id in opn:
            continue
        wrt = open(".tmp", "w")
        wrt.write(opn+"\n"+data_id)
        wrt.close()
        frm = em_data["from"]
        cc = em_data["cc"]
        if (cc == None):
            cc = "None"
        to = em_data["to"]
        sub = em_data["subject"]
        mail_data = em_data["body_text"]
        attch = em_data["attachments"]
        psb("\033[92m\n\n            [*] Inbox Wait for your massage : \033[37m0"+str(em_cont))
        
        print("\033[92m\n[*] From    : \033[37m"+frm)
        print("\033[92m\n[*] To      : \033[37m"+to)
        print("\033[92m\n[*] CC      : \033[37m"+cc)
        print("\033[92m\n[*] Subject : \033[37m"+sub)
        print("\n\033[92m[*] Mail    :\033[37m\n\n"+mail_data)
        if not (attch == "[]"):
            atc_num = 1
            for atc in attch:
                id = atc["id"]
                down = "https://api.internal.temp-mail.io/api/v3/attachment/"+id+"?download=1"
                print("\033[92m\n[*] Attachment No : \033[37m0"+str(atc_num))
                print("\033[92m\n[*] File Name : \033[37m"+atc["name"])
                print("\033[92m\n[*] File Size : \033[37m"+str(atc["size"])+"\033[92m  [ Bytes ]")
                print("\033[92m\n[*] Download From Here : \033[37m"+down)
                atc_num = atc_num + 1
        em_cont = em_cont + 1


    
def invox(mdata):
    psb("\033[92m\n    [*] Press ctrl Then c To Go Back To Main Menu...")
    psb("\t\033[92m\033[33m[\033[34m*\033[33m] \033[92mInbox wait for your massage\033[33m[\033[34m*\033[33m] \033[37m")
    url = "https://api.internal.temp-mail.io/api/v3/email/"+mdata+"/messages"
    while True:
        try:
            re = requests.get(url).text
            if not re == "[]\n":
                print_mail(re)
            time.sleep(0.5)
        except KeyboardInterrupt:
            break


def see_mail():
    logo()
    if os.path.exists(".mail"):
        old_mails = open(".mail", "r").readlines()
        mn = 1
        psb("\033[92m    [*] Your Created Emails : \n")
        for mail in old_mails:
            psb("\033[92m    [0"+str(mn)+"] \033[37m"+mail)
            mn = mn + 1
    else:
        time.sleep(0.8)
        psb("\033[92m    [!]  Currently You Have No Old Mail Address")


def log_old():
    logo()
    try:
        old_mails = open(".mail", "r").readlines()
    except:
        psb("\033[92m   [!]  Currently You Have No Old Mail Address [!]")
        return None
    if not (old_mails == "[]"):
        psb("\033[92m   [*] Copy The Mail You Want To Restore and Past Below...\n")
        for mail in old_mails:
            if (mail == ""):
                continue
            psb("\033[92m    [#] \033[37m"+mail)
        mold = input("\033[92m    [*] Past Your Mail:> \033[37m")
        while not mold+"\n" in old_mails and not mold in old_mails and not mold == "":
            psb("\033[91m    [!] Only Past Emails From Above...\033[37m")
            mold = input("\033[92m    [*] Past your Mail:> \033[37m")
        if (mold == ""):
            mold = None
        return mold
    else:
        psb("\033[92m    [!]  Currently You Have No Old Mail Address [!]")
        return None
os.system('clear')


def remove():
    logo()
    psb("\033[92m   [*] Removing All Old Mail's Data...")
    psb("  [*] Please Wait....")
    time.sleep(0.8)
    try:
        os.system("rm .mail")
    except:
        pass
    try:
        os.system("rm .tmp")
    except:
        pass
    psb("    [*] Successfully Removed All Old Mails Data...")

os.system('clear')
def main():
    psb("\n\033[95m    [••] Choose Your Method...")
   
    print(" \n    [01] Genarate Random Mail")
    print("    [02] Castom mail Address")
    print("    [03] See Mails You Created")
    print("    [04] Log In To Old Mails")
    print("    [05] Remove All Old Mail's Data")
    print("    [00] Exit")
    
    op = input("\n\033[92m   [*] Choose Your Option:> \033[37m").replace("0", "").replace("##", "#")
    while not op in ["1", "2", "3", "4", "5", "0"]:
        print("\033[91m    [!] Choose a Correct Option!!\033[37m")
        op = input("\033[92m   [*] Choose Your Option:> \033[37m").replace("0", "").replace("##", "#")
    if (op == "1"):
        mdata = random_mail()
        do_mail(mdata)
        o = input("\033[92m    [*] Press Enter To Go Back....")
    elif (op == "2"):
        mdata = create_mail()
        do_mail(mdata)
        o = input("\033[92m    [*] Press Enter To Go Back....")
    elif (op == "3"):
        see_mail()
        o = input("\033[92m    [*] Press Enter To Go Back....")
    elif (op == "4"):
        mdata = log_old()
        if not (mdata == None):
            do_mail(mdata)
        o = input("\033[92m    [*] Press Enter To Go Back....")
    elif (op == "5"):
        remove()
        o = input("\033[92m    [*] Press Enter To Go Back....")
    elif (op == "0"):
        logout()
    
    
def do_mail(mdata):
    if not os.path.exists(".mail"):
        os.system("touch .mail")
    fmopn = open(".mail", "r").read()
    fmout = open(".mail", "w")
    if not (fmopn == "") and not (mdata in fmopn):
        fmout.write(fmopn+"\n"+mdata)
    elif (fmopn == ""):
        fmout.write(mdata)
    else:
        fmout.write(fmopn)
    fmout.close()
    logo()
    psb("\033[92m[*] Your Created Mail : \033[37m"+mdata)
    invox(mdata)
    

if __name__ == "__main__":
    logo()
    while True:
        main()


