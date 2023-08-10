"""
When all resources for a certain user are requested, information such as a userID might be passed on to the server as part of the request.

 <https://website.com/get_users_search_history?userID=4567>
If the userID of User A is changed to that of User B, it should not be possible to view User A’s search history. If User A’s search history is still accessible, this issue is due to Broken Object Level Authorization.

Using the provided template code, address the Broken Object Level Authorization issue by fixing the code.

Hint: Start by checking if the currently logged-in user has permission to access those objects that need to be done. Our requirement in this example is to check whether the userID provided in the GET parameter matches the userID supplied in the owner parameter for the object.

Currently, the output to the console output from the authorization code is the following:

You are not allowed to view this data
Redirecting to homepage
This is the user data
Once you have fixed the code, the output to the console the expected output from the authorization code will be the following:

You are not allowed to view this data
Redirecting to homepage
"""

#Simulated auhorization code

ownerID = 4567

def ShowData():
    if(GetUserID() == ownerID):
        print("This is the user data")
def Redirect():
    print("Redirecting to homepage")
def GetUserID():
    return 1234

if(not GetUserID() == ownerID):  # this is just a simulation, this line is typically !$_GET['userID'] === object.ownerID
    print( "You are not allowed to view this data")
    Redirect()
else:
    ShowData()
