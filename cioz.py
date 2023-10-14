import requests
import time
import random
import pyfiglet
from termcolor import colored
import os

def clear_console():
    os.system('clear')

def print_banner():
    banner = "CIOZ TRACKER"
    print(colored('CIOZ TRCKR 0.1v', 'red'))
    ascii_banner = pyfiglet.figlet_format(banner)
    for char in ascii_banner.rstrip():
        color = random.choice(['red', 'yellow', 'green', 'cyan', 'blue', 'magenta'])
        print(colored(char, color), end='')
        time.sleep(0.0)
    print(colored('\nCoded By CioZ', 'green'))
    print(colored('github.com/ciozru / Discord: thecioz', 'cyan'))

def get_location_details(ip_address):
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    data = response.json()
    if data['status'] == 'success':
        print(colored(f"\nIP Address: {colored(data['query'], 'red')}", 'green'))
        print(colored(f"City: {colored(data['city'], 'red')}", 'green'))
        print(colored(f"Region: {colored(data['regionName'], 'red')}", 'green'))
        print(colored(f"Country: {colored(data['country'], 'red')}", 'green'))
        print(colored(f"Postal Code: {colored(data['zip'], 'red')}", 'green'))
        print(colored(f"Location: {colored(data['lat'], 'red')}, {colored(data['lon'], 'red')}", 'green'))
        print(colored(f"Organization: {colored(data['org'], 'red')}", 'green'))
    else:
        print(colored("\nUnable to retrieve IP address details", 'yellow'))
        print(colored("It's possibly because you gave the wrong IP address.", 'red'))

def main():
    clear_console()
    print_banner()
    while True:
        ip_address = input(colored("\nIP address: ", 'green'))
        get_location_details(ip_address)
        choice = input(colored("\nDo you want to check another IP address? (Y/N) ", 'green')).lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
