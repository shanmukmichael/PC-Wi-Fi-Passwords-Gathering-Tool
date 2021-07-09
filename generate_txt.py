import sys


def generate_txt(filename,data, SSID, passwords, easy_access, profile_errors):
    with open(filename, 'w') as f:
        sys.stdout = f
        original_stdout = sys.stdout
        data = dict(data)
        data.pop('SSID')
        print('{:<35} : {:<}'.format('SSID', 'PASSWORDS'))
        print('{:<35} : {:<}'.format('----', '---------'))
        for name, pwd in data.items():
            print('{:<35} : {:<}'.format(name, pwd))
            print('\n')
        print('Total Profiles : {} | Passwords : {} | Easy Access : {} | Profile Errors : {}'.format(
            SSID, passwords, easy_access, profile_errors))
        sys.stdout = original_stdout

 
