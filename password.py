# Import libraries
import sys
import getpass
import pickle
import bcrypt

# Access user password list stored in seperate file
with open('user_list_hashed.pkl', 'rb') as pickle_file:
    user_pw = pickle.load(pickle_file)

# Function to compare unhashed and hashed pssword
def check_password(plain_text_pw, hashed_pw):
    return bcrypt.checkpw(plain_text_pw, hashed_pw)

# Function checking for valid user credentials
def user_validation():
    user = getpass.getuser() # Get user from environment variable

    if user in user_pw.keys(): # Check if user name available
        print("You have a valid account!")
        print("Your user name is: " + user)  # Display user name
    else:
        print("Please sign up first!")
        exit()

    hashed_pw = user_pw[user] # Get password from user password list

    pw = getpass.getpass() # Prompting for password without displaying it
    pw = pw.encode('utf8') # utf8 encoding

    if check_password(pw, hashed_pw): # Check if password valid
        print("Welcome!")
    else: 
        print("Wrong password!")

# Execute program
if __name__ == '__main__':
    user_validation()

    

