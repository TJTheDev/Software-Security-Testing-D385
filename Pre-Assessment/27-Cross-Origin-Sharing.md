## What does cross-origin resource sharing (CORS) allow users to do? 
 
A. Override same starting policy for specific resources

B. Connect web security models

C. Prevent the passing of credentials

D. Protect the client header from exposure

<details>
<summary>Show Answer</summary>

---

Cross-Origin Resource Sharing (CORS) is a web security feature that allows web pages from one domain to make requests for resources (such as scripts, stylesheets, and data) from a different domain. This capability, provided by CORS, allows certain resources to bypass the same-origin policy, which restricts web pages from making requests to a different domain for security reasons.

The same-origin policy prevents web pages from making requests to domains other than the one from which the web page originated, to mitigate potential security risks. However, there are valid scenarios where a web page hosted on one domain needs to request resources from a different domain (cross-origin requests), such as loading data from a third-party API.

CORS allows users to override the same-origin policy for specific resources by defining rules on the server-side to specify which domains are allowed to access the resources. This helps protect against unauthorized access while still enabling legitimate cross-origin requests.

The other options:

B. Connect web security models: This option does not accurately describe the purpose of CORS. CORS is a security feature that deals specifically with cross-origin requests and does not directly connect web security models.

C. Prevent the passing of credentials: CORS does not primarily prevent the passing of credentials. Instead, it can control how credentials (such as cookies and HTTP authentication) are included in cross-origin requests.

D. Protect the client header from exposure: This option does not accurately describe the purpose of CORS. CORS is focused on controlling cross-origin requests, not specifically protecting client headers from exposure.

**A. Override same starting policy for specific resources (CORRECT)**
</details>
