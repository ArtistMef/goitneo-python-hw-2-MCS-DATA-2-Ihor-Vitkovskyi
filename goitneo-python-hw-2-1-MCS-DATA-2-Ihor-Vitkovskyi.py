def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_phone(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return f"{name}'s phone updated to {new_phone}."
        else:
            raise KeyError
        
@input_error    
def phone_username(search_name, contacts):
    return contacts.get(search_name, "Contact not found")   

@input_error        
def all_contacts(contacts):
    if not contacts:
        return "Contact list is empty."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result       

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))    
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "phone":
            search_name = args[0]
            print(phone_username(search_name, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()