current_users = ['anna12', 'beyonce34', 'carl56', 'daddy78', 'edith90']

new_users = ['beyonce34', 'DAddy78', 'faux90', 'goth12', 'hedwig34']

for user in new_users:
    if user.lower() in current_users:
        print('The username ' + user + ' is already in use. Please choose another one.')
    else:
        print('The username ' + user + 'is available.')