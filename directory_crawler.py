#!/usr/bin/env python3

import requests # allows to send requests over http

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass
  
target_url = "google.com"	
with open("wordlist.txt", "r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		test_url = target_url + "/" + word 
		response = request(test_url)
		if response:
			print("[+] discovered a URL >> " + test_url)
