from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choices
# import sys
import argparse


def create_password(length=8, upper=False, lower=False,
                    digit=False, pun=True):

    pool = ''

    if lower:
        pool += ascii_lowercase

    if upper:
        pool += ascii_uppercase

    if digit:
        pool += digits 

    if pun:
        pool += punctuation

    if pool != '':
        return ''.join(choices(pool, k=length))



#ignore this if you don't want to use argv
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

parser.add_argument("n", type=int, help = "length of password")
parser.add_argument("-l", "--lowercase", help="Use lowercase", action="store_true")
parser.add_argument("-u", "--uppercase", help="Use uppercase", action="store_true")
parser.add_argument("-d", "--digit", help="Use digit", action="store_true")
parser.add_argument("-p", "--punctuation", help="Use punctuation", action="store_true")

args = parser.parse_args()

print(create_password(length=args.n, lower=args.lowercase, upper=args.uppercase, digit=args.digit,pun=args.punctuation))









# parser = argparse.ArgumentParser(description='multiple X to Y')
# group = parser.add_mutually_exclusive_group()
#
# group.add_argument("-q", "--quiet", action="store_true")
# group.add_argument("-v", "--verbose" ,action="store_true")
#
# parser.add_argument("x", type=int, help='first number')
# parser.add_argument("y", type=int, help='second number')
#
# args = parser.parse_args()
#
# answer = args.x * args.y
#
#
# if args.verbose:
#     print(f"running {__file__}")
# elif args.quiet:
#     print(f"{args.x}*{args.y} == {answer}")
# else:
#     print(answer)