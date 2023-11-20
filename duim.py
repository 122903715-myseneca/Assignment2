#!/usr/bin/env python3

import subprocess, sys
import os
import argparse



'''
OPS445 Assignment 2 - Winter 2022
Program: duim.py 
Author: Aleksander Savotchka
The python code in this file (duim.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: Milestone 1 completed. Call_du_sub function and percent_to_graph(). Purpose of code: To return the contents of a directory along with how much drive space the individual is using. Returns the file sizes as a number of bytes.

Date: 2023-11-20
'''

def parse_command_args():
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="DU Improved -- See Disk Usage Report with bar charts",epilog="Copyright 2022")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    # check the docs for an argparse option to store this as a boolean.
    # add argument for "target". set number of args to 1.
    args = parser.parse_args()


def percent_to_graph(percent, total_chars):
    "returns a string: eg. '##  ' for 50 if total_chars == 4"
    # Calculating the number of symbols that must be printed based on the given percent
    num_symbols = round(percent * total_chars / 100)
    # Calculating the number of spaces
    num_spaces = total_chars - num_symbols
    # Returning the string with required symbols and spaces
    return '#' * num_symbols + ' ' * num_spaces

def call_du_sub(location: str) -> list:
    "takes the target directory as an argument and returns a list of strings"
    "returned by the command `du -d 1 location`"
    # Using subprocess to call the du -d 1 + location
    process = subprocess.Popen(['du', '-d', '1', location], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # Decoding the output
    output = stdout.decode('utf-8')
    lines = output.strip().split('\n')
    return lines

def create_dir_dict(alist):
    "gets a list from call_du_sub, returns a dictionary which should have full"
    "directory name as key, and the number of bytes in the directory as the value."
    pass


if __name__ == "__main__":
    pass

