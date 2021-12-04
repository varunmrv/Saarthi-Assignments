import re
passw= input("Input your password\n")
s = True
while s:  
    if (len(passw)<6 or len(passw)>16):
        break
    elif not re.search("[a-z]",passw):
        break
    elif not re.search("[0-9]",passw):
        break
    elif not re.search("[A-Z]",passw):
        break
    elif not re.search("[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]",passw):
        break
    else:
        print("Valid Password")
        s=False
        break

if s:
    print("Not a Valid Password")
