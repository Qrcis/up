import time

import os

import os.path

from os import path

try:

    import string

except:

    os.system("pip install strings")

from random import choice

from time import sleep

import datetime

try:

    import tqdm

    from requests import get

    from requests import post

    

except:

    os.system("pip install requests")

    os.system("pip install tqdm")

import random as rn

from random import randint

try:

    from threading import Thread

except:

    os.system("pip install threaded")

from json import loads, dumps

import base64

import sys

import time

try:

    import multiprocessing.pool

except:

    os.system("pip install multiprocess")

try:

    import functools

except:

    os.system("pip install functools")    

try:

    from Crypto.Cipher import AES

    from Crypto.Util.Padding import pad, unpad

except:

    os.system("pip install pycryptodome")

    

import time

from re import findall

    

try:

    from termcolor import colored

except:

    os.system("pip install termcolor")

from requests import post, get

import glob

from sys import exit

import pathlib

import sys

import subprocess

import platform

import concurrent.futures

from tqdm import tqdm

import random

import datetime

import re

from re import findall

from pathlib import Path

from random import randint, choice

from json import loads, dumps, JSONDecodeError

try:

    import pyfiglet

    import rainbowtext

except:

    os.system("pip install pyfiglet")

    os.system("pip install rainbowtext")

class encryption:

    def __init__(self, auth):

        self.key = bytearray(self.secret(auth), "UTF-8")

        self.iv = bytearray.fromhex('00000000000000000000000000000000')

    def replaceCharAt(self, e, t, i):

        return e[0:t] + i + e[t + len(i):]

    def secret(self, e):

        t = e[0:8]

        i = e[8:16]

        n = e[16:24] + t + e[24:32] + i

        s = 0

        while s < len(n):

            e = n[s]

            if e >= '0' and e <= '9':

                t = chr((ord(e[0]) - ord('0') + 5) % 10 + ord('0'))

                n = self.replaceCharAt(n, s, t)

            else:

                t = chr((ord(e[0]) - ord('a') + 9) % 26 + ord('a'))

                n = self.replaceCharAt(n, s, t)

            s += 1

        return n

    def encrypt(self, text):

        raw = pad(text.encode('UTF-8'), AES.block_size)

        aes = AES.new(self.key, AES.MODE_CBC, self.iv)

        enc = aes.encrypt(raw)

        result = base64.b64encode(enc).decode('UTF-8')

        return result

    def decrypt(self, text):

        aes = AES.new(self.key, AES.MODE_CBC, self.iv)

        dec = aes.decrypt(base64.urlsafe_b64decode(text.encode('UTF-8')))

        result = unpad(dec, AES.block_size).decode('UTF-8')

        return result

class accesses:

    class admin:

        pin = "PinMessages"

        newAdmin = "SetAdmin"

        editInfo = "ChangeInfo"

        banMember = "BanMember"

        changeLink = "SetJoinLink"

        editMembersAccess = "SetMemberAccess"

        deleteMessages = "DeleteGlobalAllMessages"

    class user:

        viewMembers = "ViewMembers"

        viewAdmins = "ViewAdmins"

        sendMessage = "SendMessages"

        addMember = "AddMember"

class clients:

    web = {

        "app_name": "Main",

        "app_version": "4.1.11",

        "platform": "Web",

        "package": "web.rubika.ir",

        "lang_code": "fa"

    }

    android = {

        "app_name": "Main",

        "app_version": "2.9.5",

        "platform": "Android",

        "package": "ir.resaneh1.iptv",

        "lang_code": "fa"

    }

defaultDevice = {"token_type":"Web","token":"","app_version":"WB_4.1.11","lang_code":"fa","system_version":"Mr Null","device_model":"Mr Null","device_hash":"25910024641080241001011080"}

class Bot:

    def __init__(self, auth):

        self.auth = auth

        self.enc = encryption(auth)

    def _getURL():

        servers = ["https://messengerg2c1.iranlms.ir/"]

        lserver = random.choice(servers)

        return lserver

    def getFolders(self):

        server = Bot._getURL()

        return loads(

            self.enc.decrypt(post(json={

                "api_version": "5",

                "auth": self.auth,

                "data_enc": self.enc.encrypt(dumps({

                    "method": "getFolders",

                    "input": {},

                    "client": {"app_name": "Main", "app_version": "4.2.0", "platform": "Web", "package": "web.rubika.ir", "lang_code": "fa"},

                }))}, url=server).json()["data_enc"]))

    

def print_slow(txt):

    for x in txt:

        print(x, end='', flush=True)

        time.sleep(0.1)

        

def clear():

    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)

    

    

