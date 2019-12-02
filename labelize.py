import pandas as pd
from readchar.readchar_linux import readchar
import sys

users = ['christina', 'flo', 'jules', 'lucien']

user = "Write your name here!"

if user not in users:
    print("You must tell me your name before labelling !")
    sys.exit()

DATA_FILE = f"./to-label/to-label-{user}.csv"

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def readchar_stdin(prompt):
    char = ""
    answers = ['y', 'n']

    while char not in answers:
        print(f"{prompt} [y/n]: ", end="", flush=True)
        char = readchar()
        print(char)

        # Check if ctrl-c or ctrl-d
        if char == '\x03' or char == '\x04':
            raise KeyboardInterrupt

        # Check if valid answer
        if char not in answers:
            print(f"You must write a character in {answers}!")

    return char == 'y'


def fill_interactive(title, description):
    print(f"{color.UNDERLINE}{color.BOLD}{color.YELLOW}Title{color.END}: {title}\n")
    print(f"{color.UNDERLINE}{color.BOLD}{color.YELLOW}Description{color.END}: {description}\n")

    healthy = readchar_stdin("- Healthy?")
    veg = readchar_stdin("- Vegetarian/vegan?")
    sport = readchar_stdin("- Sport/productivity?")

    about_country = readchar_stdin("- Any country")
    country = None

    if about_country:
        print("- What countries? ", end="", flush=True)
        country = sys.stdin.readline()[:-1] # Remove \n

    print("\n")

    return healthy, veg, sport, country


data = pd.read_csv(DATA_FILE, header=None, names=["asin", "title", "description", "healthy", "vegetarian/vegan", "sport/productivity", "country"])

try:
    to_label = data[data[["healthy", "vegetarian/vegan", "sport/productivity"]].isnull().any(axis=1)]

    print(f"{color.BOLD}{color.GREEN}Welcome back, {user} !")
    print(f"There are {len(to_label.index)} more products to label{color.END}\n")

    for i in to_label.index:
        title = data.loc[i, 'title']
        description = data.loc[i, 'description']

        healthy, veg, sport, country = fill_interactive(title, description)

        data.loc[i, 'healthy'] = healthy
        data.loc[i, 'vegetarian/vegan'] = veg
        data.loc[i, 'sport/productivity'] = sport
        data.loc[i, 'country'] = country

except KeyboardInterrupt:
    print("Saving DataFrame...")
    data.to_csv(DATA_FILE, index=False, header=False)
    print("Saved DataFrame, quitting.")
    sys.exit()
