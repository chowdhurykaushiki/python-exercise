# -*- coding: utf-8 -*-
"""
Write a password generator in Python. 
Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, 
generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.
"""
class InvalidInput(Exception):
    pass

class PwdGenerator:   
    def weakPwd(self):
        comboStr=string.ascii_uppercase+string.ascii_lowercase
        weakpwd=''.join(random.choice(comboStr) for x in range(5))
        return (weakpwd)
    def strongPwd(self):
        comboStr=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
        strpwd=''.join(random.choice(comboStr) for x in range(8))
        return strpwd
if __name__=="__main__":
    import string
    import random
    PwdGOBJ=PwdGenerator()
    try:
        pwdIndicator=int(input("Press 1 to generate weak password\n Press 2 to generate strong password: \n"))
        if pwdIndicator not in (1,2):
            raise InvalidInput
        elif pwdIndicator==1:
            print("Your password: ",PwdGOBJ.weakPwd())
        elif pwdIndicator==2:
            print("Your password: ",PwdGOBJ.strongPwd())
    except ValueError :
        print("Invalid input")
    except InvalidInput:
        print("Invalid value entered")
    