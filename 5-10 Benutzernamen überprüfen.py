current_users = ['admin', 'leon', 'carlo', 'sabrina', 'diane']
new_user = ['admin', 'carlo', 'sebastian', 'jörg', 'dirk']
for user in new_user:
    if not user in current_users:
      print('invalid')
    else:
      print('login')

