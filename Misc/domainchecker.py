import urllib2 as u
from multiprocessing import Process
import time
def urlchecker(s,k):
	time.sleep(3)
	request=u.Request(s)
	request.get_method= lambda : "HEAD"
	try :
		a=u.urlopen(s)
		print(k+"-NA")
	except u.URLError :
		print(k+"-A")
	except u.HTTPError:
		print(k+"-A")	
l=[]	
k=[".com",".in",".club",".org",".co.in",".club.in",".us",".uk",".co.uk"]
m=raw_input("Enter the domain title : ")
for item in k:
	p=Process(target=urlchecker, args=("http://"+m+item,item))
	l.append(p)
for item in l:
	item.start()
for item  in l:
	item.join()
		
	
