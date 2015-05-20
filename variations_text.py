import urllib.request
import os
import re
import time
import json

class Youtube(object):

	def wget(self,url):
		self.url = url 
		self.data = os.popen('wget -qO- %s'% self.url).read()
		return self.data

class Extract(Youtube):

	def data_out(self):
		products = {}
		results_hash = {}
		results_array = []
		results_array = results_hash
		offers_hash = {}
		results_array = offers_hash
		features_hash = {}
		features_array = {}
		features_hash = features_array
		results_array = features_hash
		variations_hash = {} 
		#varaitions_array = []
		#variations_hash = varaitions_array
		results_array = variations_hash

		products["results"] = results_hash
		products["results"]["offers"] = offers_hash
		products["results"]["features"] = features_hash
		products["results"]["images"] = []
		products["results"]["variations"] = []
		products["results"]["variations"] = variations_hash
		#products["results"]["variations"] = variations_hash

		data= self.data
		if re.search(r'<h1[^>]*>([^<]*)<\/h1',data):
			results_hash["name"] = re.findall(r'(?ms)<h1[^>]*>([^<]*)<\/h1',data)[0]
			#print (name)
			print (results_hash["name"])
		else:
			print ("not found")

		if re.search(r'(?ms)selectLabel">([^<]*)<\/label>',data):
			var_key1 = re.findall(r'(?ms)selectLabel">([^<]*)<\/label>',data)[0]
			co = re.compile(r'(?ms)\s*(\w+)\s*',re.DOTALL | re.IGNORECASE)
			var_key1 = re.sub(co,r"\1",var_key1)
		if re.search(r'(?ms)selectLabel">[^<]*<\/label>.*?selectLabel">[^<]*<\/label>',data):
			var_key2 = re.findall(r'(?ms)selectLabel">[^<]*<\/label>.*?selectLabel">([^<]*)<\/label>',data)[0]
			co = re.compile(r'(?ms)[\n]*\s*(\w+)\s*[\n]*',re.DOTALL | re.IGNORECASE)
			var_key2 = re.sub(co,r"\1",var_key2)

		if re.search(r'(?ms)SkuInventory\"\s\:\[(.*?)\]\}\;',data):
			anchor_par = re.findall(r'(?ms)SkuOptions"\s\:\[(.*?\"\}\]\}\]\}\]\,"AllSkuOptions)|(?ms)SkuOptions"\s\:\[(.*?\"\}\]\}\]\,"AllSkuOptions)|(?ms)SkuOptions"\s\:\[(.*?\"\}\]\,"AllSkuOptions)',data)
			anchor_par = str(anchor_par)
			#print (anchor_par)
			anchor_child = re.findall(r'(?ms)((value":"[^\"]*\","displayValue":"[^\"]*\","skuCode":"[^\"]*\","sizes"\:\[.*?"dimensions".*?\"\}\]\}\])\}|(value":"[^\"]*\".*?,"sizes"\:\[\{"value":"[^\"]*","displayValue":"[^\"]*","skuCode".*?\}\])\}|(value":"[^\"]*\","displayValue":"[^\"]*\","skuCode":"[^\"]*\"))',anchor_par)
			#print (anchor_child)
			for key in anchor_child:
				key = str(key)
				#print (key)
				if re.search(r'(?ms)displayValue\"\:\"[^\"]*\"',key):
					data = re.findall(r'(?ms)displayValue\"\:\"([^\"]*)\"',key)[0]
					#variations_hash[var_key1] = data
					#print (variations_hash)
					if re.search(r'(?ms)sizes"\:\[(.*?"dimensions".*?\}\]\}\])|(?ms)sizes"\:\[(\{"value":"[^\"]*","displayValue":"[^\"]*","skuCode".*?\}\])',anchor_par):
						anc_par_val = re.findall(r'(?ms)sizes"\:\[(.*?"dimensions".*?\}\]\}\])|(?ms)sizes"\:\[(\{"value":"[^\"]*","displayValue":"[^\"]*","skuCode".*?\}\])',anchor_par)
						anc_par_val = str(anc_par_val)
						
						anc_chid_val = re.findall(r'(?ms)((value":"[^\"]*\","displayValue":"[^\"]*\","dimensions.*?}]})|(value":"[^\"]*\","displayValue":"[^\"]*\","skuCode":"[^\"]*\"}))',anc_par_val)
						for value in anc_chid_val:
							#print (type(value))
							
							value = str(value)
							if re.search(r'(?ms)displayValue\"\:\"[^\"]*\"',value):
								#print (value)
								data1 = re.findall(r'(?ms)displayValue\"\:\"([^\"]*)\"',value)[0]
								variations_hash.append({var_key1 : data})
								variations_hash.append({var_key2 : data1})
								print (variations_hash)
					else:
						variations_hash[var_key1] = data
						print (variations_hash)
			#print (products)
		else:
			print ("Variations not found")

show = Extract()
show.wget("http://www.buckle.com/boys-buckle-black-miller-tshirt/prd-34705YB3088/sku-4134240600")
show.data_out()
