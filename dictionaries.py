#!/usr/bin/env python3.7

import os

#Get current working directory
my_dir = os.getcwd()

#Create an empty list
file_info = []

#This will go through the directory to get the files including all information
for dirpath, dirnames, filenames in os.walk(my_dir):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        file_size = os.path.getsize(file_path)
        file_info.append({"name": file, "size": file_size})

#Print the list of files and all information
for file in file_info:
    print(file)