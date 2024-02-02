import string
import random 


def passwordgen():
    print("\t\t\t\t\tPassword Generator\n\n\n\n")
    len = int(input("Enter the length of the desired password:" ))

    #using random lib to generate random characters
    password = ''.join(random.choices(string.ascii_lowercase+string.digits,k = len))

    print(password)



passwordgen()