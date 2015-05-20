#from urllib.request import Request, urlopen
import urllib.request
import os
import re
import time
import json

class AccessData(object):
	while True:
		try:

			def urllib(self,url):
				filename = "cookies.txt"
				self.url = url 
				headers = {}
				headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
				req = urllib.request.Request(url, headers = headers)
				resp = urllib.request.urlopen(req)
				self.get_data_out = resp.read()


		#self.get_data_out = Request(self.url,headers)
		#self.get_data_out = urlopen(self.get_data_out).read()
				return self.get_data_out

			def wget(self,url):
				self.url = url 
				self.get_data_out = os.popen('wget -qO- %s'% url).read()
				return self.get_data_out

		except:
			continue
			time.sleep(3)
		break

class Spidering(AccessData):

	def cat(self,sleep):
		data = self.get_data_out
		str(data)
		f1 = open('staples_category_urls.txt','w')
		if re.search(r'(?ms)href\=\"([^\"]*cat\_.*?)\"',data):
			main_url = re.findall(r'(?ms)href\=\"([^\"]*cat\_.*?)\"',data)
			for url in main_url:
				#pass
				url = re.sub(r"^","http://staples.com",url)
				print (url)
				f1.write(url+"\n")
		else:
			print ("Match Not Found")
		time.sleep(sleep)
		f1.close()

	def cat1(self,sleep):
		f1 = open('staples_category_urls.txt','r')
		f2 = open('staples_category1_urls.txt','a')
		f3 = open('product_urls.txt','a')
		for url in f1:
			show_content.wget(url)
			data = self.get_data_out
			if re.search(r'(?ms)href\=\"([^\"]*cat\_.*?)\"',data):
				main_url = re.findall(r'(?ms)href\=\"([^\"]*cat\_.*?)\"',data)
				for url in main_url:
				#pass
					url = re.sub(r"^","http://staples.com",url)
					f2.write(url+"\n")
			else:
				print ("Match Not Found")
			if re.search(r'(?ms)href\=\"([^\"]*product\_.*?)\"',data):
				main_url = re.findall(r'(?ms)href\=\"([^\"]*product\_.*?)\"',data)
				for url in main_url:
				#pass
					url = re.sub(r"^","http://staples.com",url)
				
					f2.write(url+"\n")
			time.sleep(sleep)

	def pagination(self,sleep):
		f1 = open('staples_category1_urls.txt','r')
		f2 = open('product_urls.txt','a')
		f3 = open('pagination_urls.txt','a')
		for url in f1:
			show_content.wget(url)
			data = self.get_data_out
			if re.search(r'(?ms)href\=\"([^\"]*product\_.*?)\"',data):
				main_url = re.findall(r'(?ms)href\=\"([^\"]*product\_.*?)\"',data)
				for url in main_url:
				#pass
					url = re.sub(r"^","http://staples.com",url)
				#print (url)
					f2.write(url+"\n")
			else:
				print ("Match Not Found")
			if re.search(r'(?ms)<a\sclass\=\"hide\"\shref\=\"([^\"]*)\"[^>]*><\/a>\s*<li\sclass\="pageNext',data):
				main_url = re.findall(r'(?ms)<a\sclass\=\"hide\"\shref\=\"([^\"]*)\"[^>]*><\/a>\s*<li\sclass\="pageNext',data)
				for url in main_url:
				#pass
					url = re.sub(r"^","http://staples.com",url)
				#print (url)
					f2.write(url+"\n")
			time.sleep(sleep)

	def product(self,sleep):
		f1 = open('staples_category1_urls.txt','r')
		f2 = open('product_urls.txt','a')
		f3 = open('pagination_urls.txt','a')
		for url in f1:
			show_content.wget(url)
			data = self.get_data_out
			if re.search(r'(?ms)href\=\"([^\"]*product\_.*?)\"',data):
				main_url = re.findall(r'(?ms)href\=\"([^\"]*product\_.*?)\"',data)
				for url in main_url:
				#pass
					url = re.sub(r"^","http://staples.com",url)
				
					f2.write(url+"\n")
			else:
				print ("Match Not Found")
			time.sleep(sleep)



sleep = 2
show_content = Spidering()

#show_content.wget("http://www.staples.com/office/supplies/sitemap-html")
#show_content.cat(sleep)
#show_content.cat1(sleep)
show_content.pagination(sleep)
show_content.product(sleep)