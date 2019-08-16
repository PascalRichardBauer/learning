user_name = ['admin', 'leon', 'carlo', 'sabrian', 'diane']
for user in user_name:
    if 'admin' in user:
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")