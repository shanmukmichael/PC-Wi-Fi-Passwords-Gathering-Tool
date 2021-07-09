# :signal_strength: PC-Wi-Fi-Passwords-Gathering-Tool 
* This is the commandline tool helps to gather SSID &amp; passwords , make a file &amp; send it to recipient's mail
* NOTE : for sending mail you should turn on less secure apps option :link: https://myaccount.google.com/lesssecureapps

### :pushpin: Prerequests 
*  ```python 3 ``` :snake:
*  ```pip install -r requirements.txt```

### Usage
```
python wifi_tool.py [-h] -s S -p P -r R [-f F] [-v]
the following arguments are required: -s, -p, -r

Example : python wifi_tool.py -s shanmukmichael@gmal.com -p password123 -r shanmukmichael@gmal.com -f password_hack.pdf
```

## Tool Options

- ### Help -h | --help
```
python wifi_tool.py -h
```
```
PC Wi-Fi Passwords Gathering Tool
---------------------------------

required arguments:
  -s S           : sender mail id Ex: -s shanmukmichael@gmail.com
  -p P           : sender mail password Ex: -p password123
  -r R           : receiver mail id Ex: -r shanmukmichael@gmail.com

 optional arguments:
  -f F           : filename with .txt (or) .pdf extension
                   DEFAULT filename set as Wi-Fi_Profiles.pdf
  -v, --version  : show tool version
```

- ### Version -v | V
```
python wifi_tool.py -v
```

``` 
 Author: mr_shanmuk

 Github: githhub.com\shanmukmichael

 PC Wi-Fi Passwords Gathering Tool Version : v1.0
```
:beetle: report :link: https://github.comshanmukmichael/PC-Wi-Fi-Passwords-Gathering-Tool/issues
