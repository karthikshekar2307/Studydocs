# Ask user for their name
name = input("What's your name? ").strip().title()

# Remove whitespace from str and capitalize user;s name
name = name.strip().title()


# split user name into first name and last name
first, last = name.split(" ")

# say hello to user
print(f"hello, {name}")