auths = set([
  "qkdbnzmqcpfnpkzfhkvjpemgaetnybld","ecocyptcjulqmalwvfrqtppdhtskcevg","dpxctxmytqyjhvxeondwmcjizatvurye","mctqzoxpgncidczpdxuapcrzawnrporj","gyxikibzsrltvlwcjkjoabryxarexnar","amqdhjpxeeowptrufrhhhcdnnzlitlej","kkpebwvtfsrbtcdakeriqyxsqmclrakd","anchalriijxuyphkfvhbwdxhumtwtuuq","fcyggejiwpvnepvflybsrwfffboeqxhl","dgqfkhkwfosielacdibbtgieejhqeszi","wjnsvrnlsbbxdrqccxskstbcsdxetqrn","xwcgwdtiimrarrckcvxcdlrxgxdxvdka","sgoxstamtibacdmesexrfddvqrbkmcqq","zzjnafzculnmlwzsbffapwissxlgjsio","bmbdeljhqfmsbhobampfyiizlbojtngv","wzcuuqtpucodgfgkbpmnzfmtqilfrvvu","mfriwqcniyioyjgzkylgbvyjhxtsxsgi","wwodgczkudxnsxfdsgpkjyiygbhmqjnv","lmxzhtshbweysjrzmtznkdvbfvnqrcuk","uyugvrkhnyesulymhqtaiagqqvjlwtde","lmjrgwlbbwkzdrxchnquvuwfkcviepjj","lnxmrstqoawxqlcrnnsgtjwgvgrjrplh","vjdidcglxgwzzefxyjwifnxrcagtiupy","lllvbpelxgnxvqehwfeuszlqwewxylri","jgjcbhsydnjsxgnfurervkcjanlnuntq","zgvebwcautvvduymyzcilbygvhcfmphs","gdcyzrlyojuhpivygnpzoqunamjymuii","ciiyznyrtawlfaehytbnmmcyhzhyvtho","ogbfebdakelgoemjwoevkdgqrbtfryjd","gvycadrefhuanpfmqgqtuzsooikaypwf","oxtosenswpnvqytdidzuundygokfbxbq","rguywayjozxlqzecppdwkhmjrbjigqny","tfvyzjzazxlytxmcusbloukppnnkqndx","cserumequcndcikdjpcrietpxrfjtghy","ndcobqtkdrfsavedvmgnhdbynfwfkaqr","kkwsqesbiwxieyocswxohyhrlwrpwnwt","lnaxvibxqsufbueidjifaazwzaiaixar","nyjwoujbjtixhjdtmrvjctgfaogdnpwb","ylestxgtwrqvlrrzffmkkkflgoyzpjnl","zwilbxafzlyuqoczautjbxrcjxgtmrgn","jpixcjwddudguzmqyppnmcaesefgpjmo","vfkmdlzkaolwpzubovptyxjdzhesmnhp","cntcwpaoqdbmxpyzrljzbsrxrjypmfnp","rrqagsiihcvsjcetzppkmfebsncbgyjx","vclnrdsuylvagwyuyeevqvovdhcofavf","jhurwowjkbukbvyyimphtcumeawlrmcx","yhzqemykundetzguvgrgtvslkxehexfa","ocekgjxzrmobaxbjwoxnlefyqwzxzzry","jioavylugyjprgidsttuefpajmurljfe","gdhavuxoavckmlgcrfyvjvaacqhqnimq","peaxtrojklmtusqjykmqxkqrmqtuxthh","kufudyjizqbvotkeylznqesfnnkjubgk","rmugfsljxmzqnprgvusmosdprcwokmkp","azxxkdsizhwirzagwshkmhupojakczml","rfzwvjztjnuuequczapflfrfjjcaoerl","rvgblqtnwtyiulrevtubsttroshssnpx","tlioolnhieysqxljcmcsmwqajujqgwsy","dfekxxtiznmergcqmjvmizlmfvpntwam","vwhldlxeipumcxsadzggnwcczsanqqrq","nsctilqpddjrbdrsbjakqlpcqqyzoqca","xuhgzgguifmicpbuoxrjctprebdutjsk","gziaptprpwhrwjzzokycxastnbuawyfk","dajlkyxjeiynxthzhvghiosiawuxzlzl","uevxqjnzmhtusqxkkidxxirgndhfftpn","dufpjkdtlljgugzbftoscjhjlwbqdtjz","gzkiczojdgrjxjetkuaeuvzblpubenmk","xgycswafzavvvfyerqvfclkwekiikkjd","dslcoejmkqabycevrlhyuezkrploaxut","tfnfayputkrkwvfjlbaudjwjkoqeuerf","mxhwwsjhqlludrreylsmauflqtwglqtf","ayrezcjmiileewudsyktqwbupwxazabw","fiexzeoisfjwzquhwiqoctbirecrucwp","lrkxqzohgpqzodcogpjeqrgztwpiukzl"

])#در این قسمت شناسه هاتونو به ترتیب وارد می کنید

#slant , 3-d, 3x5, 5lineoblique, alphabet, banner3-D, doh, letters, aligator, dotmatrix, bubble, buldhead, digital 

text = pyfiglet.figlet_format(text=f"Mr Null")



print(text) ## این قسمت متن رو بزرگ و رنگی می کنه !

print("- - - - - - - - - - - - KOS BOT - - - - - - - - - - - - ")

print_slow(f"""

{colored("Channel Rubika ","yellow")} : {colored("@test","green")}

{colored("Creator","yellow")} : {colored("@test","green")}

""")

tedad = 0

count_start = len(auths)

try:

    print_slow(f"""

\n

{colored("Count Auth for test | تعداد شناسه ها برای تست","red")}:{colored(f"{count_start}","green")}\n

    """)

    for auth in auths:

        try:

            bot = Bot(auth)

            status = bot.getFolders()["status"] # این قسمت چک می کنه auth سالمه یا ن

            if status == "OK":

                tedad += 1

                print(f"""

{colored("AUth IS OK ","green")}:{colored(f"{tedad}","red")}\n

                """)

                o = open("Auths.txt" , 'w+') # اینجا هم شناسه هایی که سالمن رو ذخیره می کنه

                o.write(f"\n{auth}")

                o.close()

        except:

            continue

    print(f"""

{colored("Count Auth | تعداد شناسه های پیدا شده","green")}:{colored(f"{tedad}","red")}

    """)

except:pass

