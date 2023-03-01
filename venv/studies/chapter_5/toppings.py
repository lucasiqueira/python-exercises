available_topping = ['mushrooms', 'olives', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['pepperoni', 'onion', 'extra cheese']
#requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        if topping in available_topping:
            print('Adding ' + topping + '.')
        else:
            print("Sorry, we don't have " + topping + ".")
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')