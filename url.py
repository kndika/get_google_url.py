banner ="""
                _                 _             
               | |               (_)            
 __      _____ | |_   _____  _ __ _ _ __   __ _ 
 \ \ /\ / / _ \| \ \ / / _ \| '__| | '_ \ / _` |
  \ V  V / (_) | |\ V / (_) | |  | | | | | (_| |
   \_/\_/ \___/|_| \_/ \___/|_|  |_|_| |_|\__, |
                                           __/ |
                                          |___/ 


Cording By Wolvoring

exampal

wrong  = inurl:/index.php?option=com_fabrik
correct= index.php?option=com_fabrik

url https://gbhackers.com/latest-google-dorks-list/
"""
print (banner)
import os
name =raw_input("Enter a google dorks:")
#name = input("Enter a google dorks:")
try: 
	from googlesearch import search 
except ImportError: 
	print("No module named 'google' found") 

# to search 
query = name
print ('geting some url waiting..............................!')
for j in search(query, tld="co.in", num=2000, stop=80, pause=20):
 
	f=open('temp.txt','a')
	f.write('\n'+(j))
	f.close()
with open("temp.txt","r") as f:
    lines = f.read()
    lines = lines.replace("http://","")
    lines = lines.replace("https://","")
    lines = lines.replace("www.", "")
    urls = [url.split('/')[0] for url in lines.split()]
    
    f=open('list.txt','a')
    f.write('\n'.join(urls))
    f.close()
    
#os.remove("temp.txt")

print ('export to txt and clen ..........................................................!')
print ('Job finish')


import time
import sys


animation = "|/-\\"

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print ('End!')
