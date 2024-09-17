**The user submits the following request to an API endpoint that requires a header:**
 
import requests 
url = 'https://api.github.com/invalid' 
  
try: 
  request_response = requests.get(url) 
  
  "# If the response was successful, no Exception will be raised"
  
  request_response.raise_for_status()  
  
except Exception as err: 

   print(f'Other error occurred: {err}')   
        
else: 
   print('Success!') 
 
## Which response code will the user most likely be presented with? 
 
A. 404—"Not found"

B. 200—"OK"

C. 400—"Bad request"

D. 401—"Unauthorized"

<details>
<summary>Show Answer</summary>

---

In the provided code snippet, the user sends a GET request to the URL 'https://api.github.com/invalid'. This URL suggests that the user is attempting to access a resource that is invalid or not found. The code then uses the requests.get method to send the request and checks if the response was successful using the raise_for_status() method.

The raise_for_status() method raises an exception if the HTTP status code in the response indicates an error (non-2xx status codes). Since the URL contains the word "invalid," it's likely that the server will return a 404 status code, which means "Not found." This status code indicates that the requested resource does not exist on the server.

Therefore, the user is most likely to be presented with a 404 response code, indicating that the requested resource could not be found.

The other options are less likely based on the provided URL and the typical use of these status codes:

B. 200—"OK": This status code indicates that the request was successful. Given that the URL contains "invalid," it's unlikely that a 200 status code would be returned.

C. 400—"Bad request": This status code indicates that the request was malformed or could not be understood by the server. The URL itself is not malformed; it simply points to a resource that is likely not found.

D. 401—"Unauthorized": This status code indicates that the request requires authentication, and the user is not authorized to access the resource. While authentication could be a possibility, the more common scenario based on the URL is that the resource is not found, leading to a 404 response.

**A. 404—"Not found" (CORRECT)**
</details>
