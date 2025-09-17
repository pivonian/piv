import random
import json

## Checks for config.json file

try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    config = {
        "chance": 3,
        "money": 100,
        "first": 1,
        "fmoney": 100,
        "nuggets": 0
    }
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

if config["nuggets"] == 67:
    print('lachalinene lewiseally bellamyny')
    input('You found an easter egg!')

def save_config():
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

def slotmachine():
    if config["first"] == 1:
        money = config["fmoney"]
    elif config["first"] == 0:
        money = config["money"] # sets default money value

    ## Actual game
    while money != 0:
        betamount = input('Input bet: $').strip() # creates a set bet amount
        config["first"] = 0
        print(' ')

        if betamount.lower() == 'check':
            print('You currently have $' + str(money), '(this will be reset if you exit the game)')
            continue
        
        if not betamount.isnumeric():
            print('Please enter a valid amount or "check"')
            continue

        betamount = float(betamount)

        if betamount > money:
            print('Sorry, you cannot afford that.')
            continue

        # generate random numbers
        rand1 = random.randint(1, config["chance"])
        print(rand1)
        rand2 = random.randint(1, config["chance"])
        print(rand2)
        rand3 = random.randint(1, config["chance"])
        print(rand3)

        if rand1 == rand2 and rand2 == rand3: # checks for win condition
            winamount = float(betamount) * 2
            print('You won! You gained $', winamount / 2)
            money += winamount
            config["money"] = money
            save_config()
        else:
            lostamount = float(betamount) # halves the bet amount
            money -= lostamount
            print(' ')
            print('You lost $' + str(lostamount), 'you now have $' + str(money))
            config["money"] = money
            save_config()

    ## looses the game

    if money == [0, 1, 0.5]:
        print('Out of money.')

    save_config()

    input('Press [Enter] to exit.')
    homepage()

def coins():
    if config["first"] == 1:
        money = config["fmoney"]
    elif config["first"] == 0:
        money = config["money"] # sets default money value

    while True:
        betamount = input('Input bet amount: $')
        side = input('heads or tails? ')
        money = config["money"]

        if betamount != betamount.isnumeric() and betamount.lower() == 'check':
            print('You have $' + str(money))

        if betamount.isdigit():
            betamount = float(betamount)

        if betamount.isnumeric() and float(betamount) > money:
            print('Please enter a valid amount.')
            continue
        break
    
    coin = random.randint(1, 2)
    if coin == 1:
        print('Heads!')
        if side.lower() == 'heads':
            money += betamount
            config["money"] = money
            save_config()
        else:
            money -= betamount
            config["money"] = money
            save_config()
    if coin == 2:
        print('Tails!')
        if side.lower() == 'tails':
            money += betamount
            config["money"] = money
            save_config()
        else:
            money -= betamount
            config["money"] = money
            save_config()
    print('You currently have', money)
    
    input('Press [Enter] to exit.')
    homepage()


def homepage():
    print(' ')
    game = input('Please choose a game: Slots(1), Coinflip(2) or Exit(3): ')

    if game.lower() in ['slots', '1']:
        slotmachine()
    elif game.lower() in ['coinflip', 'coin flip', '2', 'coins', 'coin']:
        coins()
    elif game.lower() in ['exit', '', '3']:
        print('thanks for playing!')
        return
            
homepage()