#coding: utf-8
import requests
from bs4 import BeautifulSoup
import time
import datetime
topthread=''
#state=False
isbreak=True
isfirst=True

username=raw_input('username:')
password=raw_input('password:')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
data={
	'fastloginfield':'username',
	'username':username,
	'cookietime':'259200',
	'password':password,
	'quickforward':'yes',
	'handlekey':'ls',
	'questionid':,   #login question
	'answer':''.decode('utf-8')   #answer
}
se=requests.Session()
r=se.post(url='http://xxx.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&inajax=1',headers=headers,data=data)

re=se.get(url='http://xxx.com/forum.php?mod=forumdisplay&fid=38&filter=author&orderby=dateline',headers=headers)
#print r.content
soup=BeautifulSoup(re.content,'html5lib')
div=soup.findAll('div',attrs={'class':'hasfsl'})
for d in div:
	#print d
	input=d.findAll('input',attrs={'name':'formhash'})
	for i in input:
		formhash=i['value']
		print formhash
while True:
	try:
		isbreak=False
		datetime1=datetime.datetime.now()
		res=se.get(url='http://ahd1080.com/forum.php?mod=forumdisplay&fid=38&filter=author&orderby=dateline',headers=headers)
		datetime2=datetime.datetime.now()
		print str(res.status_code)+'\nrequest time:  '+str(datetime2-datetime1)
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
								mesg='111111111111111111111'
								postdata={
									'message':mesg,
									'formhash':formhash,
									'subject':''
								}
								uri='http://xxx.com/forum.php?mod=post&action=reply&fid=38&tid='+str(number)+'&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'
								r2=se.post(url=uri,headers=headers,data=postdata)
								time.sleep(600000)	
							break
					else:
						isbreak=True
						break
			if isbreak==True:
				break
		res.close()
	except Exception as e:
		print e
		time.sleep(600000)
