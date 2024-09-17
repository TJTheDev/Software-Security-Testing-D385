## Which method is used for a SQL injection attack? 
 
A. Exploiting query parameters

B. Passing safe query parameters 

C. Using SQL composition 

D. Utilizing literal parameters 

<details>
<summary>Show Answer</summary>

---

A SQL injection attack occurs when an attacker maliciously injects SQL (Structured Query Language) code into a vulnerable SQL query, manipulating the query's behavior and potentially gaining unauthorized access to the database or altering its contents. Exploiting query parameters is a common method used in SQL injection attacks.

When the input from query parameters is not properly sanitized or validated, attackers can inject SQL commands as input, causing unexpected and often dangerous actions to occur in the database. This can lead to data leakage, unauthorized access, data modification, and other security vulnerabilities.

It's crucial to properly validate and sanitize user input when constructing SQL queries to prevent SQL injection attacks. Parameterized queries or prepared statements are common techniques used to mitigate SQL injection risks by separating user input from the query structure, making it much more difficult for attackers to inject malicious SQL code.

The other options (B, C, and D) do not specifically describe the method used in a SQL injection attack:

B. Passing safe query parameters is a good practice to prevent SQL injection by properly handling and sanitizing user input, but it's not the method used for an actual SQL injection attack.

C. Using SQL composition, while it may sound related, is not a specific method used to describe an SQL injection attack. It's important to avoid dynamically composing SQL queries with untrusted user input.

D. Utilizing literal parameters doesn't directly relate to SQL injection attacks. In SQL, literal parameters are used to represent constant values directly in a query. The issue in SQL injection is not with literal parameters but with improperly handled dynamic input that can be manipulated by attackers.

**A. Exploiting query parameters (CORRECT)**
</details>
