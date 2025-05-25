# Hassan - Week 8 User Input Assignment
# This program collects employee info and checks if it's valid using rules from class

# Step 1: Get Employee ID (must be a number, 7 digits max)
employee_id = input("Enter Employee ID (numbers only, up to 7 digits): ")
if not employee_id.isdigit() or len(employee_id) > 7:
    print("Invalid Employee ID. Program will now exit.")
    exit()

# Step 2: Get Employee Name (must be letters, no special characters)
employee_name = input("Enter Employee Name: ")
bad_name_chars = '!\"@#$%^&*()_=+<>/?;:[]{}\\'
if any(char in bad_name_chars for char in employee_name) or not employee_name.replace(" ", "").isalpha():
    print("Invalid Employee Name. Program will now exit.")
    exit()

# Step 3: Get Email Address (must not have disallowed characters, must have '@' and '.')
employee_email = input("Enter Employee Email Address: ")
bad_email_chars = '!\"\'#$%^&*()=+<>/?;:[]{}\\'
if any(char in bad_email_chars for char in employee_email) or "@" not in employee_email or "." not in employee_email:
    print("Invalid Email Address. Program will now exit.")
    exit()

# Step 4: Get Employee Address (optional, but must not contain bad characters if entered)
employee_address = input("Enter Employee Address (optional): ")
bad_address_chars = '!\"\'@$%^&*_=+<>?;:[]{}'
if employee_address != "":
    if any(char in bad_address_chars for char in employee_address):
        print("Invalid Address. Program will now exit.")
        exit()

# Step 5: Print final message if everything is valid
print(f"\nHello, {employee_name}. Your Employee ID is {employee_id}, and your email address is {employee_email}.")

if employee_address == "":
    print("You did not provide an address.")
else:
    print(f"Your address is {employee_address}.")
