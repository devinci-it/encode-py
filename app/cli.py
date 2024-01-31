import argparse
from app.encoder import encode_base64, decode_base64, encode_url, decode_url, encode_html, decode_html
from prettytable import PrettyTable
import click
import os

def clear_screen():
    """
    Clear the CLI screen based on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def display_results(data, result, encoding_type):
    """
    Display the results in a pretty table format.

    Parameters:
    - data (str): The input string.
    - result (str): The encoded or decoded string.
    - encoding_type (str): The type of encoding used.
    """
    table = PrettyTable()
    table.field_names = ["Input String", "Result", "Encoding Type"]
    table.add_row([data, result, encoding_type])
    print(table)

def print_banner():
    """
    Print the banner for the script.
    """
    banner = """
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    █░▄▄█░▄▄▀█▀▄▀█▀▄▄▀█░▄▀█░▄▄
    █░▄▄█░██░█░█▀█░██░█░█░█░▄▄
    █▄▄▄█▄██▄██▄███▄▄██▄▄██▄▄▄
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        String Encoder CLI App
        Author: devinci-it
        2024
        MIT License
    """
    print(banner)

@click.command()
@click.option('-e', '--encode', is_flag=True, help='Encode input string')
@click.option('-d', '--decode', is_flag=True, help='Decode input string')
@click.option('-c', '--continuous', is_flag=True, help='Continuous mode for encoding/decoding')
@click.option('-t', '--type', type=click.Choice(['base64', 'url', 'html']), default='base64', help='Select encoding type (default: base64)')
@click.option('-i', '--interactive', is_flag=True, help='Interactive mode for encoding/decoding')
@click.option('-h', '--help', is_flag=True, help='Show help message')
def main(encode, decode, continuous, type, interactive, help):
    """
    Encode/decode strings using various methods.

    Parameters:
    - encode (bool): Flag for encoding mode.
    - decode (bool): Flag for decoding mode.
    - continuous (bool): Flag for continuous mode.
    - type (str): Encoding type (base64, url, html).
    - interactive (bool): Flag for interactive mode.
    - help (bool): Show help message.
    """
    if help:
        print_banner()
        print("Usage: python cli.py [OPTIONS]\n")
        print("Options:")
        print("-e, --encode      Encode input string")
        print("-d, --decode      Decode input string")
        print("-c, --continuous  Continuous mode for encoding/decoding")
        print("-t, --type TEXT   Select encoding type (default: base64)")
        print("-i, --interactive Interactive mode for encoding/decoding")
        print("-h, --help        Show this message and exit")
        return

    print_banner()

    if interactive:
        print("Welcome to String Encoder Interactive Mode!")
        print("Choose an encoding type:")
        print("1. Base64")
        print("2. URL")
        print("3. HTML")

        choice = input("Enter the number of your choice (1/2/3): ")

        encoding_functions = {
            '1': (encode_base64, decode_base64),
            '2': (encode_url, decode_url),
            '3': (encode_html, decode_html),
        }

        if choice not in encoding_functions:
            print("Invalid choice. Exiting.")
            return

        encode_func, decode_func = encoding_functions[choice]

        while True:
            clear_screen()
            data = input("Enter the string:")

            if encode:
                result = encode_func(data)
                display_results(data, result, type)
            elif decode:
                result = decode_func(data)
                display_results(data, result, type)

            if not continuous:
                break

    else:
        pass

if __name__ == '__main__':
    main()
