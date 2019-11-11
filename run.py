#! /usr/bin/env python3.6

import random
from users import Users
from credentials import Credentials
import pyperclip

def create_user(fname, lname, email, usrname, password):
    '''
    Create a new user
    '''

    new_user = Users(fname, lname, email, usrname, password)
    return new_user

def save_user(account):
    '''
    Saves the provided user in the users list
    '''

    Users.save_user(account)

def create_credential(account, username, password):
    '''
    create a credential
    '''

    new_credential = Credentials(account, username, password)
    return new_credential

def save_credential(account):
    '''
    saves the provided credential in the credentials list
    '''

    Credentials.save_credential(account)

def find_user(username):
    '''
    Search for a user using a username
    '''

    found_user = Users.find_user(username)
    return found_user

def find_credential(password):
    '''
    Find a credential using the password
    '''

    return Credentials.find_by_password(password)

def del_user(username):
    '''
    Remove  a user from the user list
    '''
    found_user = Users.find_user(username)
    Users.delete_user(found_user)

def del_credential(password):
    '''
    Remove a credential based on its account id
    '''

    found_credential = Credentials.find_by_password(password)
    Credentials.delete_credential(found_credential)

def find_all_users():
    '''
    Show all saved users
    '''

    return Users.show_all()

def find_all_credentials():
    '''
    Show all saved credentials
    '''

    return Credentials.display_all()

def main():
    print("Welcome to the Password Locker")

    print("Select L to login or R to register")
    response = input().lower()
  
    while True:  
        if response == 'l':
            
            print("Username .....")
            usr = input().lower()

            print("Password .....")
            passwrd = input().lower()

            found = find_user(usr)

            
            if(found):
                
                if((found.username == usr) and (found.password == passwrd)):
                    print(f"Hello {found.first_name} {found.last_name}, Welcome back.")
                    print("What would you like to do? Select the following short codes to perform the following actions")
                    
                    while True:
                        print('*'*20)
                        print("Select: CC to create a credential; FC to find a credential; SA to show all credentials; DC to delete a credential; EX to exit")
                        
                        selection = input().lower()

                        if(selection == 'cc'):
                            print("Would you like to select the password yourself? Y/N")
                            resp = input().lower()

                            if resp == 'y':
                                print("Account(e.g facebook, twitter, etc ...)")
                                acc = input().lower()

                                print("Preferred username .......")
                                usrname = input().lower()

                                print("password ...........")
                                pswrd = input().lower()

                                save_credential(create_credential(acc, usrname, pswrd))
                                found_cred = find_credential(pswrd)
                                if(found_cred):
                                    print(f"Your credential for {found_cred.account_name} has been saved successfully")
                                    continue
                                    
                            
                            elif resp == 'n':
                                rang = range(2000, 2019)
                                rand = []
                                for x in rang:
                                    rand.append(str(x))

                                print("Account(e.g facebook, twitter, etc ...)")
                                acc = input().lower()

                                print("Preferred username .......")
                                usrname = input().lower()

                                pswrd = (usrname + random.choice(rand))
                                save_credential(create_credential(acc, usrname, pswrd))
                                found_cred = find_credential(pswrd)

                                if(found_cred):
                                    
                                    print(f"Your credential for {found_cred.account_name} has been saved successfully")

                                    print(f"Your password is {found_cred.password}")
                                    continue
                                else:
                                    print("There was a problem, exiting ......")
                                    break

                        elif selection == 'fc':
                            print("Please provide a password for the credential to be found")
                            rspns = input().lower()

                            found = find_credential(rspns)
                            print(f"for {found.account_name} account, username: {found.username} ....... password: {found.password}")

                        elif selection == 'sa':
                            if(find_all_credentials()):
                                for cred in find_all_credentials():
                                    print(f"Account name: {cred.account_name}....Username: {cred.username}....password: {cred.password}")
                            else:
                                print("There seems to be no credential saved")

                        elif selection == 'dc':
                            print("Kindly provide a password for the account to be removed")
                            inpt = input().lower()

                            del_credential(inpt)
                            print("Your credential has been deleted")

                        elif selection == 'ex':
                            print("Exiting now .........")
                            return

                        else:
                            print("Sorry, i didnt quite catch that, please try again")
                            continue
                                

                else:
                    print("Username not found, please try again")
                    response = 'l'
                    continue
            else:
                print("Username not found, please register first")
                response = 'r'
                continue

        elif response == 'r':
            print("First name ......")
            fname = input().lower()

            print("Last name ......")
            lname = input().lower()

            print("Email ........")
            email = input().lower()

            print("Prefered username .......")
            username = input().lower()

            print("Password ..............")
            password = input().lower()
            
            save_user(create_user(fname, lname, email, username, password))
            for user in find_all_users():
                print(f"{user.username} {user.password}")
                print("Your account has been created, proceed to login? Y/N")
                rspnse = input().lower()
                if rspnse == 'y':
                    response = 'l'
                    continue 
                elif rspnse == 'n':
                    break
                else:
                    print("please try again")
            

        else:
            print("I didnt quite catch that, kindly try again")


if __name__ == '__main__':
    main()
