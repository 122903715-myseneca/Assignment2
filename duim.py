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

Descriptiotn: Milestone 1 completed. Call_du_sub function and percent_to_graph(). Purpose of code: To return the contents of a directory along with how much drive space the individual is using. Returns the file sizes as a number of bytes.
Date: 2023-11-20
'''

def parse_command_args():
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="DU Improved -- See Disk Usage Report with bar charts",epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    # check the docs for an argparse option to store this as a boolean.
    # add argument for "target". set number of args to 1.
    parser.add_argument("-H", "--human-readable", action="store_true", help="print sizes in human readable format.")
    parser.add_argument("target", nargs="?", default=".", help="Required directory to scan.")
    args = parser.parse_args()
    return args


def percent_to_graph(percent: float, total_chars: int) -> str:
    "returns a string: eg. '##  ' for 50 if total_chars == 4"
    # Calculating the number of symbols that must be printed based on the given percent based on total_char
    num_symbols = round(percent * total_chars / 100)
    # Calculating the number of spaces
    num_spaces = total_chars - num_symbols
    # Returning the string with the required symbols and spaces
    return '#' * num_symbols + ' ' * num_spaces

def call_du_sub(location: str) -> list:
    "use subprocess to call `du -d 1 + location`, rtrn raw list"
    # Using subprocess to call the du -d 1 + location, rtrn raw list
    process = subprocess.Popen(['du', '-d', '1', location], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # Decoding the output
    output = stdout.decode('utf-8')
    lines = output.strip().split('\n')

    return lines

def create_dir_dict(raw_dat: list) -> dict:
    "get list from du_sub, return dict {'directory': 0} where 0 is size"
    " This function takes a list from the raw_dat variable as input, which is obtained from the call_du_sub function"

    directory_dict = {}

    for line in raw_dat:
        size, directory = line.split('\t')
        directory_dict[directory] = int(size)

    return directory_dict

def calculate_percent(size: int, total_size: int) -> float:
    # Calculating percentage based on the total_size
    return(size / total_size) * 100.0

def main():
    args = parse_command_args()

    # Getting the target directory and printing an error if the directory does not exist
    target = args.target
    if not os.path.exists(target) or not os.path.isdir(target):
        print(f"Error: '{target}' does not exist!")
        return

    # Calling the call_du_sub function with target directory
    raw_data = call_du_sub(target)

    # Creating a directory which contains directory sizes
    directory_sizes = create_dir_dict(raw_data)

    # Calculating total size of the directory
    total_size = sum(directory_sizes.values())

    # Printing the value
    print(f"Disk usage for '{target}' (Total Size: {total_size} bytes)")

    # Iterating through the subdirectories and calculating the percentages
    for directory, size in directory_sizes.items():
        if directory == target:
            continue # skips the directory
        percent = calculate_percent(size, total_size)
        graph = percent_to_graph(percent, args.length)
        print(f"{directory}: {graph} {percent:.2f}%")


if __name__ == "__main__":
    args = parse_command_args()
    
    " Calling call_du_sb with the target directory"
    raw_data = call_du_sub(args.target)

    " Creating a dictionary containing directory sizes"
    directory_sizes = create_dir_dict(raw_data)

    " Converting sizes to human readable format"
    if args.human_readable:
        for directory, size in directory_sizes.items():
            size_str = ''
            units = ['B', 'K', 'M', 'G', 'T']
            for unit in units:
                if size < 1024:
                    size_str = f"{size:.1f}{unit}"
                    break
                size /= 1024
                directory_sizes[directory] = size_str

    " Printing result"
    for directory, size in directory_sizes.items():
        graph = percent_to_graph(size, args.length)
        print(f"{directory}: {graph} {size}")

    main()
