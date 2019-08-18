#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Developed Eric Pedra
#Top Global lose :v
#--- PayPal Checker ---
#Multiprocessing & Threading
#Jangan Terlalu kuat MyThreading , Cukup 10  aja ,jgn 100 ,ntar di blocked sementara webnya :)
#So Very Fast ~ 
from multiprocessing.dummy import Pool 
from threading import Lock, Thread
from fake_useragent import UserAgent 
from colorama import init, Fore
import time, sys, os, requests, datetime, ctypes
init(convert=True)
#Windows Clear
clear = lambda: os.system('cls')
#Input Email .TXT
mailist = open('combo.txt').readlines()
# Threading & multiprocessing
MyThreading = 10 #<- kalau mw input bisa juga pakai int :) jgn kuat" :v ,gk kuat api webnya :v,di blocked jika 100 
kunci = Lock()
myPool = Pool(MyThreading)
#Program Python3
ctypes.windll.kernel32.SetConsoleTitleW("PayPal Validator Developed by Eric Pedra")
class PayPal(Thread):
    startTime = time.time()
    text = '''
╠═════════════════════════════════════════╣
║╔═╗┌─┐┬ ┬╔═╗┌─┐┬    ╔═╗┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐║
║╠═╝├─┤└┬┘╠═╝├─┤│    ║  ├─┤├┤ │  ├┴┐├┤ ├┬┘║
║╩  ┴ ┴ ┴ ╩  ┴ ┴┴─┘  ╚═╝┴ ┴└─┘└─┘┴ ┴└─┘┴└─║
║═════════════════════════════════════════║'''
    live        = 'live'.encode()
    my_fake_s   = UserAgent()
    facebook    = 'Facebook : https://www.facebook.com/Ahmad.AI.Ghazali'
    code        = 'Developed by : Eric Pedra'
    grup        = 'Grup : https://www.facebook.com/groups/ngodingbareng/'
    version     = 'PayPal_Validator'

    def __init__(self):
        clear()
        print(Fore.CYAN + PayPal.text)
        print(Fore.GREEN + PayPal.facebook)
        print(Fore.RED + PayPal.grup)
        print(Fore.YELLOW + PayPal.code)
        self.mydate()
        print('Save -> PayPalValid.txt')
        
        
    def mydate(self): # Fungsi Tanggal & Bulan ,Tahun
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        print("[!] Update "+str(year)+"/"+str(month)+"/"+str(day))
    
    def save(self,emails):
        #penyimpan = str(input("[+] Masuk Pinyampanan File .TXT: "))
        with open('PayPalValid.txt', 'a', encoding='utf8') as f:
            f.write(emails +'\n')

    def checking(self,emails):
        headers = {'User-Agent': self.my_fake_s.chrome}
        urls = 'https://member.wahyusyaadi.web.id/api.php?email='
        web = requests.get(urls+emails, headers=headers)
        if self.live in web.content:
            print (Fore.GREEN ,' ->',self.version,'-',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'- LIVE - '+emails)
            self.save(emails)
        else:
            print(Fore.RED ,' ->',self.version,'-',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'- DEAD - '+emails)

    #Selesai , Perbaiki Sendiri 
    def finish(self):
        endTime = time.time()
        print ('==========')
        print ("Done")
        print ("Total Time    : "), round(endTime - self.startTime, 2), 'Seconds'
        print ("Total Threads : "), (MyThreading)
        print ("Total Mailist   : "), len(mailist)
        print ("=====Finish====")

    def email(self,emails):
        try:
            emails = emails.rstrip()
            checker.PayPal(emails)
        except:
            pass

checker = PayPal()

if __name__ == "__main__":
    myPool.map(checker.checking, mailist)
    myPool.close()
    myPool.join()
    
