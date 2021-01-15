def print_message():
  print ("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def extra_options():
  res = input('Do you want a mug for here, a cup to-go, or a refill of your own cup? \n[a] I\'ll have it here in a mug. \n[b] I ll take a plastic cup to go! \n[c] I brought my own! > ').lower()
 
 if res == 'a':
   print('Awesome! Your order will be ready in a mug soon!')
 elif res == 'b':
    print('Okay, no problem! We\'ll get you a plastic cup.')
 elif res == 'c':
    print('Great! We\'ll fill up your reusable cup.')
 else:
    print_message()
    return extra_options()
              
def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>").lower()
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
def order_latte():
  milk = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n[d] Almond milk \n[e] Oatmilk \n[f] Hemp milk>").lower()
  if milk == 'a':
    return 'latte'
  elif milk == 'b':
    return 'non-fat latte'
  elif milk == 'c':
    return 'soy latte'
	elif milk == 'd':
	  return 'almond latte'
	elif milk == 'e':
	  return 'oat latte'
	elif milk == 'f':
	  return 'hemp latte'
  else:
    print_message()
    return order_latte()

def extra_options():
  res = input('Would you like a plastic cup or did you bring your own reusable cup? \n[a] I\'ll need a cup. \n[b] Brought my own! \n> ')
  
  if res == 'a':
    print('Okay, no problem! We\'ll get you a plastic cup.')
  elif res == 'b':
    print('Great! We\'ll fill up your reusable cup.')
  else:
    print_message()
    return extra_options()


def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>").lower()
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ').lower()
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  print("Alright, that's a {} {}.".format(size, drink_type))

  extra_options()
  
  name = input("Can I get your name please?")
  print("Thanks, {}! Your drink will be ready shortly".format(name))
 
coffee_bot()