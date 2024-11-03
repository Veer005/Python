import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def main():
    # Ask the user for their name
    name = input("Enter your name: ")

    # Generate ASCII art using pyfiglet
    ascii_art = pyfiglet.figlet_format(name)

    # Display the ASCII art in red
    print(Fore.GREEN + ascii_art)

if __name__ == "__main__":
    main()