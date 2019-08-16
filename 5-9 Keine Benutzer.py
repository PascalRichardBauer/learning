user_name = []
for user in user_name:
    if 'admin' in user:
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")
    
if user_name:
    for user in user_name:
        print("Hello "  + user + ", thank you for logging in again.")
else: 
    print("We need to find more users!")