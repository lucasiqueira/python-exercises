user_names = ['jake125', 'devk8', 'admin', 'tron3k', '67vip']
# user_names = []

if user_names:
    for name in user_names:
        if name == 'admin':
            print('Hello admin, would you like to see the status report?')
        else:
            print('Hello ' + name + ', thank you for logging in again.')
else:
    print('There are no users in the database.')