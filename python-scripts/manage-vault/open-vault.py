#!/usr/bin/env python3

'''
This script is ... 
Author: Manoj Kesavulu
Email: manojpratnas@gmail.com
"date: 2023-05-25 14:54:56"
'''

import os
import sys
# get path to the home folder of the user
home = os.path.expanduser("~")

# function to open mount veracrypt volume using a file and pim
def open_vault_pim():
    #check if the veracrypt volume is mounted
    if os.path.ismount("/mnt/veracrypt1/"):
        print("vault is already open!")
        return
    # get the file name from the user
    file_name = home + "/Repos/scripts-and-configs/safe"
    # check if the file exists
    if os.path.isfile(file_name):
        # open the veracrypt volume
        os.system("sudo veracrypt --text --keyfiles='' --protect-hidden=no --mount " + file_name + " /mnt/veracrypt1/")
    else:
        print("File does not exist")


# function to dismount veracrypt volume
def dismount_vault():
    # check if the veracrypt volume is mounted
    if os.path.ismount("/mnt/veracrypt1/"):
        # dismount the veracrypt volume
        os.system("sudo veracrypt --text --non-interactive --dismount /mnt/veracrypt1/")
    else:
        print("veracrypt volume is not mounted")

# main function
def main():
    # check if the user wants to open or close the veracrypt volume
    if sys.argv[1] == "open":
        open_vault_pim()
    elif sys.argv[1] == "close":
        dismount_vault()
    else:
        print("Invalid argument")
    
# call the main function
if __name__ == "__main__":
    main()
