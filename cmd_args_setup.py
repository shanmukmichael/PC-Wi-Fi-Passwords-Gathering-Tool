import argparse
from argparse import  RawTextHelpFormatter

__version__ ='''
 Author: mr_shanmuk\n
 Github: githhub.com\\shanmukmichael\n
 PC Wi-Fi Passwords Gathering Tool Version : 0.1\n
'''
__description__= '''
 Author: mr_shanmuk\n
 Github: github.com\\shanmukmichael\n
 PC Wi-Fi Passwords Gathering Tool\n ---------------------------------'''

def cmd_setup():
    parser = argparse.ArgumentParser(description=__description__, formatter_class=RawTextHelpFormatter)
    parser._action_groups.pop()
    required = parser.add_argument_group(' required arguments')

    required.add_argument('-s', type=str,
                        help=': sender mail id', required=True)

    required.add_argument('-p', type=str,
                        help=': sender mail password', required=True)

    required.add_argument('-r', type=str,
                        help=': receiver mail id', required=True)

    optional = parser.add_argument_group(' optional arguments')

    optional.add_argument('-f', type=str, default='Wi-Fi_Profiles.pdf',
                        help=''': filename with .txt (or) .pdf extension\n  DEFAULT filename set as Wi-Fi_Profiles.pdf''')

    optional.add_argument('-v', '--version', action='version', version=__version__, help=": show tool version")

    args = parser.parse_args()

    return args.s, args.p, args.r, args.f
