# Declare Vars
first_name = 'Rick'
last_name = 'Rivas'
person_bio = """
My name is Ricky Rivas and I am from Tulsa, Oklahoma. My knowledge of Javascript 
is making learning Python so easy. 
"""
my_age = 22

# Array methods
my_hobbies = []
my_hobbies.extend(['Web Dev', 'Web Design', 'Billiards'])
print(my_hobbies)


first_index = my_hobbies[0]
print(first_index)

# boolean var
user_logged_in = True
user_gold_status = False

# Declare functions
def printName(name):
    print(name)

# Call function
# printName(first_name)

# Find type
# print(type(my_age))

# Convert int to str
my_age_string = str(my_age)
# print(type(my_age_string))

# conditionals
if first_name == 'Ricky':
    print('First name is Ricky')
elif first_name == "Bryan":
    print('First name is Bryan')
else:
    print('First name not recognized...')

#boolean conditional
if user_logged_in & user_gold_status:
    print('User is logged in and is a premium user')
elif user_logged_in & user_gold_status == False:
    print('User is logged in as a regular user')

# Loops

for x in my_hobbies:
    printName(x)
