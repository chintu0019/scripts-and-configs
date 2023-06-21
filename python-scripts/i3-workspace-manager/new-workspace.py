#!/usr/bin python3

'''
This script is to create a new workspace or move the current container to the next workspace using i3-msg
Author: Manoj Kesavulu
Email: manojpratnas@gmail.com
"date: 2023-06-21 12:47:27"
'''

import os
import sys

# function to get the total number of workspaces using i3-msg
def get_total_workspaces():
    # get the total number of workspaces
    total_workspaces = os.popen("i3-msg -t get_workspaces | jq '. | length'").read()
    # convert the string to integer
    total_workspaces = int(total_workspaces)
    return total_workspaces

# function to create a new workspace using i3-msg
def create_new_workspace():
    # get the total number of workspaces
    total_workspaces = get_total_workspaces()
    # create a new workspace
    os.system("i3-msg workspace " + str(total_workspaces + 1))

# function to move current container to the next workspace using i3-msg and focus on it
def move_container_to_next_workspace():
    # get the total number of workspaces
    total_workspaces = get_total_workspaces()
    # move the current container to the next workspace
    os.system("i3-msg move container to workspace " + str(total_workspaces + 1))
    # focus on the next workspace
    os.system("i3-msg workspace " + str(total_workspaces + 1))

# main function
def main():
    # check if the user wants to create a new workspace or move the current container to the next workspace
    if sys.argv[1] == "create":
        create_new_workspace()
    elif sys.argv[1] == "move":
        move_container_to_next_workspace()
    else:
        print("Invalid argument")

# call the main function
if __name__ == "__main__":
    main()

