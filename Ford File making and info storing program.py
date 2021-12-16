from genericpath import isfile
import os

def main():
    print("welcome to the person information saver program!\nThis program will save your name, address, and phone number to a file")
    dirchoice = input("please enter the directory in which you want to save your file to. You are \
currently in the " + curdir + " directory. \nYou can copy and paste this directory to save the file or specify a new directory using the same format:\n")
#if the directory exists, the program moves on, if not it creates a directory using the makedirs syntax
    if os.path.isdir(dirchoice) == True:
        filemake(dirchoice)
    elif os.path.isdir(dirchoice) == False:
        try:
            os.makedirs(dirchoice)
        #if directory cannot be made at specified address, it makes user choose again
        except:
            print("error, can not make a directory there! check your spelling and syntax!")
            main()
        print("creating new directory...")
        filemake(dirchoice)
def filemake(dirchoice):
    #asks the user for a filename along with their info and is stored in variables
    filename = input("please enter a filename for the file. Please only use letters and do not add extensions:\n")
    print ("opening file...")
    #appends a .txt to the filename in order to make it a text file
    filename = filename + ".txt"
    name = input("please enter your name: ")
    address = input("please enter your address: ")
    phone_number = input("please enter your phone number: ")
    #if the file exists already, it simply appends to the file with a new entry
    if os.path.isfile(os.path.join(dirchoice,filename)) == True:
        with open(os.path.join(dirchoice,filename), "a") as f:
            f.write(name + ", " + address + ", " + phone_number + "\n")
    #if the file does not exist, it will write a new file
    if os.path.isfile(os.path.join(dirchoice,filename)) == False:
        with open(os.path.join(dirchoice,filename), "w") as f:
            #simply combines the user data to write to file
            f.write(name + ", " + address + ", " + phone_number + "\n")
    #opens and reads contents of file to user
    with open(os.path.join(dirchoice,filename)) as f:
        print("opening file...\n")
        contents = f.read()
        print(contents)
#uses the get current working directory to save the directory to a variable
curdir = str(os.getcwd())
main()