**When creating a new user, an administrator must submit the following fields to an API endpoint:**
 
Name 

Email Address 

Password 

IsAdmin 
 
## What is the best way to ensure the API is protected against privilege escalation? 
 
A. Implement resource and field-level access control

B. Ensure incoming requests are rate limited 

C. Remove IsAdmin from the endpoint 

D. Encrypt the incoming request 

<details>
<summary>Show Answer</summary>

---

The best way to ensure the API is protected against privilege escalation in this scenario is to implement resource and field-level access control. This means controlling which resources (endpoints) users have access to and which fields within those resources they can modify.

By implementing access control, you can define roles and permissions for users. This ensures that only authorized users, such as administrators, can access the endpoint to create new users, and you can restrict who can set the IsAdmin field to True. This prevents regular users from escalating their privileges by setting themselves as administrators.

Options B, C, and D are also important security measures but don't directly address privilege escalation in this context:

B. Ensuring incoming requests are rate limited helps protect against denial of service attacks, but it doesn't directly address privilege escalation.

C. Removing IsAdmin from the endpoint is not a complete solution because it doesn't handle the cases where an administrator legitimately needs to set this field. It's essential to control access to this field instead of removing it entirely.

D. Encrypting the incoming request is a good security practice to protect data in transit, but it doesn't directly prevent privilege escalation. It ensures that the data being sent is secure but doesn't control who has the privilege to set specific fields.

**A. Implement resource and field-level access control (CORRECT)**
</details>
