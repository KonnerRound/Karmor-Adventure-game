print('This is a new game created by Konner Round.')
name = input('Enter your name! ')
print(f'Greetings {name}! Welcome to your adventure')
start = input('Would you rather play the game or parish to the unknown world of karmor?')
if start == 'play':
    print("Great! Let's play the game! ")
    setting = input('Want to go to the Stronghold, or go to the trading city? ')
else:
    print('Lame. Okay you\'re dead now...')
    quit()

if setting == 'trading city':
    print("Welcome to the Trading City, here you can sell or buy new items for your journey, or you can go to the tavern and meet new people and find quests, you\'re tour guide told you to wait here...")
    response = input("But he has been gone a long time... Follow him or wait here?")
    if response == 'follow':
        print("you follow him into the town...")
    elif response == 'wait':
        print("You wait another ten minutes and he still ins\'t here!")
    else:
        print('invalid response! you lose!')
        quit()

if setting == 'stronghold':
    print("Welcome to the StrongHold, here you can sell or buy new items for your journey, or you can go to the tavern and meet new people and find quests, you\'re tour guide told you to wait here...")
    response = input("But he has been gone a long time... Follow him or wait here?")
    if response == 'follow':
        print("you follow him into the Castle...")
    elif response == 'wait':
        print("You wait another ten minutes and he still ins\'t here!")
    else:
        print('invalid response! you lose!')
        quit()
else:
    print('invalid response! you lose!')
    quit()