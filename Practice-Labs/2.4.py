"""
With rate limiting, a unique IP address is restricted from making too many requests in a fixed period of time.

The code snippet below implements rate limiting using a "Token Bucket." Each time a message is received: the bucket is checked for tokens. If the bucket has 1 or more tokens, the algorithm removes one token and sends the message. If no tokens remain in the bucket, the algorithm drops the message.

Complete line #18 to finish the limit() function and ensure that the API only allows 5 messages per every 10 seconds.

See commented lines for detailed instructions.

When correct, this code should produce no output.

The output to the console will be the following:
(Your program produced no output)

"""

import time

# Define a class named Limiter for rate limiting
class Limiter:

    # Constructor (__init__) method to initialize the limiter with rate and per parameters
    def __init__(self, rate, per):
        self.rate = rate
        self.per = per
        self.bucket = rate
        self.last_check = time.time()

    # Method to limit the frequency of a callback function
    def limit(self, callback_fn):
        current = time.time() # Get the current time

        time_passed = current - self.last_check    # Calculate the time passed since the last check
        
        self.last_check = current   # Update the last check time to the current time
      
        # The bucket represents the current available tokens in the rate limiter
        # Finish line 18 by writing an expression that determines the value of the bucket
        # Use the following variables in your expression: time_passed, self.bucket, self.rate, and self.per 
        
        bucket = self.bucket + time_passed * (self.rate / self.per)
      
        # If the calculated bucket value is greater than the rate, reset it to the maximum rate
        if (bucket > self.rate):
            self.bucket = self.rate

        # If the bucket value is less than 1, it means no tokens are available, so do nothing (pass)
        if (bucket < 1):
            pass

        else:
            # Otherwise, if there are available tokens in the bucket, execute the callback function
            callback_fn()

            # Decrease the bucket value by 1 to represent the consumption of one token
            self.bucket = bucket - 1
