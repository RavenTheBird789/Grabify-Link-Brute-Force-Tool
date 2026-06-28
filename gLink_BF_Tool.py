# Grabify Link Brute Force Tool

import random
import requests
import string

def green(text: str) -> str: 
    # Wrap text in ANSI codes for green color
    return f"\033[92m{text}\033[0m"

def bold(text: str) -> str: 
    # Wrap text in ANSI codes for bold formatting
    return f"\033[1m{text}\033[0m"

def red(text: str) -> str: 
    # Wrap text in ANSI codes for red color
    return f"\033[91m{text}\033[0m"

def yellow(text: str) -> str:
    # Wrap text in ANSI codes for yellow color
    return f"\033[93m{text}\033[0m"

equalSign = "="
emptySpace = "     "

def trademark(bf_func):
    def wrapper(args):
        print(green(equalSign * 30))
        print(green(bold("Grabify Link Brute Force Tool")))
        print(green(equalSign * 30))
        print(red(emptySpace + "By: RavenTheBird789"))
        print(green(equalSign * 30))
        bf_func(args)
    return wrapper

base_url = "https://grabify.link/track/"

alphanumeric = list(string.ascii_uppercase) + [str(n) for n in range(10)]

@trademark
def brute_force(x):
    print(green("Potential Grabify Links (Note: Many links are likely false positives): "))
    y = 0
    link_val = ""
    while y < x:
        y += 1
        for _ in range(6):
            link_val += random.choice(alphanumeric)
            req = f"{base_url}{link_val}"
        response = requests.get(req)
        if response.status_code == 200:
            print(green(f"{y}. {req} Success: {response}"))
        elif response.status_code == 404:
            print(red(f"{y}. {req} Error: {response}"))
        else:
            print(yellow(f"{y}. {req} Error: {response}"))
        link_val = ""

Uques = int(input(green(bold("How many grabify links would you like to try for?: "))));
brute_force(Uques);