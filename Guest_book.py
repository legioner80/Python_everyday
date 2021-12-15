# Prompts for user their name.
# After entering heir name ,print a greeting.
# Add a line recording their visit in a file called quest_book.txt
filename = 'Guest_Book.txt'

print("Enter 'q' when finished.")
while True:
    name = input("What is your name? ")
    if name == 'q':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + "\n")
        print("Hello " + name + ", you've been added  to the guest book.")
