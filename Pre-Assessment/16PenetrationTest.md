Consider the following penetration test: 
 
import requests 
urls = open("websites.txt", "r") 
  
for url in urls: 
   url = url.strip() 
   req = requests.get(url) 
   print (url, 'reportde02 
 
  try: 
      transport_security = req.headers['Strict-Transport-Security'] 
   except: 
      print ('HSTS header not set properly') 
 
Which security vulnerability is shown? 
 
A. Man-in-the-middle  (CORRECT)
B. Cross-site scripting 
C. Denial of service
D. Code injection 
