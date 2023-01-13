import time
import os
import sys
import pyfiglet
import random

#module animasi mengetik
from os import system
from time import sleep
import sys

def typing(s):
    for c in s + '\n':
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(random.random() * 0.9)
typing('loading...')


def logo():
    print("""\33[0;37m
           _________________________________
          | #***SIMPLE LOOPING PROGRAM***#  |
          | AUTHOR : ./Freebel ft ZopinSec98|
          | VERSION: 1.0.0                  |
          | GITHUB : Mr-Freebel-Id          |
          | TEAM   : SQUAD CYBER KALONG     |
          |_________________________________|
          \33[0;37m""")
logo()
#Menu tools
a = [1 ,2 ,3 ,4 ,5 ,6 ,7]
b = ["Hendrik" , "Zopin", "Create your name", "Help", "Exit Program", "Info Script", "Install Package(recomended)"]


for val1, val2 in zip (a, b):
    print(val1, val2)
#Input tools
inpt = int(input("Choose your character =>: "))

#Percabangan menu_tools nomor 1
if (inpt == 1):
    while True:
        print("Hendrik")
        time.sleep(0.1)
#Percabangan menu_tools nomor 2
if (inpt == 2):
    while True:
        print("Zopin Antares")
        time.sleep(0.1)

#Percabangan menu_tools nomor 3
if (inpt == 3):
    a = input("Enter your name: ")
    print("Your name", a)
    while True:
        print(a)
        time.sleep(0.1)
#Percabangan menu_tools nomor 4
if (inpt == 4):
        print("Pertama , pilih fitur yang anda inginkan(Masukkan nomor). Selebihnya ikuti petunjuk")
#Percabangan menu_tools nomor 5
if (inpt == 5):
    os.system('exit')
#Percabangan menu_tools nomor 6
if (inpt == 6):
    print("ni adalah program pertama saya , mungkin tidak terlalu bagus namun untuk melatih skill coding :v")
#Percabangan menu_tools 7
if (inpt == 7):
    sleep(1)
    system("apt update && apt upgrade")
    system("pkg update && pkg upgrade")
    system("pkg install python")
    system("pkg install python2")
    system("pkg install python3")
    system("pip3 install pyfiglet")
os.system('clear')

