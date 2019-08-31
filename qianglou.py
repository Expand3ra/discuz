#coding: utf-8
import requests
import time
import datetime
from bs4 import BeautifulSoup

cookies=''#######need your cookie#########
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
d_cookie={}
topthread=''
#state=False
isbreak=True
isfirst=True
mesg=''
url='http://***/forum.php?mod=forumdisplay&fid=%%&filter=author&orderby=dateline'
uri=''

def getcookie():
	for line in cookies.split(';'):
		if '=' in line:
			name,value=line.strip().split('=',1)  
			d_cookie[name]=value 	

def getformhash():
	r=requests.get(url='http://***/forum.php?mod=forumdisplay&fid=**&filter=author&orderby=dateline',headers=headers,cookies=d_cookie)
	#print r.content
	soup=BeautifulSoup(r.content,'html5lib')
	div=soup.findAll('div',attrs={'class':'hasfsl'})
	for d in div:
		#print d
		input=d.findAll('input',attrs={'name':'formhash'})
		for i in input:
			formhash=i['value']
			#print i['value']
			return formhash
	
def replydata(number,formhash):
	global mesg
	mesg='111111111111111111111'
	postdata={
		'message':mesg,
		'formhash':formhash,
		'subject':''
	}
	uri='http://***/forum.php?mod=post&action=reply&fid=%%&tid='+str(number)+'&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'
	r=requests.post(url=uri,headers=headers,cookies=d_cookie,data=postdata)
	time.sleep(600000)

		
def gettitle():	
	global topthread,isbreak,isfirst
	try:
		formhash=getformhash()
		print formhash
		isbreak=False
		res=requests.get(url=url,headers=headers,cookies=d_cookie)
		res.encoding='utf-8'
		#print res.text
		soup=BeautifulSoup(res.content,'html5lib')
		for line in soup.findAll('table',attrs={'summary':"forum_38"}):
			id=line.findAll('tbody',attrs={'id':True})
			isfirst=True
			#print id[0]
			for l in id:
				#print l['id']
				if l['id'].startswith('normalthread'):
					a=l.findAll('a',attrs={'class':'xst'})
					for a1 in a:
						title=a1.text
						print title
					if isfirst:
						if topthread=='':
							topthread=l['id'].strip()
							isbreak=True
							isfirst=False
							print topthread[13:]+'\n'
							break
						elif l['id']==topthread:
							isbreak=True
							isfirst=False
							print topthread[13:]+'\n'
							break
						elif l['id'].strip()!=topthread:
							print 'get new title!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
							number=l['id'][13:].strip()
							isbreak=True
							topthread=l['id'].strip()
							isfirst=False
							if 'VIP' in title or 'vip' in title:
								print 'reply!!!!!!'
								replydata(number,formhash)
							break
					else:
						isbreak=True
						break
			if isbreak==True:
				break
		res.close()
	except Exception as e:
		print e
	
if __name__ == '__main__':
	getcookie()
	while 1:
		try:
			#print 'refresh!\n'
			gettitle()
			#time.sleep(30)
		except Exception as e:
			print 'sleeping....'
			time.sleep(30)
			print e
		
			
