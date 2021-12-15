# Program that prompts the user for their name. When the user respond, their name is written in a separate txt.file.
name = input("What is your name? ")
filename = 'guest.txt'
with open(filename, 'w') as f:
    f.write(name)
