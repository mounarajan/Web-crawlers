import urllib.request
import os
import re
import time
import json

class Facebook(object):

	def wget(self,url):
		#self.url = url 
		self.data = os.popen('wget -qO- %s'% url).read()
		return self.data

	def curl(self,url):
		
		self.url = url 
		self.data = os.popen('curl --silent %s >/dev/null'% self.url).read()
		return self.data

		#print (self.data)

	def urllib(self,url):
		filename = "cookies.txt"
		self.url = url 
		headers = {}
		headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
		req = urllib.request.Request(url, headers = headers)
		resp = urllib.request.urlopen(req)
		self.data = resp.read()


class out(Facebook):

	def email_add(self,url_direct):

		
		f1 = open('moun_facebook_crawl_urls.txt','a')
		f2 = open('moun_video_crawl_urls.txt','a')
		data = self.data 
		data = str(data)
		
		#f1 = open('staples_category_urls.txt','w')
		#f1.write(data)
		#links = re.findall(r'(?ms)<a href\=['|\"]*([^\"]*\/[about|contact]+.*?)\"',data)
		if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
			email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
			f1.write(email+"\n")
			print (email)
		if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
			email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
			for mail in email:
				if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
					f1.write(mail+"\n")
					print (mail)
		if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
			must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
			for mail in must:
				if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
					f1.write(mail+"\n")
					print (mail)
		if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
			ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
			f1.write(ear+"\n")
			print (ear)

		if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
			ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
			for mail in ear:
				if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
					f1.write(mail+"\n")
					print (mail)
		if re.search(r'(?ms)<a href\=[\'|\"]+([^\"|\']*\/about.*?|contact.*?)[\'|\"]+',data):
			links = re.findall(r'(?ms)<a href\=[\'|\"]+([^\"|\']*\/about.*?|contact.*?)[\'\"]+',data)
			for url in links:
				#pass
				#url = re.sub(r"^","http://staples.com",url)
				if re.search(r'^http\:\/\/',url):
					f2.write(url+"\n")
					print (url)
				else:
					url = re.sub(r'^','%s'% url_direct,url)
					f2.write(url+"\n")
					print (url)

	def email_from_links(self):

		
		f1 = open('moun_facebook_crawl_urls.txt','a')
		#f2 = open('moun_video_crawl_urls.txt','a')
		data = self.data 
		data = str(data)
		
		#f1 = open('staples_category_urls.txt','w')
		#f1.write(data)
		#links = re.findall(r'(?ms)<a href\=['|\"]*([^\"]*\/[about|contact]+.*?)\"',data)
		if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
			email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
			f1.write(email+"\n")
			print (email)
		if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
			email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
			for mail in email:
				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail):
					f1.write(mail+"\n")
					print (mail)
		if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
			must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
			for mail in must:
				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail):
					f1.write(mail+"\n")
					print (mail)
		if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
			ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[^\.]*[\.]*\w+(?:[\w\.\+]*))',data)[0]
			f1.write(ear+"\n")
			print (ear)

		if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
			ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[^\.]*[\.]*\w+(?:[\w\.\+]*))',data)
			for mail in ear:
				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail):
					f1.write(mail+"\n")
					print (mail)

		#print (email)
		#print (links)
		#print (must)
		#print (ear)
		#f2.write(links)
		
		


f1 = open('links.txt','r')
#f2 = open('links.txt','r')
for li in f1:
	show = out()
	if re.search(r'^htt',li):
		lin = re.sub(r"\s*","",li)
	#li = "%s"%li
		print(lin)
		show.wget(lin)
		show.email_add(lin)
		time.sleep(3)

with open('moun_video_crawl_urls.txt') as result:
        uniqlines = set(result.readlines())
        with open('moun_video_crawl_urls1.txt', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))

f2 = open('moun_video_crawl_urls1.txt','r')
for li in f2:
	show = out()
	if re.search(r'^htt',li):
		lin = re.sub(r"\s*","",li)
	#li = "%s"%li
		print(lin)
		show.wget(lin)
		show.email_from_links()
		time.sleep(3)

#show.email_add()
with open('moun_facebook_crawl_urls.txt') as result:
        uniqlines = set(result.readlines())
        with open('moun_facebook_crawl_urls1.txt', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))