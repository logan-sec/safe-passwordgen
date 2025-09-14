import secrets # cryptographically secure random numbers
import string # gives you ready-made sets of characters
import argparse # lets you add nice command-line options

parser = argparse.ArgumentParser(description="Random password generator")
parser.add_argument("--length", type=int, default=36, help="Length of the password (default: 36)")

args = parser.parse_args()

if args.length < 8:
    print("Error: password length must be at least 8")
    exit(1)

alphabet = string.ascii_letters + string.digits + string.punctuation 
password = ''.join (secrets.choice(alphabet) for _ in range(args.length)) 

question = input("Do you want me to print password? 'yes' or 'no' ")
if question == "yes":
    print(password)

elif question == "no":
    print("password will not be printed. ")

else:
    print("password will not be printed. ")