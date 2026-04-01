# Grabify Link Brute Force Tool

import random
import string

base_url = "https://grabify.link/track/"

alphanumeric = list(string.ascii_uppercase) + [str(n) for n in range(10)]

def value_gen():
    link_val = ""
    for _ in range(6):
        link_val += random.choice(alphanumeric)
        req = f"https://grabify.link/track/{link_val}"
    print(req);

def brute_force(x):
    print("Potential Grabify Links (Note: Many links are likely false positives): ")
    y = 0
    while y < x:
        y += 1
        value_gen()

Uques = int(input("How many grabify links would you like to try for?: "));
brute_force(Uques);  