# Importing requests to get information from websites
# Importing random to randomly pick dad joke
# Importing pyfiglet & colorama to create colorized ASCII art for the header
import requests
import random
import pyfiglet
from colorama import Fore, Back, init

# Resets colorama settings after each time it is ran
init(autoreset=True)

# Creating the ASCII art and saving it to a variable
header = pyfiglet.figlet_format("DAD JOKES 3000", font="standard")

# Colorizing and printing the ASCII art
print(Fore.RED + header)

# Asking the user for a joke topic, & saving it to a variable
user_choice = input("What do you want to hear a joke about?: ")

# Requesting dad jokes from website
url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_choice})

# Turning response into dict via .json, stripping away other uneeded
# information and compiling jokes into one full list
data = response.json()
joke_dict = data["results"]
jokes = [li['joke'] for li in joke_dict]

# This will count the amount of jokes on the subject the user entered
joke_count = 0
for x in jokes:
    joke_count += 1

# If any jokes are returned, one is picked at random and printed, else print that none are found
if joke_count > 0:
    print(f"Okay! I have {joke_count} jokes about {user_choice}s, here's one!")
    dad_joke = random.choice(jokes)
    print(dad_joke)
else:
    print("Sorry, I don't have any jokes about that...")
