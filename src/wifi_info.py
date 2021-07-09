import subprocess
from tqdm import tqdm


def wifi_info():

    cmd_data = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    # print(data)
    profile_names = [profiles.split(':')[1][1:-1]
                    for profiles in cmd_data if "All User Profile" in profiles]
    if len(profile_names) != 0:
        names = ['SSID']
        pwds = ['PASSWORDS']
        SSID = len(profile_names)
        passwords = 0
        easy_access = 0
        profile_errors = 0
        data = zip(names, pwds)
        for wifi_name in tqdm(profile_names):
            try:
                wifi_info = subprocess.check_output(
                    ['netsh', 'wlan', 'show', 'profiles', wifi_name, 'key=clear']).decode('utf-8').split('\n')
                password = [key.split(':')[1][1:-1]
                            for key in wifi_info if "Key Content" in key]

                if len(password) != 0:
                    names.append(wifi_name)
                    pwds.append(password[0])
                    passwords += 1
                else:
                    names.append(wifi_name)
                    pwds.append('')
                    easy_access += 1

            except Exception as CalledProcessError:
                no_profile = '"'+wifi_name+'" profile not found'
                names.append(no_profile)
                pwds.append('--------')
                profile_errors += 1
                continue
        return data, SSID, passwords, easy_access, profile_errors

    else:
        print("No Profiles Found")

