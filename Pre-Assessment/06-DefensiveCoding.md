## What are two common defensive coding techniques?

A. Check functional preconditions and postconditions

B. Encrypt passwords and email submissions

C. Adjust length and encoding of messages

D. Develop code with exceptions to find errors


<details>
<summary>Show Answer</summary>

---

- A. Check functional preconditions and postconditions

Functional preconditions and postconditions are common defensive coding techniques used to ensure the correctness and robustness of software. Here's an explanation of these terms:

Preconditions: Functional preconditions are checks that are performed at the beginning of a function or method to verify that the input data or the environment's state is valid and meets the expected criteria. By checking preconditions, developers can ensure that the function can safely proceed with its execution and prevent potential issues or errors that might arise due to invalid data.

Postconditions: Functional postconditions are checks performed at the end of a function or method to ensure that the expected outcomes or results have been achieved. Postconditions help validate that the function has executed correctly and produced the intended results. They also aid in identifying any unexpected behaviors or issues that might have occurred during the execution.

By implementing these checks in the code, developers can significantly reduce the likelihood of errors, crashes, and security vulnerabilities. By catching potential issues early on and providing meaningful feedback to users or other parts of the system, functional preconditions and postconditions contribute to the overall stability and reliability of the software. (CORRECT)

Now let's briefly discuss the other options:

- B. Encrypt passwords and email submissions: While encrypting passwords and sensitive data is an essential security practice, it is not specifically related to "defensive coding techniques." Defensive coding primarily involves writing code in a way that reduces the likelihood of bugs, vulnerabilities, and unexpected behaviors.

- C. Adjust length and encoding of messages: This option seems to refer to data validation and handling, which can be part of defensive coding. However, it is more specific to data sanitization and security practices rather than general "defensive coding techniques" mentioned in the question.

- D. Develop code with exceptions to find errors: While using exceptions in code is a useful approach to handling unexpected situations and error scenarios, it is not a primary technique for "finding errors" in the code. Defensive coding focuses on preventing errors from occurring in the first place or handling them gracefully when they do happen.

### In conclusion, the correct answer is A. Check functional preconditions and postconditions because these techniques play a crucial role in improving the reliability and correctness of software by ensuring valid inputs and expected outcomes in functions and methods.
</details>
