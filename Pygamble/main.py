import os, sys, random, json
import chicken_counter, blackjack  # import instead of subprocess

# Helper for PyInstaller resource paths
def resource_path(relative_path):
    base = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(base, relative_path)

CONFIG_FILE = resource_path("config.json")

# Load or create config.json
try:
    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    config = {"chance": 3, "money": 100, "first": 1, "fmoney": 100, "nuggets": 0}
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

if config["nuggets"] == 67:
    print("lachalinene lewiseally bellamyny")
    input("You found an easter egg!")

def save_config():
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

# --- Slots game ---
def slotmachine():
    money = config["fmoney"] if config["first"] == 1 else config["money"]

    while money > 0:
        betamount = input("Input bet: $").strip()
        config["first"] = 0
        print()

        if betamount.lower() == "check":
            print("You currently have $", money)
            continue

        if not betamount.isnumeric():
            print("Please enter a valid amount or 'check'")
            continue

        betamount = float(betamount)
        if betamount > money:
            print("Sorry, you cannot afford that.")
            continue

        # random rolls
        rand1, rand2, rand3 = [random.randint(1, config["chance"]) for _ in range(3)]
        print(rand1, rand2, rand3)

        if rand1 == rand2 == rand3:
            winamount = betamount * 2
            print("You won! You gained $", winamount / 2)
            money += winamount
        else:
            money -= betamount
            print("You lost $", betamount, "you now have $", money)

        config["money"] = money
        save_config()

    print("Out of money.")
    save_config()
    input("Press [Enter] to exit.")
    homepage()

# --- Coinflip ---
def coins():
    money = config["fmoney"] if config["first"] == 1 else config["money"]

    while True:
        try:
            betamount = float(input("Input bet amount: $"))
        except ValueError:
            print("Enter a valid number.")
            continue

        side = input("heads or tails? ").lower()

        if betamount > money:
            print("Not enough money.")
            continue
        break

    coin = random.choice(["heads", "tails"])
    print(coin.capitalize() + "!")

    if side == coin:
        money += betamount
    else:
        money -= betamount

    config["money"] = money
    save_config()

    print("You currently have", money)
    input("Press [Enter] to exit.")
    homepage()

# --- Homepage ---
def homepage():
    print()
    game = input("Choose: Slots(1), Coinflip(2), Chicken Counter(3), Blackjack(4), Exit(5): ")

    if game.lower() in ['slots','1']:
        slotmachine()
    elif game.lower() in ['coinflip','2','coin','coins']:
        coins()
    elif game.lower() in ['chicken','3']:
        chicken_counter.play()
        homepage()
    elif game.lower() in ['blackjack','4']:
        blackjack.play()
        homepage()
    elif game.lower() in ['exit','5','']:
        print("Thanks for playing!")
        return

if __name__ == "__main__":
    homepage()
